# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: February 25, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 7 - Implementation of Chandy-Misra-Haas Distributed Deadlock Detection Algorithm (Scenario: Deadlock Detected).

# Wait-For-Graph (WFG) Matrix representing process dependencies
# A cycle exists here: P1 -> P2 -> P3 -> P4 -> P1
print('''
Wait-For-Graph (Adjacency Matrix):
     P1  P2  P3  P4  P5

P1   0   1   0   0   0
P2   0   0   1   0   0
P3   0   0   0   1   1
P4   1   0   0   0   0
P5   0   0   0   0   0 
''')

# 1 indicates a dependency (P_row depends on P_col)
dependency_matrix = [
    [0, 1, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [0, 0, 0, 1, 1], 
    [1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0]
]

deadlock_detected = False

def propagate_probe(matrix, initiator_idx, current_idx):
    """
    Sends a probe along the edges of the Wait-For-Graph.
    If the probe returns to the initiator, a deadlock is detected.
    """
    global deadlock_detected
    num_nodes = 5
   
    for next_node in range(num_nodes):
        if matrix[current_idx][next_node] == 1:
            # Check for cycle (Deadlock Condition)
            if initiator_idx == next_node:
                print(f" [*] S{current_idx+1} ==> S{next_node+1} | Probe:({initiator_idx+1}, {current_idx+1}, {next_node+1}) --------> DEADLOCK DETECTED")
                deadlock_detected = True
                break
                
            print(f" [*] S{current_idx+1} ==> S{next_node+1} | Probe:({initiator_idx+1}, {current_idx+1}, {next_node+1})")
            propagate_probe(matrix, initiator_idx, next_node)

def main():
    print("="*60)
    print(" CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION (DEADLOCK CASE) ")
    print("="*60)

    try:
        initiator = int(input("[?] Enter Initiator Site No. (1-5): "))
        initiator_idx = initiator - 1

        print(f"\n[*] Probe propagation starting from Site P{initiator}...")
        
        # Initial probe transmission from the initiator
        for target in range(5):
            if dependency_matrix[initiator_idx][target] == 1:
                print(f" [*] S{initiator_idx+1} ==> S{target+1} | Probe:({initiator}, {initiator_idx+1}, {target+1})")
                propagate_probe(dependency_matrix, initiator_idx, target)

        if not deadlock_detected: 
            print("\n[RESULT] No deadlock detected from this initiator.")
            
    except ValueError:
        print("[!] Invalid input. Please enter a numerical process ID.")
    except Exception as e:
        print(f"[!] Error: {e}")

    print("\n" + "_"*60)

if __name__ == "__main__":
    main()
