import sys
import os
def ntimes(n, clear) :
	save_file = 0;
	try :
		n = int(n);
	except ValueError :
		print('\n\nYou must introduce an integer\n\n')
		return save_file;
	if (n <= 0) :
		print('\n\nYou must introduce a positive integer\n\n')
		return save_file;
	os.system(clear)
	num = 1;
	next_num = 1;
	print(num)
	for x in range(0,n-1) :
		print(next_num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
	print('\nS    - Save to a file')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s') :
		save_file = 1;
		return save_file;
	else :
		os.system(clear)
		return save_file;
def upton(maxnum, clear) :
	try :
		maxnum = int(maxnum);
	except ValueError :
		print('\n\nYou must introduce an integer\n\n')
		return;
	if (maxnum < 1) :
		print('\n\nYou must insert a value greater or equal to 1\n\n')
	os.system(clear)
	num = 1;
	next_num = 1;
	itera = 0;
	print(num)
	while (next_num<=maxnum) :
		print(next_num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
		itera += 1;
	print('\nS    - Show more information')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s') :
		os.system(clear)
		if (num==maxnum) :
			print("The number", maxnum, "is in the Fibonacci sequence")
		print("Number of iterations:       ", itera)
		print("Your number:                ", maxnum)
		print("Next number in the sequence:", next_num)
		print("Diference to that number:   ", (next_num - maxnum))
		print("\n\n")
		return;
	else :
		print('')
		return;
def file_saver(n) :
	name = str(input('Name of the file: '));
	name = name.replace(" ","")
	name = name + '.txt';
	file = open(name,"w");
	conc = "Number of iterations: " + n + '\n';
	file.write(conc)
	num = 1;
	next_num = 1;
	n = int(n);
	for x in range(0,n) :
		str_num = str(num) + '\n';
		file.write(str_num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
	file.close()
	return name;
def message() :
	import datetime
	hour = datetime.datetime.now().hour;
	if (hour>=20) :
		greeting = 'night!';
	elif (hour>=12) :
		greeting = 'afternoon!';
	elif (hour>=5) :
		greeting = 'day!';
	else :
		greeting = 'night!';
	return greeting;
plat = sys.platform
if (plat == 'linux') :
    clear = 'clear';
elif (plat == 'win32') :
    clear = 'cls';
else : clear = 'clear';
os.system(clear)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\n\n')
repeat = 1;
while (repeat==True) :
	print('1 - Calculate n number of times')
	print('2 - Calculate up to a certain number')
	print('T - Terminate')
	choice = str(input('==> '));
	choice = choice.upper();
	if (choice=='1') :
		n = str(input('Number of times: '));
		save_file = ntimes(n,clear);
		if (save_file==True) :
			name = file_saver(n);
			os.system(clear)
			print('\nFile saved as:', name, '\n\n')
	elif (choice=='2') :
		maxnum = str(input('Calculate to the number: '))
		upton(maxnum, clear);
	elif (choice=='T') :
		import datetime
		greeting = message();
		print('\nThank you, have a good', greeting)
		repeat = 0;
	else :
		os.system(clear)
		print('\nInvalid option\n')