# Name: Amey Mahendra Thakur
# Course: Distributed Computing Lab (CSL802)
# Roll No: 50 | Batch: B3
# Date of Experiment: January 27, 2022
# Repository: https://github.com/Amey-Thakur/DISTRIBUTED-COMPUTING-AND-DISTRIBUTED-COMPUTING-LAB
# Description: Experiment 3 - Implementation of Remote Method Invocation (RMI) for a Distributed Calculator using Pyro4 (Server-side)

import Pyro4
import random
import datetime
import math
import sys

@Pyro4.expose
class RemoteCalculator(object):
    """
    The RemoteCalculator class contains methods that will be invoked remotely 
    by the client using the Pyro4 framework.
    """
    
    def get_usid(self, name):
        """Generates a unique session ID for the user."""
        session_id = random.randint(1000, 9999)
        return f"Hello, {name}.\nYour authenticated User Session ID is: {session_id}"

    def add(self, a, b):
        """Performs addition."""
        return f"{a} + {b} = {a + b}"

    def subtract(self, a, b):
        """Performs subtraction."""
        return f"{a} - {b} = {a - b}"

    def multiply(self, a, b):
        """Performs multiplication."""
        return f"{a} * {b} = {a * b}"

    def division(self, a, b):
        """Performs division with error handling for zero."""
        if b == 0:
            return "Error: Division by zero is undefined."
        return f"{a} / {b} = {a / b}"

    def sqr(self, a):
        """Calculates the square of a number."""
        return f"{a} ^ 2 = {a ** 2}"

    def sqrt(self, a):
        """Calculates the square root of a number."""
        if a < 0:
            return "Error: Cannot calculate square root of a negative number in real domain."
        return f"sqrt({a}) = {math.sqrt(a)}"

    def mod(self, a, b):
        """Calculates the remainder of division."""
        return f"{a} % {b} = {a % b}"

    def per(self, a, b):
        """Calculates the percentage of a relative to b."""
        if b == 0:
            return "Error: Division by zero in percentage calculation."
        return f"( {a} / {b} ) * 100 = {(a / b) * 100}%"

    def exp(self, a, b):
        """Performs exponentiation (a to the power of b)."""
        return f"{a} ** {b} = {a ** b}"

def main():
    # Capture current server timestamp
    now = datetime.datetime.now()
    print(f"[*] Server initialized on: {now.strftime('%d-%m-%Y')} at {now.strftime('%H:%M:%S')}")

    try:
        # 1. Initialize the Pyro4 Daemon
        daemon = Pyro4.Daemon()
        
        # 2. Locate the Pyro4 Name Server
        # Ensure 'pyro4-ns' is running in the background for this to work
        ns = Pyro4.locateNS()
        
        # 3. Register the server class with the daemon
        uri = daemon.register(RemoteCalculator)
        
        # 4. Register the object name with the Name Server
        ns.register("RMI.calculator", uri)
        
        print("[*] RMI Calculator Server is now active and registered.")
        print("[*] Waiting for remote procedure calls...")
        
        # 5. Start the request loop
        daemon.requestLoop()
        
    except Exception as e:
        print(f"[!] Server Error: {e}")
        print("[!] Ensure the Pyro4 Name Server (pyro4-ns) is operational.")

if __name__ == "__main__":
    main()
