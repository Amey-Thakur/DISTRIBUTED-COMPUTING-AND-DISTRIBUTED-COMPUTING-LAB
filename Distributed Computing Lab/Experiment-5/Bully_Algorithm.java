/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: February 10, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 5 - Implementation of the Bully Algorithm for Leader Election in Distributed Systems.
 */

import java.util.Scanner;

public class Bully_Algorithm {
    /**
     * The Bully Algorithm is used to elect a coordinator (leader) among a group 
     * of processes. The process with the highest process ID is always chosen.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("--- [BULLY ALGORITHM SIMULATOR] ---");
        
        // 1. Initialize process pool
        System.out.print("[?] Enter the total number of processes: ");
        int totalProcesses = scanner.nextInt();
        
        // Array to store active (1) or failed (0) status of processes
        int[] processStatus = new int[totalProcesses];
        
        // 2. Define failure scenario
        System.out.print("[?] Enter the process ID (0 to " + (totalProcesses - 1) + ") that has failed: ");
        int failedProcess = scanner.nextInt();

        // Populate initial process states
        for (int i = 0; i < totalProcesses; i++) {
            if (i == failedProcess) {
                processStatus[i] = 0; // 0 indicates the process is offline/failed
            } else {
                processStatus[i] = 1; // 1 indicates the process is operational
            }
        }

        // 3. Initiate election
        System.out.print("[?] Enter the process ID that detects failure and starts election: ");
        int electionInitiator = scanner.nextInt();

        System.out.println("\n[*] Election Process Started by Node " + electionInitiator + "...");

        int currentProcess = electionInitiator;
        int lastSuccessfulCoordinatorCandidate = -1;

        // 4. Iterate through higher-ID processes to find the new coordinator
        while (currentProcess < totalProcesses) {
            
            // Skip the failed process if it happens to be the one we are evaluating
            if (currentProcess == failedProcess) {
                currentProcess++;
                continue;
            }

            boolean receivedOk = false;
            System.out.println("\n[Node " + currentProcess + "]: Broadcasting ELECTION messages to nodes with higher IDs...");

            // Send election messages to all processes with higher IDs
            for (int j = currentProcess + 1; j < totalProcesses; j++) {
                System.out.println("    -> Sending ELECTION message to Node " + j);
                
                // If a higher process is active, it sends an OK message back
                if (processStatus[j] == 1) {
                    System.out.println("    <- [OK] received from Node " + j);
                    receivedOk = true;
                }
            }

            // If no higher active process responds with OK, this process becomes the winner/coordinator
            if (!receivedOk) {
                lastSuccessfulCoordinatorCandidate = currentProcess;
            }
            
            currentProcess++;
        }

        // 5. Announce the result
        System.out.println("\n" + "=".repeat(40));
        System.out.println(" ELECTION RESULT: COORDINATOR IDENTIFIED ");
        System.out.println("=".repeat(40));
        System.out.println("[RESULT] Process " + lastSuccessfulCoordinatorCandidate + " is now the NEW COORDINATOR.");
        System.out.println("=".repeat(40));

        scanner.close();
    }
}