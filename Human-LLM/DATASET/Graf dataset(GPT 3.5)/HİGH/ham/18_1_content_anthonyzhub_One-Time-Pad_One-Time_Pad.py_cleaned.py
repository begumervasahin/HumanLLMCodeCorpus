from random import randint
b1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\;:"[]{}()_-!@
def fonk1(b10, b11):
	for b13 in range(b10):
		with open("otp" + str(b13) + ".txt", "w") as f:
			for i in range (b11):
				f.write(str(randint(0, 81)) + "\n")
def fonk2(b12):
	with open(b12, "r") as f:
		b2 = f.read().splitlines()
	return b2
def fonk3():
	b3 = input('Enter your message: ')
	return b3
def fonk4(b12):
	with open(b12, 'r') as f:
		b2 = f.read()
	return b2
def fonk5(b12, data):
	with open(b12, 'w') as f:
		f.write(data)
def fonk6(b6, b13):
	b4 = ''
	for position, character in enumerate(b6):
		if character not in b1:
			b4 += character
		else:
			b5 = (b1.index(character) + int(b13[position])) % 81
			b4 += b1[b5]
	return b4
def fonk7(b4, b13):
	b6 = ''
	for position, character in enumerate (b4):
		if character not in b1:
			b6 += character
		else:
			b7 = (b1.index(character) - int(b13[position])) % 81
			b6 += b1[b7]
	return b6
def fonk8():
	b8 = ['1', '2', '3', '4']
	b9 = '0'
	while True:
		print('1. Generate one-time pads')
		print('2. Encrypt a message')
		print('3. Decrypt a message')
		print('4. Quit program')
		b9 = input('Enter number: ')
		if b9 = = '1':
			b10 = int(input('How many OTP should be generated? '))
			b11 = int(input('What will be the maximum message b11? '))
			fonk1(b10, b11)
		elif b9 = = '2':
			b12 = input('Enter b12 of the OTP you want to use: ')
			b13 = fonk2(b12)
			b6 = fonk3()
			b4 = fonk6(b6, b13)
			b12 = input('Enter name of b5 file: ')
			fonk5(b12, b4)
		elif b9 = = '3':
			b12 = input('Enter b12 of the OTP you want to use: ')
			b13 = fonk2(b12)
			b12 = input('Type the name of the file to be b7: ')
			b4 = fonk4(b12)
			b6 = fonk7(b4, b13)
			print('Decrypted Message: \n' + b6)
		elif b9 = = '4':
			exit()
		b9 = '0'
fonk8()