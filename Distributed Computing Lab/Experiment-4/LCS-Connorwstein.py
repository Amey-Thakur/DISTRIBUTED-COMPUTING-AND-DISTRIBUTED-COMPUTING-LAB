# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: February 3, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 4 - Multi-threaded Implementation of Lamport's Distributed Mutual Exclusion Algorithm using Logical Clocks.

import signal
import sys
import time
import threading
from queue import Queue

# Global Configuration
INITIALLY_GRANTED_PROC = "A"
PROCESS_IDENTIFIERS = {"A", "B", "C"}
resource_usage_counts = {"A": 0, "B": 0, "C": 0}
message_queues = {"A": Queue(), "B": Queue(), "C": Queue()}

class Message:
    """
    Represents a communication packet in the distributed system.
    Contains metadata for message type, logical timestamp, and routing information.
    """
    def __init__(self, msg_type, timestamp, sender, receiver):
        self.msg_type = msg_type
        self.timestamp = timestamp
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return f"Message({self.msg_type}, TS:{self.timestamp}, From:{self.sender}, To:{self.receiver})"

class Process(threading.Thread):
    """
    Simulates a discrete process in a distributed environment.
    Uses Lamport's Logical Clock to manage priority in a shared resource request queue.
    """
    def __init__(self, name, initially_granted, other_processes):
        super(Process, self).__init__()
        self.name = name
        self.has_resource = initially_granted == name
        self.other_processes = other_processes
        self.lamport_clock = 0  # Internal logical clock (ticked after each event)
        self.request_queue = []
        self.requested = False
        
        # Initialize the request queue with the starting grant
        self.request_queue.append(Message("request", -1, initially_granted, initially_granted))

    def remove_request(self, msg_type, sender):
        """Removes a processed request from the internal priority queue."""
        index_to_remove = -1
        for i, req in enumerate(self.request_queue):
            if req.msg_type == msg_type and req.sender == sender:
                index_to_remove = i
                break
        
        if index_to_remove != -1:
            del self.request_queue[index_to_remove]
        else:
            print(f"[*] Process {self.name}: Warning - Request not found for removal.")

    def use_resource(self):
        """Simulates critical section execution."""
        print(f"[!] Process {self.name} is executing in the CRITICAL SECTION.")
        resource_usage_counts[self.name] += 1
        time.sleep(2)  # Simulate work duration

    def handle_message(self, msg):
        """Processes incoming messages based on their type (request/release/ack)."""
        if msg.msg_type == "request":
            # Add neighbor's request to local queue and respond with an Acknowledgement (ACK)
            self.request_queue.append(msg)
            for proc in self.other_processes:
                if proc == msg.sender:
                    message_queues[proc].put(Message("ack", self.lamport_clock, self.name, msg.sender))
        
        elif msg.msg_type == "release":
            # Remove the releasing process's request from local priority queue
            self.remove_request("request", msg.sender)
            
        elif msg.msg_type == "ack":
            # ACKs are implicitly handled by checking if newer timestamps are received from all nodes
            pass
            
        else:
            print(f"[?] Process {self.name}: Received unknown message type: {msg.msg_type}")

    def run(self):
        """Main process execution loop."""
        while True:
            # Case 1: Process currently holds the resource
            if self.has_resource:
                self.use_resource()
                self.remove_request("request", self.name)
                
                # Broadcast RELEASE message to all other processes
                for proc in self.other_processes:
                    message_queues[proc].put(Message("release", self.lamport_clock, self.name, proc))
                    self.lamport_clock += 1
                
                self.has_resource, self.requested = False, False
                continue

            # Case 2: Process wants to acquire the resource
            if not self.requested:
                print(f"[*] Process {self.name} is initiating a RESOURCE REQUEST.")
                # Add local request to own queue
                self.request_queue.append(Message("request", self.lamport_clock, self.name, self.name))
                
                # Broadcast REQUEST message to all peers
                for proc in self.other_processes:
                    message_queues[proc].put(Message("request", self.lamport_clock, self.name, proc))
                    self.lamport_clock += 1
                self.requested = True
            
            else:
                # Case 3: Process is waiting for permission/synchronization
                print(f"[*] Process {self.name} is waiting for synchronization...")
                msg = message_queues[self.name].get(block=True)        
                
                # Update Lamport Clock: L(e) = max(L(local), L(received) + 1)
                if msg.timestamp >= self.lamport_clock:
                    self.lamport_clock = msg.timestamp + 1
                
                print(f"[+] Process {self.name} received: {msg}")
                self.handle_message(msg)
                self.lamport_clock += 1
                
                # Check if resource acquisition conditions are met
                if self.is_resource_available():
                    print(f"[#] Resource access GRANTED to {self.name}")
                    self.has_resource = True

            print(f"--- Process {self.name} State | Queue Size: {len(self.request_queue)} | Clock: {self.lamport_clock} ---")
            time.sleep(1)

    def is_resource_available(self):
        """
        Conditions for resource acquisition in Lamport's Mutual Exclusion:
        1. Local request must be at the head of the priority queue (lowest timestamp).
        2. A message with a higher timestamp must have been received from every other process.
        """
        peer_acknowledgements = {p: False for p in self.other_processes}
        local_request = None
        
        # Locate the local request in our queue
        for req in self.request_queue:
            if req.sender == self.name:
                local_request = req
                break
        
        if local_request is None:
            return False
            
        # Verify if our request is older (lower timestamp) than any other message received from peers
        for req in self.request_queue:
            if req.sender in peer_acknowledgements and req.timestamp > local_request.timestamp:
                peer_acknowledgements[req.sender] = True
        
        return all(peer_acknowledgements.values())

def main():
    print("="*60)
    print(" LAMPORT DISTRIBUTED MUTUAL EXCLUSION SIMULATOR ")
    print("="*60)
    
    # Initialize and start discrete process threads
    node_a = Process("A", INITIALLY_GRANTED_PROC, list(PROCESS_IDENTIFIERS - {"A"}))
    node_b = Process("B", INITIALLY_GRANTED_PROC, list(PROCESS_IDENTIFIERS - {"B"}))
    node_c = Process("C", INITIALLY_GRANTED_PROC, list(PROCESS_IDENTIFIERS - {"C"}))

    # Configure as daemon threads to allow clean exit on main thread termination
    node_a.daemon = True
    node_b.daemon = True
    node_c.daemon = True

    try:
        node_a.start()
        node_b.start()
        node_c.start()
        
        while True:
            # Synchronize thread joining with a timeout to maintain responsiveness
            node_a.join(5)
            node_b.join(5)
            node_c.join(5)
            
    except KeyboardInterrupt:
        print("\n\n[!] Execution Interrupted by User.")
        print("-" * 30)
        print(" FINAL RESOURCE USAGE STATISTICS ")
        print("-" * 30)
        for process, count in resource_usage_counts.items():
            print(f"Process {process}: {count} critical section entries.")
        print("-" * 30)
        sys.exit(0)

if __name__ == "__main__":
    main()