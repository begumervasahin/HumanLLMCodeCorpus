import sys
def fonk1(b18):
	b1 = open(b18, 'r').readlines()
	b2 = []
	b3 = []
	for i in range(len(b1)):
		for j in range(len(b1)):
			b3.append((b1[i].split(" ")[j]).replace('\n', ''))
		b2.append(b3)
		b3 = []
	return b2
def fonk2(b2):
	b4 = []
	b3 = []
	for i in range(len(b2)):
		for j in range(len(b2)):
			if(b2[i][j] != "1024"):
				b3.append(str(j) + " "+ b2[i][j])
		b4.append(b3)
		b3 = []
	return b4
def fonk3(b4, b14, b19):
	b5 = [0] * len(b4)
	b6 = []
	b3 = []
	b7 = [0] * len(b4)
	b3.append ('- ' + b14 + ' 0')
	b6.append(b3)
	b5[int(b14)] = 1
	b8 = int(b14)
	a1 = 0
	b9 = ""
	a2 = 0
	b10 = ""
        b11 = ""
	while b5[int(b19)] != 1:
		b10 = (b4[b8][0]).split(" ")[0]
		b11 = int((b4[b8][0]).split(" ")[1]) + int(a1)
		for i in range(1,len(b4[b8])):
			if(b5[int(b10)] != 1):
				if(int(b10) == int(b19) ):
					b9 = b8
				else:
					b12 = (b4[b8][i]).split(" ")[0]
					if(b5[int(b12)] != 1):
						b13 = int((b4[b8][i]).split(" ")[1]) + int(a1)
						if(b13 < b11) :
							b10 = b12
				                	b11 = b13
							b9 = b8
			elif(b9 = = int(b14) or b5[int(b10 )] == 1):
				b10 = (b4[b8][i]).split(" ")[0]
				b11 = int((b4[b8][i]).split(" ")[1]) + int(a1)
		if(b9 = = ""):
			b9 = b8
		a2 = (b6[b7[int(b9)]][0]).split(" ")[2]
		if(len(b6) > 2 and b9 != int(b14) and int(b10) != int(b19)):
			for i in range(len(b4[int(b9)])):
				b12 = (b4[b9][i]).split(" ")[0]
				if(b5[int(b12)] != 1):
					b13 = int((b4[b9][i]).split(" ")[1]) + int(a2)
					if(b13 < b11):
						b10 = (b4[b9][i]).split(" ")[0]
				                b11 = b13
		b3 = []
		b3.append(str(b9) + ' ' + str(b10) + ' ' + str(b11))
		b6.append(b3)
		b5[int(b10)] = 1
		b7[int(b10)] = len(b6) -1
		b8 = int(b10)
		a1 = int(b11)
	return b6
def fonk4(b6,b14, b19):
	if(b14 = = b19):
		print(b14)
	else:
		b15 = ""
		b15 += (b6[(len(b6)-1)][0]).split(" ")[1]
		b15 += " "
		b16 = (b6[(len(b6)-1)][0]).split(" ")[0]
		while int(b16) != int(b14):
			for i in range(1,len(b6)-1):
				if((b6[i][0]).split(" ")[1] == b16):
					b15 += (b6[i][0]).split(" ")[1]
					b15 += " "
					b16 = (b6[i][0]).split(" ")[0]
		b15 += (b6[0][0]).split(" ")[1]
		print(b15[::-1])
b17 = sys.argv[1:]
b18 = b17[0]
b14 = b17[1]
b19 = b17[2]
b4 = fonk2(fonk1(b18))
fonk4(fonk3(b4,b14,b19),b14,b19)