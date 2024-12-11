
import string
def fonk1(b8, b11):
	b1 = ""
	a1 = 0
	for b2 in b8:
		for j in string.ascii_uppercase:
			if b2 = = j:
				b3 = string.ascii_uppercase.find(b2)
				if b3 + b11[a1] > 25:
					b3 -= 26
				b4 = string.ascii_uppercase[b3+b11[a1]]
				b1 += b4
				a1 += 1
				if a1 >= len(b11):
					a1 = 0
		for k in string.digits:
			if b2 = = k:
				b1 += string.digits[int(b2)]
		for w in string.whitespace:
			if b2 = = w:
				b3 = string.whitespace.find(b2)
				b1 += string.whitespace[b3]
	return b1
def fonk2(b1, b11):
	b5 = []
	for b2 in range(len(b11)):
		b5.append(26 - b11[b2])
	b6 = fonk1(b1, b5)
	return b6
def fonk3():
	print("Welcome to the Polyalphabetic Cipher.\n")
	b7 = "encrypt"
	b8 = "Thanks for taking a look at my polyalphabetic cipher!"
	b9 = string.punctuation + string.whitespace + string.digits
	b10 = str.maketrans({key: None for key in b9})
	b7 = b7.translate(b10)
	b11 = []
	for b2 in b7.upper():
		for j in string.ascii_uppercase:
			if b2 = = j:
				b12 = string.ascii_uppercase.find(b2)
				b11.append(b12 + 1)
	b13 = str.maketrans({key: None for key in string.punctuation})
	b8 = b8.translate(b13)
	print("Shifting the input by this list:", b11)
	print("Message to be encrypted:\n", b8, b14 = "")
	b1 = fonk1(b8.upper(), b11)
	print("\nYour encrypted b8 is:\n", b1, b14 = "")
	b6 = fonk2(b1, b11)
	print("Your decrypted b8 is:\n", b6, b14 = "")
fonk3()