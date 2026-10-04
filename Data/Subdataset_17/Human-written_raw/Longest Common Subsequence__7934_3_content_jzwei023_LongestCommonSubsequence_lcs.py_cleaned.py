'''
	A Python script to read two strings from a file and find their longest common subsequence.
	Also, print the size of the longest common subsequence.
	Using the following values for parent array:
		- 2 for up
		- 1 for left
		- 0 for diagnal
'''
def calculate_LCS(A,B):
	n = len(A)
	m = len(B)
	opt = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
	pi = [[0 for i in range(0,m+1)] for j in range(0,n+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if A[i-1] == B[j-1]:
				opt[i][j] = opt[i-1][j-1] + 1
				pi[i][j] = 0
			elif opt[i][j-1] >= opt[i-1][j]:
				opt[i][j] = opt[i][j-1]
				pi[i][j] = 1
			else:
				opt[i][j] = opt[i-1][j]
				pi[i][j] = 2
	i = n
	j = m
	S = ''
	while i>0 and j>0:
		if pi[i][j] == 0:
			S = A[i-1] + S
			i-=1
			j-=1
		elif pi[i][j] == 2:
			i-=1
		else:
			j-=1
	return str(opt[n][m]),S
input_file = "input.txt"
output_file = "output.txt"
file_in = open(input_file,"r")
lines = file_in.readlines()
file_in.close()
A = lines[0].strip()
B = lines[1].strip()
file_out = open(output_file, "w")
length, sequence = calculate_LCS(A,B)
file_out.write(length)
file_out.write("\n" + sequence)
file_out.close()