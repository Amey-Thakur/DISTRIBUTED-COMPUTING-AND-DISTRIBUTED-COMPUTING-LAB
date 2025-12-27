import threading
import time

r1 = 0

print("We assume two processers")

l1 = int(input("Enter the limit of processor one: "))
l2 = int(input("Enter the limit of processor two: "))
n = int(input("Enter the number of processes: "))

n = n + r1


def run1():
    
    print()
    print(f"Processor 1 (limit = {l1}):")

    if(n == 0):
        print("No processes are remaining")
    
    else:
        
        if(l1 > n):
            print("Underloaded processor")
            print(f"{n} processes are executed")
        
        elif (l1 == n):
            print("Normal processor")
            print(f"{n} processes are executed")
            print("No need to forward any process to next processor.")

        elif(l1 < n):
            print("Overloaded processor")
            print(f"{n} processes are executed")
            rem = n - l1
            print(f"{rem} will be forwarded to next processor")

    global r1 
    r1 = rem


def run2():
    
    time.sleep(5)

    print()
    print(f"Processor 2 (limit = {l2}):")

    if(r1 == 0):
        print("No processes are remaining")
    
    else:
        
        if(l2 > r1):
            print("Underloaded processor")
            print(f"{r1} processes are executed")
        
        elif (l2 == r1):
            print("Normal processor")
            print(f"{r1} processes are executed")
            print("No need to forward any process to next processor.")

        elif(l1 < r1):
            print("Overloaded processor")
            print(f"{n} processes are executed")
            rem = n - (l1 -l2)
            print(f"{rem} will be forwarded to next processor")


def run():
    
    t1 = threading.Thread(run1())
    t2 = threading.Thread(run2())

    t1.start()
    t2.start()


run()