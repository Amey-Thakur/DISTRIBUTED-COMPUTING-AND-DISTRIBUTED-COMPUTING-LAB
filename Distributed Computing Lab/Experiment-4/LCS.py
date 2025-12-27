# Python program to illustrate the Lamport's
# Logical Clock

# Function to find the maximum timestamp
# between 2 events
def max1(a, b) :

	# Return the greatest of th two
	if a > b :
		return a
	else :
		return b

# Function to display the logical timestamp
def display(e1, e2, p1, p2) :
	print()
	print("The time stamps of events in P1:")
	for i in range(0, e1) :
		print(p1[i], end = " ")
	
	print()
	print("The time stamps of events in P2:")
	
	# Print the array p2[]
	for i in range(0, e2) :
		print(p2[i], end = " ")

# Function to find the timestamp of events
def lamportLogicalClock(e1, e2, m) :
	p1 = [0]*e1
	p2 = [0]*e2

	# Initialize p1[] and p2[]
	for i in range (0, e1) :
		p1[i] = i + 1

	for i in range(0, e2) :
		p2[i] = i + 1
	
	for i in range(0, e2) :
		print(end = '\t')
		print("e2", end = "")
		print(i + 1, end = "")
	
	for i in range(0, e1) :
		print()
		print("e1", end = "")
		print(i + 1, end = "\t")

		for j in range(0, e2) :
			print(m[i][j], end = "\t")
		
	for i in range(0, e1) :

		for j in range(0, e2) :
		
			# Change the timestamp if the
			# message is sent
			if(m[i][j] == 1) :
				p2[j] = max1(p2[j], p1[i] + 1)
				for i in range(j + 1, e2) :
					p2[k] = p2[k - 1] + 1

			# Change the timestamp if the
			# message is received
			if(m[i][j] == -1) :
				p1[i] = max1(p1[i], p2[j] + 1)
				for k in range(i + 1, e1) :
					p1[k] = p1[k - 1] + 1

	# Function Call
	display(e1, e2, p1, p2)

# Driver Code

if __name__ == "__main__" :
	e1 = 5
	e2 = 3
	m = [[0]*3 for i in range(0,5)]
	
	# dep[i][j] = 1, if message is sent
	# from ei to ej
	# dep[i][j] = -1, if message is received
	# by ei from ej
	# dep[i][j] = 0, otherwise

	m[0][0] = 0
	m[0][1] = 0
	m[0][2] = 0
	m[1][0] = 0
	m[1][1] = 0
	m[1][2] = 1
	m[2][0] = 0
	m[2][1] = 0
	m[2][2] = 0
	m[3][0] = 0
	m[3][1] = 0
	m[3][2] = 0
	m[4][0] = 0
	m[4][1] = -1
	m[4][2] = 0
	
	# Function Call
	lamportLogicalClock(e1, e2, m)

	# This code is contributed by rakeshsahni
