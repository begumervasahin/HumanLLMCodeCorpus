import sys
import numpy as np
def fonk1(b10):
	a1 = 0
	b1 = np.ones(len(b10))
	for i in b10:
		b1[a1] = ord(i)
		a1 += 1
	b1 = b1.astype(int)
	b2 = np.ones(3*len(b1))
	a1 = 0
	for i in b1:
		if fonk4(i) == 3:
			b2[a1]   = i/100%10
			b2[a1+1] = i/10%10
			b2[a1+2] = i%10
		elif fonk4(i) == 2:
			b2[a1]   = 0
			b2[a1+1] = i/10%10
			b2[a1+2] = i%10
		else:
			b2[a1]   = 0
			b2[a1+1] = 0
			b2[a1+2] = i%10
		a1 += 3
	b2 = b2.astype(int)
	return(b2)
def fonk2(converted_array, b9):
	b3 = len(converted_array)
	b4 = []
	for i in range (0, b3):
		b4.append((converted_array[i] + b9[i])%10)
	return b4
def fonk3(encrypted_array, b9):
	b3 = len(encrypted_array)
	b5 = []
	for i in range(0, b3, 3):
		b6 = ((encrypted_array[i] - b9[i] + 10)%10) * 100
		b6 += ((encrypted_array[i+1] - b9[i+1] + 10)%10) * 10
		b6 += ((encrypted_array[i+2] - b9[i+2] + 10)%10)
		b5.append(b6)
	return b5
def fonk4(b7):
	if(b7 = = 0):
		return 1
	if(b7 < 0):
		b7 *= -1
	a1 = 0
	while b7 != 0:
		b7
		a1 += 1
	return a1
def fonk5():
	if(len(sys.argv) != 4):
		sys.exit("Error: incorrect number of arguments")
	try:
		b8 = open(sys.argv[2])
	except IOError:
		sys.exit("Error: cannot open b8")
	except:
		sys.exit("Error")
	try:
		b9 = open(sys.argv[3])
	except IOError:
		sys.exit("Error: cannot open b9")
	except:
		sys.exit("Error")
	try:
		b10 = b8.read()
		b11 = b9.read()
	except:
		sys.exit("Error: cannot read from files")
	b8.close()
	b9.close()
	b12 = []
	for i in b11:
		if (ord(i) > 47) and (ord(i) < 58):
			b12.append(int(i))
	if(sys.argv[1] == "encrypt"):
		b1 = fonk1(b10)
		if len(b12) < len(b1):
			sys.exit("Error: b9 is shorter than numeric version of b8")
		b13 = fonk2(b1, b12)
		b14 = "encrypted_" + sys.argv[2]
		b15 = ""
		for i in b13:
			b15 += str(i)
		b15 += "\n"
		b16 = open(b14, "w+")
		b16.write(b15)
		b16.close()
	elif(sys.argv[1] == "decrypt"):
		b17 = []
		for i in b10:
			if (ord(i) > 47) and (ord(i) < 58):
				b17.append(int(i))
		if len(b12) < len(b17):
			sys.exit("Error: b9 is shorter than numeric version of b8")
		b5 = fonk3(b17, b12)
		b14 = "decrypted_" + sys.argv[2]
		b15 = ""
		for i in b5:
			b15 += chr(i)
		b16 = open(b14, "w+")
		b16.write(b15)
		b16.close()
	else:
		print("Error: incorrect command, must be \"encrypt\" or \"decrypt\"")
if b18 = = "__main__":
	fonk5()