/**
 * Name: Amey Mahendra Thakur
 * Course: Distributed Computing Lab (CSL802)
 * Roll No: 50 | Batch: B3
 * Date of Experiment: February 18, 2022
 * Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
 * Description: Experiment 6 - Implementation of Token Ring Mutual Exclusion Algorithm for Distributed Systems.
 */

import java.util.Scanner;
import java.util.InputMismatchException;

public class Token_Ring {
    /**
     * The Token Ring algorithm ensures mutual exclusion by passing a 'token' 
     * around a logical ring of processes. Only the process holding the token 
     * can access the critical section or send data.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("--- [TOKEN RING MUTUAL EXCLUSION SIMULATOR] ---");
        
        try {
            // 1. Initialize the logical ring
            System.out.print("[?] Enter the total number of nodes in the ring: ");
            int numNodes = scanner.nextInt();
            
            System.out.println("[*] Initializing Ring Topology:");
            System.out.print("    Ring: ");
            for (int i = 0; i < numNodes; i++) {
                System.out.print(i + " -> ");
            }
            System.out.println("0 (Circular)");

            int currentTokenPosition = 0; // Initial token holder
            int userChoice = 0;

            // 2. Main execution loop for data transmission
            do {
                System.out.println("\n" + "-".repeat(30));
                System.out.print("[?] Enter Sender Node ID: ");
                int sender = scanner.nextInt();
                
                System.out.print("[?] Enter Receiver Node ID: ");
                int receiver = scanner.nextInt();
                
                System.out.print("[?] Enter Data Packet (Integer): ");
                int data = scanner.nextInt();

                // Validation: Ensure nodes exist
                if (sender >= numNodes || receiver >= numNodes || sender < 0 || receiver < 0) {
                    System.out.println("[!] Error: Invalid Node ID. Please enter IDs between 0 and " + (numNodes - 1));
                    userChoice = 1; // Prompt retry
                    continue;
                }

                // 3. Token Passing Phase: Passing token from current holder to the desired sender
                System.out.print("\n[*] Token Passing sequence: ");
                int tempPosition = currentTokenPosition;
                while (tempPosition != sender) {
                    System.out.print(tempPosition + " -> ");
                    tempPosition = (tempPosition + 1) % numNodes;
                }
                System.out.println(sender + " [TOKEN ACQUIRED]");

                // 4. Data Transmission Phase: Forwarding data through the ring to the receiver
                System.out.println("[*] Node " + sender + " is transmitting data: " + data);
                int forwarder = (sender + 1) % numNodes;
                while (forwarder != receiver) {
                    System.out.println("    -> Data forwarded by Node " + forwarder);
                    forwarder = (forwarder + 1) % numNodes;
                }
                System.out.println("[+] Node " + receiver + " successfully received data: " + data);

                // Update token position to the last sender (or specific protocol logic)
                currentTokenPosition = sender;

                // 5. Continuation Prompt
                boolean validMenuInput = false;
                while (!validMenuInput) {
                    System.out.print("\n[?] Do you want to perform another transmission? (1: Yes, 0: No): ");
                    try {
                        userChoice = scanner.nextInt();
                        if (userChoice == 0 || userChoice == 1) {
                            validMenuInput = true;
                        } else {
                            System.out.println("[!] Please enter 1 for Yes or 0 for No.");
                        }
                    } catch (InputMismatchException e) {
                        System.out.println("[!] Invalid input type. Please enter a number.");
                        scanner.next(); // Clear buffer
                    }
                }

            } while (userChoice == 1);

            System.out.println("\n[*] Terminating simulator. Protocol sequence finalized.");

        } catch (InputMismatchException e) {
            System.out.println("[!] Critical Error: Invalid input type recorded.");
        } finally {
            scanner.close();
        }
    }
}