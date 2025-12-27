# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: February 25, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 7 - Unified implementation of Chandy-Misra-Haas Deadlock Detection Algorithm (Deadlock & No-Deadlock scenarios).

class ChandyMisraHaas:
    """
    Implements the Chandy-Misra-Haas edge-chasing algorithm.
    This algorithm detects distributed deadlock by sending probes along the Wait-For-Graph.
    """
    def __init__(self, n):
        self.n = n
        self.deadlock_found = False

    def reset(self):
        self.deadlock_found = False

    def initiate_probe(self, matrix, initiator):
        """
        Starts the probe-sending process from a detected wait condition.
        """
        self.reset()
        idx = initiator - 1
        print(f"\n[*] Site S{initiator} initiating deadlock detection probe...")
        
        for next_node in range(self.n):
            if matrix[idx][next_node] == 1:
                print(f"    -> Probe Sent: (Init:{initiator}, Sender:{initiator}, Receiver:{next_node+1})")
                self.propagate(matrix, idx, next_node)
        
        if not self.deadlock_found:
            print(f"\n[RESULT] Verification Successful: No deadlock detected from initiator S{initiator}.")
        else:
            print(f"\n[RESULT] CRITICAL: DISTRIBUTED DEADLOCK DETECTED (Cycle detected at Site S{initiator}).")

    def propagate(self, matrix, initiator_idx, current_idx):
        """
        Recursively propagates the probe (Initiator, Sender, Receiver).
        """
        if self.deadlock_found:
            return

        for k in range(self.n):
            if matrix[current_idx][k] == 1:
                # If probe returns to initiator, a cycle exists
                if k == initiator_idx:
                    print(f"    !! Deadlock: Probe (Init:{initiator_idx+1}, Sender:{current_idx+1}, Receiver:{k+1}) returned to initiator !!")
                    self.deadlock_found = True
                    return
                
                print(f"    -> Probe Forwarded: (Init:{initiator_idx+1}, Sender:{current_idx+1}, Receiver:{k+1})")
                self.propagate(matrix, initiator_idx, k)

def main():
    print("="*65)
    print(" CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION SIMULATOR ")
    print("="*65)

    scenarios = {
        "1": {
            "name": "Scenario A: Deadlock Case (Cycle: P1->P2->P3->P4->P1)",
            "matrix": [
                [0, 1, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 1, 1], 
                [1, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]
            ]
        },
        "2": {
            "name": "Scenario B: No-Deadlock Case (Acyclic Graph)",
            "matrix": [
                [0, 1, 0, 0, 0], 
                [0, 0, 1, 0, 0], 
                [0, 0, 0, 1, 1], 
                [0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0]
            ]
        }
    }

    print("\nSelect Experimental Configuration:")
    for k, v in scenarios.items():
        print(f"  {k}. {v['name']}")
    
    choice = input("\n[?] Enter choice (1/2): ")
    if choice not in scenarios:
        print("[!] Invalid selection.")
        return

    matrix = scenarios[choice]["matrix"]
    
    print("\n[*] Wait-For-Graph Adjacency Matrix:")
    print("     P1  P2  P3  P4  P5")
    for i, row in enumerate(matrix):
        print(f"P{i+1}  " + "   ".join(map(str, row)))

    try:
        initiator = int(input("\n[?] Enter site initiating detection (1-5): "))
        if 1 <= initiator <= 5:
            detector = ChandyMisraHaas(5)
            detector.initiate_probe(matrix, initiator)
        else:
            print("[!] Site number must be between 1 and 5.")
    except ValueError:
        print("[!] Error: Invalid numeric input.")

    print("\n" + "="*65)

if __name__ == "__main__":
    main()
