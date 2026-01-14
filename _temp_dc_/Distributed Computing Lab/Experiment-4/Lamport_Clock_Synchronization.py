# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: February 3, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 4 - Implementation of Lamport's Logical Clock Algorithm for event synchronization in distributed systems.

def get_max(a, b):
    """
    Returns the maximum of two values. 
    Used to update logical clocks upon message receipt.
    """
    return a if a > b else b

def display_timestamps(e1_count, e2_count, p1_clocks, p2_clocks):
    """
    Formats and displays the final logical timestamps for all events in processes P1 and P2.
    """
    print("\n" + "="*40)
    print(" LAMPORT LOGICAL CLOCK RESULTS ")
    print("="*40)
    
    print(f"\nTime stamps of events in Process P1 (e1_1 to e1_{e1_count}):")
    print("  ", "  ".join(map(str, p1_clocks)))
    
    print(f"\nTime stamps of events in Process P2 (e2_1 to e2_{e2_count}):")
    print("  ", "  ".join(map(str, p2_clocks)))
    print("="*40 + "\n")

def compute_lamport_clock(e1, e2, message_matrix):
    """
    Computes logical timestamps based on Lamport's algorithm.
    Rules:
    1. Local events increment the clock by 1.
    2. Message Receipt: clock = max(local_clock, received_timestamp + 1)
    """
    # Initialize clock arrays with sequential local increments
    p1 = [i + 1 for i in range(e1)]
    p2 = [i + 1 for i in range(e2)]

    print("\n[*] Initializing Dependency Matrix (Event Interactions):")
    # Display the communication matrix for user clarity
    header = "\t" + "\t".join([f"e2_{j+1}" for j in range(e2)])
    print(header)
    
    for i in range(e1):
        row = f"e1_{i+1}\t" + "\t".join(map(str, message_matrix[i]))
        print(row)

    # Process events and synchronize clocks based on message matrix
    # Matrix semantics: 
    # 1  => Message sent from e1_i to e2_j
    # -1 => Message received by e1_i from e2_j
    for i in range(e1):
        for j in range(e2):
            
            # Case 1: Message sent from P1 to P2
            if message_matrix[i][j] == 1:
                # Update receiver's timestamp
                p2[j] = get_max(p2[j], p1[i] + 1)
                # Resynchronize subsequent local events in P2
                for k in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1

            # Case 2: Message sent from P2 to P1
            if message_matrix[i][j] == -1:
                # Update receiver's timestamp
                p1[i] = get_max(p1[i], p2[j] + 1)
                # Resynchronize subsequent local events in P1
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    # Output results
    display_timestamps(e1, e2, p1, p2)

if __name__ == "__main__":
    # Define number of events in Process 1 and Process 2
    num_events_p1 = 5
    num_events_p2 = 3
    
    # Initialize communication matrix (5 rows for P1, 3 columns for P2)
    # m[i][j] = 1 if P1 sends message at i to P2 at j
    # m[i][j] = -1 if P1 receives message from P2 at j at its event i
    comm_matrix = [[0 for _ in range(num_events_p2)] for _ in range(num_events_p1)]
    
    # Define interactions (based on experimental setup)
    # Example: P1 sends message at event 2 (index 1) to P2 at event 3 (index 2)
    comm_matrix[1][2] = 1
    
    # Example: P1 receives message from P2 at event 2 (index 1) during its event 5 (index 4)
    comm_matrix[4][1] = -1
    
    compute_lamport_clock(num_events_p1, num_events_p2, comm_matrix)
