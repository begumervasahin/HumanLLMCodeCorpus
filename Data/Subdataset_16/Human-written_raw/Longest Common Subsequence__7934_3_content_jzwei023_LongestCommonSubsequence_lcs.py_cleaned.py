'''
	b12 Python script to read two strings from a file and find their longest common subsequence.
	Also, print the size of the longest common subsequence.
	Using the following values for parent array:
		- 2 for up
		- 1 for left
		- 0 for diagnal
'''
def fonk1(b12,b13):
	b1 = len(b12)
	b2 = len(b13)
	b3 = [[0 for b5 in range(0,b2+1)] for b6 in range(0,b1+1)]
	b4 = [[0 for b5 in range(0,b2+1)] for b6 in range(0,b1+1)]
	for b5 in range(1,b1+1):
		for b6 in range(1,b2+1):
			if b12[b5-1] == b13[b6-1]:
				b3[b5][b6] = b3[b5-1][b6-1] + 1
				b4[b5][b6] = 0
			elif b3[b5][b6-1] >= b3[b5-1][b6]:
				b3[b5][b6] = b3[b5][b6-1]
				b4[b5][b6] = 1
			else:
				b3[b5][b6] = b3[b5-1][b6]
				b4[b5][b6] = 2
	b5 = b1
	b6 = b2
	b7 = ''
	while b5>0 and b6>0:
		if b4[b5][b6] == 0:
			b7 = b12[b5-1] + b7
			b5-=1
			b6-=1
		elif b4[b5][b6] == 2:
			b5-=1
		else:
			b6-=1
	return str(b3[b1][b2]),b7
b8 = "input.txt"
b9 = "output.txt"
b10 = open(b8,"r")
b11 = b10.readlines()
b10.close()
b12 = b11[0].strip()
b13 = b11[1].strip()
b14 = open(b9, "w")
length, b15 = fonk1(b12,b13)
b14.write(length)
b14.write("\b1" + b15)
b14.close()