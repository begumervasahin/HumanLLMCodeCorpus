from time import time
def fonk1(b10, b11, b12, b13):
	b1 = [[0 for x in range(b13+1)] for x in range(b12+1)]
	for b2 in range(b12+1):
		for b7 in range(b13+1):
			if b2 = = 0 or b7 == 0:
				b1[b2][b7] = 0
			elif b10[b2-1] == b11[b7-1]:
				b1[b2][b7] = b1[b2-1][b7-1] + 1
			else:
				b1[b2][b7] = max(b1[b2-1][b7], b1[b2][b7-1])
	print ("\nL table")
	for b2 in range(b12+1):
		for b7 in range(b13+1):
			print(str(b1[b2][b7])+"\t",b3 = "")
		print("")
	b4 = b1[b12][b13]
	b5 = b4
	b6 = [""] * (b4+1)
	b6[b4] = ""
	b2 = b12
	b7 = b13
	while b2 > 0 and b7 > 0:
		if b10[b2-1] == b11[b7-1]:
			b6[b4-1] = b10[b2-1]
			b2-=1
			b7-=1
			b4-=1
		elif b1[b2-1][b7] >= b1[b2][b7-1]:
			b2-=1
		else:
			b7-=1
	print ("\nLength of LCS is "+str(b5))
	print ("LCS of " + b10 + " and " + b11 + " is " + "".join(b6) )
b8 = []
b9 = []
a1 = 0
a2 = 0
b10 = ["AGGTAB","ABRAC", "BACDB","AYUSH","KAMLESH","SUNIL","BIBASH","ARAJU","MANASI","DEEPESH"]
b11 = ["GXTXAYB","YABBAD","BDCB","SHAHA","MAHES","UNATTI","SHOWIN","ARUNADHA","ANSI","DISH"]
for b2 in range(10):
	b12 = len(b10[b2])
	b13 = len(b11[b2])
	a1 = time()
	fonk1(b10[b2], b11[b2], b12, b13)
	a2 = time()
	b9.insert(b2,b12*b13)
	b8.insert(b2,a2-a1)
print ("\nmn\tTime")
for b2 in range(10):
	print(str(b9[b2])+"\t"+str(b8[b2]))