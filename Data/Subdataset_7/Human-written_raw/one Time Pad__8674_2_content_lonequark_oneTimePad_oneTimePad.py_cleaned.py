import random
import os
b1 = range(32, 127)
def fonk1(string, b1):
	b2 = []
	for char in string:
		b3 = ord(char)
		if b3 in b1:
			b2.append(b3)
	return b2
def fonk2(listIn):
	b4 = ""
	for b3 in listIn:
		b4 = b4 + chr(b3)
	return b4
def fonk3():
	print('Write your message. ASCII characters 32-126 accepted.')
	b5 = raw_input("> ")
	print('Name your ciphertext output b13, excluding .txt extension. For example: message1')
	print('The corresponding b8 will be the name with "b8" appended. For example: message1key')
	b6 = raw_input("> ")
	b7 = fonk1(b5, b1)
	b8 = []
	for b3 in range(0,len(b7)):
		b8.append(random.choice(b1))
	b9 = []
	for i in range(0,len(b7)):
		b10 = ( ( (b7[i] - b1[0]) + (b8[i] - b1[0] ) % len(b1)) + b1[0]
		b9.append(b10)
	b11 = fonk2(b9)
	b8 = fonk2(b8)
	b12 = b6 + ".txt"
	b13 = open(b12,"w")
	b13.write(b11)
	b13.close()
	b14 = b6 + "b8.txt"
	b13 = open(b14,"w")
	b13.write(b8)
	b13.close()
def fonk4():
	print('Enter the name of the ciphertext b13, excluding the extension.\n (For example: message1 for message1.txt)')
	b15 = raw_input('> ')
	print('Enter the name of the b8 b13, excluding the extension.\n (For example: message1key for message1key.txt')
	b14 = raw_input('> ')
	b13 = open(b15 + ".txt","r")
	b11 = b13.read()
	b13.close()
	b13 = open(b14 + ".txt","r")
	b8 = b13.read()
	b13.close()
	b9 = fonk1(b11, b1)
	b16 = fonk1(b8, b1)
	b7 = []
	for i in range(0,len(b9)):
		b17 = ( ( (b9[i] - b1[0]) - (b16[i] - b1[0]) ) % len(b1)) + b1[0]
		b7.append(b17)
	b5 = fonk2(b7)
	b18 = b15 + "b5.txt"
	b13 = open(b18,"w")
	b13.write(b5)
	b13.close()
while True:
	print('Choose a b19:\n (1) Encrypt a message\n (2) Decrypt files\n (3) Quit')
	b19 = int(raw_input('> '))
	if b19 = = 1:
		fonk3()
		print('Encryption successful.\n\n')
	elif b19 = = 2:
		fonk4()
		print('Decryption successful. Remember that the spaces are gone!\n\n')
	else:
		print('Goodbye.')
		break