print('''
     P1  P2  P3  P4  P5

P1   0   1   0   0   0
P2   0   0   1   0   0
P3   0   0   0   1   1
P4   0   0   0   0   0
P5   0   0   0   0   0 
''')

a = [   [0, 1, 0, 0, 0], 
        [0, 0, 1, 0, 0], 
        [0, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0] ]

flag = 0

def aman(a, i, k):
   
    end = 5
   
    for x in range(end):
        
        if(a[k][x] == 1):

            if(i == x):
                
                print(f' S{k+1} ==> S{x+1}      ({i+1}, {k+1}, {x+1}) --------> DEADLOCK DETECTED')
                global flag 
                flag = 1 
                break
                
            print(f' S{k+1} ==> S{x+1}      ({i+1}, {k+1}, {x+1})')
            aman(a,i,x)


print("CHANDY-MISRA-HAAS DISTRIBUTED DEADLOCK DETECTION ALGORITHM")
print("__________________________________________________________")
print()

x = 0 
end = 5
i = int(input("Enter Initiator Site No. : "))
j = i - 1

print()
for k in range(end):

    if(a[j][k]==1):
        
        print(f' S{j+1} ==> s{k+1}      ({i}, {j+1}, {k+1})')
        aman(a,j,k)


if(flag == 0): 
    print("\nNO DEADLOCK DETECTED")

print("__________________________________________________________")