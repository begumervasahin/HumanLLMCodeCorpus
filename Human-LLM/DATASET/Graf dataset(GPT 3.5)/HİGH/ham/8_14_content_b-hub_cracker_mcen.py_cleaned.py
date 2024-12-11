import sys
b1 = []
b2 = ['$']
for n in range(32, 127):
	b3 = chr(n)
	if b3 not in b2:
		b1.append(chr(n))
def fonk1(c1, c2):
	return b1[(b1.index(c1) - b1.index(c2)) % len(b1)]
def fonk2(cChar, pChar):
	return fonk1(cChar, pChar)
def fonk3(b7, cipher):
	b4 = ""
	a1 = 0
	while a1 < len(b7):
		b4 += fonk1(cipher[a1], b7[a1])
		a1 += 1
	return b4
b5 = sys.argv[1]
if b5 = = "d":
	print ("Decryption Mode, to exit press: ctrl + c")
	b6 = raw_input("Enter the b6:")
	print (b6)
	b7 = raw_input("Now enter the b7:")
	print (b7)
	print ("Plaintext: " + fonk3(b7, b6))
elif b5 = = "e":
	print ("Encryption Mode, to exit press: ctrl + c")
	b4 = raw_input("Enter the b4:")
	print (b4)
	b6 = raw_input("Now enter the b6:")
	print (b6)
	if len(b4) <= len(b6):
		a1 = 0
		b7 = ""
		while a1 < len(b4):
			b7 += fonk2(b6[a1], b4[a1])
			a1 += 1
		b8 = chr(175)
		b9 = chr(174)
		print (b8 + "KEY" + b9 + ", make sure you copy everything between the " + b8 + " and the " + b9)
		print (b8 + b7 + b9)
	else:
		print ("The length of b6 must be >= to b4 to encrypt all of it")
else:
	print ("Please enter either the character 'e' or 'd' for either encryption or decryption")
	exit(-1)