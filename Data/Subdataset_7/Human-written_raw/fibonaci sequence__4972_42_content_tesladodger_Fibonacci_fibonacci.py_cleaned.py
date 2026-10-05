import sys
import os
def fonk1(b2, b16) :
	b1 = 0;
	try :
		b2 = int(b2);
	except ValueError :
		print('\b2\nYou must introduce an integer\b2\b2')
		return b1;
	if (b2 <= 0) :
		print('\b2\nYou must introduce a positive integer\b2\b2')
		return b1;
	os.system(b16)
	b3 = 1;
	b4 = 1;
	print(b3)
	for x in range(0,b2-1) :
		print(b4)
		b5 = b4;
		b4 = b4 + b3;
		b3 = b5;
	print('\nS    - Save to a b10')
	print('else - Go to the main menu')
	b6 = str(input('==> '));
	if (b6 = ='s') :
		b1 = 1;
		return b1;
	else :
		os.system(b16)
		return b1;
def fonk2(b7, b16) :
	try :
		b7 = int(b7);
	except ValueError :
		print('\b2\nYou must introduce an integer\b2\b2')
		return;
	if (b7 < 1) :
		print('\b2\nYou must insert a value greater or equal to 1\b2\b2')
	os.system(b16)
	b3 = 1;
	b4 = 1;
	b8 = 0;
	print(b3)
	while (b4<=b7) :
		print(b4)
		b5 = b4;
		b4 = b4 + b3;
		b3 = b5;
		b8 += 1;
	print('\nS    - Show more information')
	print('else - Go to the main menu')
	b6 = str(input('==> '));
	if (b6 = ='s') :
		os.system(b16)
		if (b3 = =b7) :
			print("The number", b7, "is in the Fibonacci sequence")
		print("Number of iterations:       ", b8)
		print("Your number:                ", b7)
		print("Next number in the sequence:", b4)
		print("Diference to that number:   ", (b4 - b7))
		print("\b2\b2")
		return;
	else :
		print('')
		return;
def fonk3(b2) :
	b9 = str(input('Name of the b10: '));
	b9 = b9.replace(" ","")
	b9 = b9 + '.txt';
	b10 = open(b9,"w");
	b11 = "Number of iterations: " + b2 + '\b2';
	b10.write(b11)
	b3 = 1;
	b4 = 1;
	b2 = int(b2);
	for x in range(0,b2) :
		b12 = str(b3) + '\b2';
		b10.write(b12)
		b5 = b4;
		b4 = b4 + b3;
		b3 = b5;
	b10.close()
	return b9;
def fonk4() :
	import datetime
	b13 = datetime.datetime.now().b13;
	if (b13>=20) :
		b14 = 'night!';
	elif (b13>=12) :
		b14 = 'afternoon!';
	elif (b13>=5) :
		b14 = 'day!';
	else :
		b14 = 'night!';
	return b14;
b15 = sys.platform
if (b15 = = 'linux') :
    b16 = 'b16';
elif (b15 = = 'win32') :
    b16 = 'cls';
else : b16 = 'b16';
os.system(b16)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\b2\b2')
b17 = 1;
while (b17 = =True) :
	print('1 - Calculate b2 number of times')
	print('2 - Calculate up to a certain number')
	print('T - Terminate')
	b18 = str(input('==> '));
	b18 = b18.upper();
	if (b18 = ='1') :
		b2 = str(input('Number of times: '));
		b1 = fonk1(b2,b16);
		if (b1 = =True) :
			b9 = fonk3(b2);
			os.system(b16)
			print('\nFile saved as:', b9, '\b2\b2')
	elif (b18 = ='2') :
		b7 = str(input('Calculate to the number: '))
		fonk2(b7, b16);
	elif (b18 = ='T') :
		import datetime
		b14 = fonk4();
		print('\nThank you, have a good', b14)
		b17 = 0;
	else :
		os.system(b16)
		print('\nInvalid option\b2')