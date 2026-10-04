import random,sys
def fonk1(inputNum):
	b1 = int(inputNum)
	if(b1 != 0):
		b1 = b1 + fonk1(b1-1);
	return b1
def fonk2(b7,b2,b3):
	if(b3 != 0):
		if(b2 = =b7[b3]):
			return  True
		else:
			fonk2(b7, b2, b3 -1)
		if(b3 = =0):
			return False
def fonk3(tempString, b3):
	if (b3 != -1):
		print(tempString[b3],b4 = " ")
		fonk3(tempString,b3-1)
def fonk4(testStr):
	if(len(testStr) == 1):
		return True
	if(testStr[0] == testStr[len(testStr)-1]):
			fonk4(testStr[0:len(testStr)-2])
			return True
	return False
def fonk5(x, y):
		if(x!=1):
			y += fonk5(x-1,y)
		return y
while True:
	b5 = [sumOfNumbers,isMember,stringReverser,isPalindrome,multiply]
	print ("\n\nWhat do you want to do?\n")
	print ("\t1.  Sum of Numbers\n")
	print ("\t2.  IsMember Array Function\n")
	print ("\t3.  String Reverser\n")
	print ("\t4.  Palindrome Detector\n")
	print ("\t5.  Recursive Multiplication\n")
	print ("\t6.  End the Program\n")
	print ("CHOOSE 1-6:  ")
	b6 = int(input())
	while(b6 < 1 or b6 > 6):
		print('input valid b6 1-6')
		b6 = int(input())
	if b6 = = 6:
		sys.exit()
	if b6 = = 1:
		print('Please enter a number')
		print("\n\nSUM OF NUMBERS\n")
		b1 = int(input())
		print(b5[b6-1](b1))
	elif b6 = =2:
		b7 = []
		for i in range(9):
			b7 = b7 + [random.randint(1,100)]
		print('Is member b7 function')
		print('Please enter an integer')
		b1 = int(input())
		print('Here are the b7 values')
		for i in range(len(b7)):
			print(b7[i])
		if (fonk2(b7,b1,len(b7)-1)==True):
			print('The element was found in the b7')
		else:
			print('the element was not found in the b7')
	elif b6 = =3:
		print('String Reverser')
		print('Enter a string and I will reverse it: ')
		b8 = input()
		fonk3(b8,len(b8)-1)
	elif b6 = = 4:
		print( "\n\nPALINDROME DETECTOR\n")
		print( "Enter a string and I will tell you if it is a palindrome:  ")
		b8 = input()
		b8.upper()
		b8.replace(" ","")
		if (fonk4(b8)==1):
			print('You have entered a palindrome')
		else:
			print('The string you entered is not a palindrome')
	elif b6 = =5:
		print('Recursive Multiplication')
		print('Enter the first integer')
		b9 = int(input())
		print('Enter the second integer')
		b10 = int(input())
		print('The product of the two numbers is:', b4 = " ")
		print(fonk5(b9,b10))