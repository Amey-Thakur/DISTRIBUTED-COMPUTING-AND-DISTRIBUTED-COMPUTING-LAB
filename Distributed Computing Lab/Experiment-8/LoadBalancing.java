/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: March 11, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 8 - Implementation of a Static Load Balancing Algorithm using multithreading in Java.
 * This simulation assumes a multi-processor system where tasks are distributed based on processor capacity (limits).
 */

import java.util.Scanner;

public class LoadBalancing {
    // Shared state variables for thread communication
    public static int l1; // Limit for Processor 1
    public static int l2; // Limit for Processor 2
    public static int n;  // Total number of processes to be executed
    public static int r1; // Remainder (overflow) from Processor 1

    public static void main(String[] args) {
        r1 = 0;
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--- [STATIC LOAD BALANCING SIMULATOR] ---");
        System.out.println("[*] Assumption: Two Processors in the system.");
        
        // Input phase
        System.out.print("Enter execution limit for Processor 1: ");
        l1 = sc.nextInt();
        
        System.out.print("Enter execution limit for Processor 2: ");
        l2 = sc.nextInt();
        
        System.out.print("Enter total number of processes to execute: ");
        n = sc.nextInt();
        
        // Task distribution using individual threads for each processor
        Runnable r1Handler = new Processor1Handler();
        Thread t1 = new Thread(r1Handler);
        
        Runnable r2Handler = new Processor2Handler();
        Thread t2 = new Thread(r2Handler);
        
        // Start multi-threaded execution
        t1.start();
        t2.start();
        
        // Close scanner
        sc.close();
    }
}

/**
 * Handler for the first processor logic.
 */
class Processor1Handler implements Runnable {
    public void run() {
        System.out.println("\n[PROCESSOR 1] Status (Capacity: " + LoadBalancing.l1 + ")");
        int limit = LoadBalancing.l1;
        int total = LoadBalancing.n;
        int remaining = 0;

        if (total == 0) {
            System.out.println("  -> No processes available for execution.");
        } else {
            if (limit > total) {
                System.out.println("  -> State: Underloaded");
                System.out.println("  -> Executed: " + total + " processes.");
            } else if (limit == total) {
                System.out.println("  -> State: Normal Load");
                System.out.println("  -> Executed: " + total + " processes.");
                System.out.println("  -> Result: All tasks completed at local site.");
            } else {
                System.out.println("  -> State: OVERLOADED");
                System.out.println("  -> Executed: " + limit + " processes (Max Capacity).");
                remaining = total - limit;
                System.out.println("  -> Overflow: " + remaining + " processes forwarded to Processor 2.");
            }
        }
        // Update shared remainder for Processor 2
        LoadBalancing.r1 = remaining;
    }
}

/**
 * Handler for the second processor logic. 
 * Includes a brief sleep to ensure sequential logic demonstration.
 */
class Processor2Handler implements Runnable {
    public void run() {
        try {
            // Simulated delay to ensure Processor 1 finishes calculation
            Thread.sleep(2000); 
        } catch (InterruptedException e) {
            System.err.println("Thread Interrupted: " + e.getMessage());
        }

        System.out.println("\n[PROCESSOR 2] Status (Capacity: " + LoadBalancing.l2 + ")");
        int limit = LoadBalancing.l2;
        int workload = LoadBalancing.r1; // Gets overflow from P1

        if (workload == 0) {
            System.out.println("  -> No overflow tasks received from Processor 1.");
        } else {
            if (limit > workload) {
                System.out.println("  -> State: Underloaded");
                System.out.println("  -> Executed: " + workload + " processes.");
            } else if (limit == workload) {
                System.out.println("  -> State: Normal Load");
                System.out.println("  -> Executed: " + workload + " processes.");
            } else {
                System.out.println("  -> State: OVERLOADED");
                System.out.println("  -> Executed: " + limit + " processes (Max Capacity).");
                int finalRemainder = workload - limit;
                System.out.println("  -> Critical: " + finalRemainder + " processes still queued (System Overloaded).");
            }
        }
    }
}
