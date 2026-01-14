# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: March 11, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 8 - Implementation of a Static Load Balancing Algorithm using multithreading in Python.

import threading
import time

# Global variables for cross-thread communication
shared_remainder = 0
lock = threading.Lock()

def processor_1_execution(limit, total_tasks):
    """
    Simulates the first processor's execution logic.
    Identifies overload and calculates tasks to be migrated.
    """
    global shared_remainder
    
    print(f"\n[PROCESSOR 1] Status (Capacity: {limit})")
    
    if total_tasks == 0:
        print("  -> No processes available for execution.")
        with lock:
            shared_remainder = 0
        return

    if limit > total_tasks:
        print("  -> State: Underloaded")
        print(f"  -> Executed: {total_tasks} processes.")
        rem = 0
    elif limit == total_tasks:
        print("  -> State: Normal Load")
        print(f"  -> Executed: {total_tasks} processes.")
        print("  -> Result: No tasks forwarded.")
        rem = 0
    else:
        print("  -> State: OVERLOADED")
        print(f"  -> Executed: {limit} processes (Max Capacity).")
        rem = total_tasks - limit
        print(f"  -> Overflow: {rem} processes forwarded to Processor 2.")

    with lock:
        shared_remainder = rem

def processor_2_execution(limit):
    """
    Simulates the second processor's execution logic.
    Executes overflow tasks received from Processor 1.
    """
    # Delay to ensure Processor 1 finishes distribution
    time.sleep(2)
    
    print(f"\n[PROCESSOR 2] Status (Capacity: {limit})")
    
    with lock:
        workload = shared_remainder

    if workload == 0:
        print("  -> No overflow tasks received from Processor 1.")
    else:
        if limit > workload:
            print("  -> State: Underloaded")
            print(f"  -> Executed: {workload} processes.")
        elif limit == workload:
            print("  -> State: Normal Load")
            print(f"  -> Executed: {workload} processes.")
        else:
            print("  -> State: OVERLOADED")
            print(f"  -> Executed: {limit} processes (Max Capacity).")
            final_rem = workload - limit
            print(f"  -> Critical: {final_rem} processes still queued (System Overloaded).")

def main():
    print("="*60)
    print(" STATIC LOAD BALANCING SIMULATOR (PYTHON) ")
    print("="*60)

    try:
        l1 = int(input("Enter execution limit for Processor 1: "))
        l2 = int(input("Enter execution limit for Processor 2: "))
        n = int(input("Enter total number of processes: "))

        # Creating threads for distributed processing
        t1 = threading.Thread(target=processor_1_execution, args=(l1, n))
        t2 = threading.Thread(target=processor_2_execution, args=(l2,))

        # Starting parallel simulation
        t1.start()
        t2.start()

        # Waiting for completion
        t1.join()
        t2.join()

    except ValueError:
        print("[!] Input Error: Please enter numerical values for limits and processes.")

    print("\n" + "="*60)

if __name__ == "__main__":
    main()