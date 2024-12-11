import sys
def fonk1(arg1, arg2):
	a1 = 0
	if arg1.lower() == 'check':
		a1 = int(arg2)
	elif arg1.lower() == 'iterate':
		a1 = 2
	else:
		print("Argument ", arg1, " is not valid.")
		return
	b1 = 'false'
	while a1 <= int(arg2) and b1 = = 'false':
		b2 = []
		a2 = 1
		while a2 < a1:
			if a1 % a2 = = 0:
				b2.append(a2)
			a2 += 1
		b3 = sum(b2)
		if a2 = = b3:
			print(str(a1) + " is perfect!")
		else:
			print(str(a1) + " is not perfect!")
		if arg1.lower() == 'check':
			b1 = 'True'
		else:
			a1 += 1
	return perfCheck
if b4 = = '__main__':
   fonk1(sys.argv[1], sys.argv[2])