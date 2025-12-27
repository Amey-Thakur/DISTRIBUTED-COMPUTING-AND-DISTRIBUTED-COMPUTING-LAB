# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: February 25, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 7 - Implementation of the Chandy-Misra-Haas (Edge-Chasing) Algorithm for Distributed Deadlock Detection.

class DeadlockDetector:
    """
    Implements the Chandy-Misra-Haas edge-chasing algorithm.
    This algorithm detects deadlocks by sending 'probes' along the edges of the 
    Wait-For-Graph (WFG). A deadlock is detected if the initiator receives its own probe.
    """
    def __init__(self, num_processes):
        self.n = num_processes
        self.deadlock_found = False

    def detect_deadlock(self, weight_matrix, initiator_site):
        """
        Initiates the probe-based deadlock detection from a specific process.
        """
        self.deadlock_found = False
        initiator_idx = initiator_site - 1
        
        print(f"\n[*] Initiating probe from Process P{initiator_site}...")
        
        # Start the recursive probe passing
        for target in range(self.n):
            if weight_matrix[initiator_idx][target] == 1:
                print(f"    -> Probe (Initiator: P{initiator_site}, Sender: P{initiator_site}, Receiver: P{target + 1})")
                self._send_probe(weight_matrix, initiator_idx, target)
        
        if not self.deadlock_found:
            print("\n[RESULT] No deadlock detected from this initiator site.")
        else:
            print("\n[RESULT] DISTRIBUTED DEADLOCK DETECTED!")

    def _send_probe(self, matrix, initiator_idx, current_idx):
        """
        Recursive function to propagate the probe through the Wait-For-Graph.
        Probe structure: (Initiator, Sender, Receiver)
        """
        if self.deadlock_found:
            return

        for next_node in range(self.n):
            if matrix[current_idx][next_node] == 1:
                # If the probe returns to the initiator, a cycle (deadlock) exists
                if next_node == initiator_idx:
                    print(f"    !! Probe returned to Initiator: P{initiator_idx + 1} !!")
                    print(f"    !! (P{initiator_idx + 1}, P{current_idx + 1}, P{next_node + 1})")
                    self.deadlock_found = True
                    return
                
                print(f"    -> Probe (Initiator: P{initiator_idx + 1}, Sender: P{current_idx + 1}, Receiver: P{next_node + 1})")
                self._send_probe(matrix, initiator_idx, next_node)

def main():
    print("="*60)
    print(" CHANDY-MISRA-HAAS DEADLOCK DETECTION ALGORITHM ")
    print("="*60)

    # Standard 5-process scenarios from the experiment
    scenarios = {
        "1": {
            "name": "No Deadlock Scenario",
            "matrix": [
                [0, 1, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 1, 1], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]
            ]
        },
        "2": {
            "name": "Deadlock Scenario (P4 -> P1 Cycle)",
            "matrix": [
                [0, 1, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 1, 1], 
                [1, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]
            ]
        }
    }

    print("\nAvailable Scenarios:")
    for key, data in scenarios.items():
        print(f"  {key}. {data['name']}")
    
    choice = input("\n[?] Select scenario (1/2): ")
    if choice not in scenarios:
        print("[!] Invalid choice. Defaulting to No Deadlock Scenario.")
        choice = "1"

    current_matrix = scenarios[choice]["matrix"]
    
    # Visualizing the Wait-For-Graph (WFG) Matrix
    print("\n[*] Wait-For-Graph (Adjacency Matrix):")
    print("     P1  P2  P3  P4  P5")
    for i, row in enumerate(current_matrix):
        print(f"P{i+1}  " + "   ".join(map(str, row)))

    try:
        initiator = int(input("\n[?] Enter process number to initiate detection (1-5): "))
        if 1 <= initiator <= 5:
            detector = DeadlockDetector(5)
            detector.detect_deadlock(current_matrix, initiator)
        else:
            print("[!] Process out of range.")
    except ValueError:
        print("[!] Please enter a valid numerical ID.")

    print("\n" + "="*60)

if __name__ == "__main__":
    main()
