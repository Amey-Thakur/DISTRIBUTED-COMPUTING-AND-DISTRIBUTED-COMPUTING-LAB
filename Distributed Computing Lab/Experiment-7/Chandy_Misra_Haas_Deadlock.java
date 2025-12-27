/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: February 25, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 7 - Java Implementation of Chandy-Misra-Haas Deadlock Detection (Scenario: Deadlock Detected).
 */

import java.util.Scanner;

public class Chandy_Misra_Haas_Deadlock {
    private static int numProcesses = 5;
    private static int[][] waitMatrix;
    private static boolean deadlockDetected = false;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("--- [CHANDY-MISRA-HAAS DEADLOCK DETECTION: DEADLOCK CASE] ---");

        // Initialize Wait-For-Graph with a cycle (P1->P2->P3->P4->P1)
        waitMatrix = new int[numProcesses][numProcesses];
        waitMatrix[0][1] = 1; // P1 -> P2
        waitMatrix[1][2] = 1; // P2 -> P3
        waitMatrix[2][3] = 1; // P3 -> P4
        waitMatrix[2][4] = 1; // P3 -> P5
        waitMatrix[3][0] = 1; // P4 -> P1 (Cycle)

        displayWFG();

        System.out.print("\n[?] Enter Initiator Process ID (1-5): ");
        int initiator = sc.nextInt();

        if (initiator >= 1 && initiator <= numProcesses) {
            initiateDetection(initiator);
        } else {
            System.out.println("[!] Invalid Process ID.");
        }
        sc.close();
    }

    private static void displayWFG() {
        System.out.println("\nWait-For-Graph Adjacency Matrix:");
        System.out.println("     P1  P2  P3  P4  P5");
        for (int i = 0; i < numProcesses; i++) {
            System.out.print("P" + (i + 1) + "  ");
            for (int j = 0; j < numProcesses; j++) {
                System.out.print(waitMatrix[i][j] + "   ");
            }
            System.out.println();
        }
    }

    private static void initiateDetection(int initiatorSite) {
        int initiatorIdx = initiatorSite - 1;
        System.out.println("\n[*] Initiating probe from P" + initiatorSite + "...");
        for (int target = 0; target < numProcesses; target++) {
            if (waitMatrix[initiatorIdx][target] == 1) {
                System.out.println("    -> Probe: (Init:" + initiatorSite + ", From:" + initiatorSite + ", To:" + (target + 1) + ")");
                propagateProbe(initiatorIdx, target);
            }
        }
        if (!deadlockDetected) System.out.println("\n[RESULT] No Deadlock detected.");
        else System.out.println("\n[RESULT] DISTRIBUTED DEADLOCK DETECTED!");
    }

    private static void propagateProbe(int initiatorIdx, int currentIdx) {
        if (deadlockDetected) return;
        for (int next = 0; next < numProcesses; next++) {
            if (waitMatrix[currentIdx][next] == 1) {
                if (next == initiatorIdx) {
                    System.out.println("    !! Probe returned to Initiator P" + (initiatorIdx + 1) + " !!");
                    System.out.println("    !! Path: (" + (initiatorIdx + 1) + ", " + (currentIdx + 1) + ", " + (next + 1) + ") --------> DEADLOCK");
                    deadlockDetected = true;
                    return;
                }
                System.out.println("    -> Probe: (Init:" + (initiatorIdx + 1) + ", From:" + (currentIdx + 1) + ", To:" + (next + 1) + ")");
                propagateProbe(initiatorIdx, next);
            }
        }
    }
}
