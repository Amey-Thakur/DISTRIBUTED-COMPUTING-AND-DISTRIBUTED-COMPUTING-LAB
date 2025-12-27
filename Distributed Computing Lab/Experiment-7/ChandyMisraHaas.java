/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: February 25, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 7 - Unified implementation of Chandy-Misra-Haas Deadlock Detection Algorithm (Deadlock & No-Deadlock scenarios).
 */

import java.util.Scanner;

public class ChandyMisraHaas {
    private static int numProcesses = 5;
    private static int[][] waitMatrix;
    private static boolean deadlockDetected = false;

    /**
     * Entry point for the Chandy-Misra-Haas Deadlock Detection Simulator.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=" + "=".repeat(63));
        System.out.println(" CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION SIMULATOR (JAVA) ");
        System.out.println("=" + "=".repeat(63));
        
        // 1. Configuration Selection
        System.out.println("\nSelect Experimental Configuration:");
        System.out.println("  1. Scenario A: Deadlock Case (Cycle: P1->P2->P3->P4->P1)");
        System.out.println("  2. Scenario B: No-Deadlock Case (Acyclic Graph)");
        System.out.print("\n[?] Enter choice (1/2): ");
        int choice = scanner.nextInt();

        if (choice != 1 && choice != 2) {
            System.out.println("[!] Invalid selection. Terminating.");
            scanner.close();
            return;
        }

        initializeWaitGraph(choice);

        // 2. WFG Visualization
        displayWaitGraph();

        // 3. Probe Initiation
        System.out.print("\n[?] Enter site ID initiating detection (1-" + numProcesses + "): ");
        int initiator = scanner.nextInt();

        if (initiator >= 1 && initiator <= numProcesses) {
            startDetection(initiator);
        } else {
            System.out.println("[!] Error: Site ID must be between 1 and " + numProcesses);
        }

        System.out.println("\n" + "=".repeat(65));
        scanner.close();
    }

    /**
     * Initializes the Adjacency Matrix for the Wait-For-Graph.
     */
    private static void initializeWaitGraph(int scenario) {
        waitMatrix = new int[numProcesses][numProcesses];
        
        // Common dependencies in both scenarios
        waitMatrix[0][1] = 1; // P1 depends on P2
        waitMatrix[1][2] = 1; // P2 depends on P3
        waitMatrix[2][3] = 1; // P3 depends on P4
        waitMatrix[2][4] = 1; // P3 depends on P5

        if (scenario == 1) {
            waitMatrix[3][0] = 1; // P4 depends on P1 (Closing the cycle: 1->2->3->4->1)
            System.out.println("\n[*] STATUS: Deadlock Scenario loaded.");
        } else {
            System.out.println("\n[*] STATUS: No-Deadlock Scenario loaded.");
        }
    }

    /**
     * Visualizes the current dependency state.
     */
    private static void displayWaitGraph() {
        System.out.println("\n[*] Wait-For-Graph Adjacency Matrix:");
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
     * Facilitates the edge-chasing probe mechanism.
     */
    private static void startDetection(int initiatorSite) {
        int initiatorIdx = initiatorSite - 1;
        deadlockDetected = false;

        System.out.println("\n[*] Site S" + initiatorSite + " initiating deadlock detection probe...");
        
        for (int target = 0; target < numProcesses; target++) {
            if (waitMatrix[initiatorIdx][target] == 1) {
                System.out.println("    -> Sending Probe: (Init:" + initiatorSite + ", Sender:" + initiatorSite + ", Receiver:" + (target + 1) + ")");
                propagateProbe(initiatorIdx, target);
            }
        }

        if (deadlockDetected) {
            System.out.println("\n[RESULT] CRITICAL: DISTRIBUTED DEADLOCK DETECTED at Site S" + initiatorSite);
        } else {
            System.out.println("\n[RESULT] Verification Complete: No deadlock detected from site S" + initiatorSite);
        }
    }

    /**
     * Recursive probe propagation through the WFG.
     */
    private static void propagateProbe(int initiatorIdx, int currentIdx) {
        if (deadlockDetected) return;

        for (int next = 0; next < numProcesses; next++) {
            if (waitMatrix[currentIdx][next] == 1) {
                // Deadlock Condition: Probe returns to the initiating site
                if (next == initiatorIdx) {
                    System.out.println("    !! Probe returned to Initiator P" + (initiatorIdx + 1) + " !!");
                    System.out.println("    !! Path: (" + (initiatorIdx + 1) + ", " + (currentIdx + 1) + ", " + (next + 1) + ") --------> CYCLE DETECTED");
                    deadlockDetected = true;
                    return;
                }

                System.out.println("    -> Forwarding Probe: (Init:" + (initiatorIdx + 1) + ", Sender:" + (currentIdx + 1) + ", Receiver:" + (next + 1) + ")");
                propagateProbe(initiatorIdx, next);
            }
        }
    }
}
