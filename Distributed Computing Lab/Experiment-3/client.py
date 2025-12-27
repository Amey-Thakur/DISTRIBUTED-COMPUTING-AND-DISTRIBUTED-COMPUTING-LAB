# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: January 27, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 3 - Implementation of Remote Method Invocation (RMI) for a Distributed Calculator using Pyro4 (Client-side)

import Pyro4
import datetime
import sys

def main():
    # Capture current client timestamp
    now = datetime.datetime.now()
    print(f"[*] Client session started on: {now.strftime('%d-%m-%Y')} at {now.strftime('%H:%M:%S')}")

    try:
        # 1. Establish a proxy connection to the remote server using the object name
        # The Pyro4 Name Server resolves "RMI.calculator" to the server's URI
        calculator = Pyro4.Proxy("PYRONAME:RMI.calculator")

        # 2. User identification handshake
        name = input("[?] Enter your name: ").strip()
        print(f"\n{calculator.get_usid(name)}\n")

        # 3. Main execution loop
        while True:
            print("-" * 40)
            print(" Distributed Calculator Menu (RMI) ")
            print("-" * 40)
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Square")
            print("6. Square Root")
            print("7. Modulus")
            print("8. Percentage")
            print("9. Exponentiation")
            print("0. Exit")
            print("-" * 40)

            choice = input("[?] Select an operation (0-9): ")

            if choice == '0':
                print("[*] Terminating client session. Goodbye!")
                break

            try:
                if choice in ['1', '2', '3', '4', '7', '8', '9']:
                    a = float(input("Enter first operand (a): "))
                    b = float(input("Enter second operand (b): "))
                elif choice in ['5', '6']:
                    a = float(input("Enter operand (a): "))
                else:
                    print("[!] Invalid selection. Please try again.")
                    continue

                # 4. Invoke remote methods
                if choice == '1':
                    print(f"[Result] {calculator.add(a, b)}")
                elif choice == '2':
                    print(f"[Result] {calculator.subtract(a, b)}")
                elif choice == '3':
                    print(f"[Result] {calculator.multiply(a, b)}")
                elif choice == '4':
                    print(f"[Result] {calculator.division(a, b)}")
                elif choice == '5':
                    print(f"[Result] {calculator.sqr(a)}")
                elif choice == '6':
                    print(f"[Result] {calculator.sqrt(a)}")
                elif choice == '7':
                    print(f"[Result] {calculator.mod(a, b)}")
                elif choice == '8':
                    print(f"[Result] {calculator.per(a, b)}")
                elif choice == '9':
                    print(f"[Result] {calculator.exp(a, b)}")

            except ValueError:
                print("[!] Error: Please enter valid numerical values.")
            except Exception as e:
                print(f"[!] Remote Invocation Error: {e}")

    except Exception as e:
        print(f"[!] Could not connect to RMI Server: {e}")
        print("[!] Ensure the server and Name Server are running.")

if __name__ == "__main__":
    main()
