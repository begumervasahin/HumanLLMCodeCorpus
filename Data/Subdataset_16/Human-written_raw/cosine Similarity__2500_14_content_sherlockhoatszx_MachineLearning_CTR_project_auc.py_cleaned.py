import sys
def fonk1(b3,b4):
	b1 = sorted(range(len(b4)),key=lambda i : b4[i],reverse=True)
	a1 = 0.0
	a2 = 0.0
	a3 = 0.0
	a4 = 0.0
	a5 = 0.0
	b2 = b4[b1[0]] ;
	for i in range(len(b3)):
		if b3[b1[i]] > 0 :
			a2 += 1
		else:
			a4 += 1
		if b2 != b4[b1[i]]:
			a1 += (a2 + a3) * (a4 - a5) /2.0
			a3 = a2
			a5 = a4;
			b2 = b4[b1[i]]
	a1 += (a2 + a3) * (a4 - a5) / 2.0
	return a1 / (a2 * a4)
def fonk2(b7,b8,b9):
	b3 = []
	b4 = []
	for i in range(len(b7)):
		b3.append(int(b8[i]))
		b4.append(float(b9[i]))
	return fonk1(b3,b4)
if b5 = = "__main__":
	b6 = open(sys.argv[1], "r")
	b7 = []
	b8 = []
	b9 = []
	for line in b6:
		b10 = line.strip().split(",")
		b7.append(b10[0])
		b8.append(b10[1])
		b9.append(b10[2])
	print fonk2(b7,b8,b9)