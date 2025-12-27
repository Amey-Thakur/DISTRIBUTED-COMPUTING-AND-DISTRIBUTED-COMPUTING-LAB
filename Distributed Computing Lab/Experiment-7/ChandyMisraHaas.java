/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: February 25, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 7 - Java Implementation of the Chandy-Misra-Haas (Edge-Chasing) Algorithm for Distributed Deadlock Detection.
 */

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class ChandyMisraHaas {
    private static int numProcesses = 5;
    private static int[][] waitMatrix;
    private static boolean deadlockDetected = false;

    /**
     * Entry point for the Deadlock Detection Simulator.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--- [CHANDY-MISRA-HAAS DEADLOCK DETECTION SIMULATOR] ---");
        
        // Define standard scenarios
        System.out.println("\nSelect Scenario:");
        System.out.println("1. Deadlock Configuration (Cycle: P1 -> P2 -> P3 -> P4 -> P1)");
        System.out.println("2. No Deadlock Configuration");
        System.out.print("[?] Choice (1/2): ");
        int choice = sc.nextInt();

        initializeScenario(choice);

        // Visualize WFG
        displayWFG();

        System.out.print("\n[?] Enter Initiator Process ID (1-" + numProcesses + "): ");
        int initiator = sc.nextInt();

        if (initiator < 1 || initiator > numProcesses) {
            System.out.println("[!] Invalid Process ID.");
        } else {
            initiateDetection(initiator);
        }

        sc.close();
    }

    /**
     * Sets up the Wait-For-Graph based on the selected scenario.
     */
    private static void initializeScenario(int choice) {
        waitMatrix = new int[numProcesses][numProcesses];
        
        // Basic dependencies present in both
        waitMatrix[0][1] = 1; // P1 -> P2
        waitMatrix[1][2] = 1; // P2 -> P3
        waitMatrix[2][3] = 1; // P3 -> P4
        waitMatrix[2][4] = 1; // P3 -> P5

        if (choice == 1) {
            waitMatrix[3][0] = 1; // P4 -> P1 (Creates Cycle)
            System.out.println("[*] Scenario Loaded: DEADLOCK CONFIGURATION");
        } else {
            System.out.println("[*] Scenario Loaded: NO DEADLOCK CONFIGURATION");
        }
    }

    /**
     * Displays the Wait-For-Graph adjacency matrix.
     */
    private static void displayWFG() {
        System.out.println("\nWait-For-Graph (Adjacency Matrix):");
        System.out.println("     P1  P2  P3  P4  P5");
        for (int i = 0; i < numProcesses; i++) {
            System.out.print("P" + (i + 1) + "  ");
            for (int j = 0; j < numProcesses; j++) {
                System.out.print(waitMatrix[i][j] + "   ");
            }
            System.out.println();
        }
    }

    /**
     * Starts the probe-based detection.
     */
    private static void initiateDetection(int initiatorSite) {
        int initiatorIdx = initiatorSite - 1;
        deadlockDetected = false;

        System.out.println("\n[*] Initiating probe from P" + initiatorSite + "...");
        
        for (int target = 0; target < numProcesses; target++) {
            if (waitMatrix[initiatorIdx][target] == 1) {
                System.out.println("    -> Sending Probe (Init:" + initiatorSite + ", From:" + initiatorSite + ", To:" + (target + 1) + ")");
                propagateProbe(initiatorIdx, target);
            }
        }

        if (!deadlockDetected) {
            System.out.println("\n[RESULT] Verification Complete: NO DEADLOCK DETECTED.");
        } else {
            System.out.println("\n[RESULT] CRITICAL: DISTRIBUTED DEADLOCK DETECTED!");
        }
    }

    /**
     * Recursive function to pass the probe along WFG edges.
     */
    private static void propagateProbe(int initiatorIdx, int currentIdx) {
        if (deadlockDetected) return;

        for (int next = 0; next < numProcesses; next++) {
            if (waitMatrix[currentIdx][next] == 1) {
                // If probe returns to initiator, deadlock exists
                if (next == initiatorIdx) {
                    System.out.println("    !! Probe returned to Initiator P" + (initiatorIdx + 1) + " !!");
                    System.out.println("    !! Path: (Init:" + (initiatorIdx + 1) + ", From:" + (currentIdx + 1) + ", To:" + (next + 1) + ")");
                    deadlockDetected = true;
                    return;
                }

                System.out.println("    -> Sending Probe (Init:" + (initiatorIdx + 1) + ", From:" + (currentIdx + 1) + ", To:" + (next + 1) + ")");
                propagateProbe(initiatorIdx, next);
            }
        }
    }
}
