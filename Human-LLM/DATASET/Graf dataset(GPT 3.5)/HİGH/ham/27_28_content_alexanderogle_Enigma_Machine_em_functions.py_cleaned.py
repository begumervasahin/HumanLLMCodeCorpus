def fonk1(str, n):
	b1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	print ""
	print str
	b2 = b1.index(n)
	b3 = []
	for i in range(len(b1[b2:len(b1)])):
		b3.append(b1[b2+i])
	for i in range(0, b2):
		b3.append(b1[i])
	b4 = []
	for i in str:
		if i.isalpha():
			b4.append(b3[b1.index(i)])
		else:
			b4.append(i)
	b5 = ''
	for i in range(len(b4)):
		b5 = b5 + b4[i]
	b4 = b5
	print ""
	print "A b6 = %s" % (b2)
	print "<",
	for letter in b3:
			print letter,
	print ">"
	return b4
def fonk2(str, n):
	b1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	print ""
	print str
	b2 = b1.index(n)
	b3 = []
	for i in range(len(b1[b2:len(b1)])):
		b3.append(b1[b2+i])
	for i in range(0, b2):
		b3.append(b1[i])
	b7 = []
	for i in str:
		if i.isalpha():
			b7.append(b1[b3.index(i)])
		else:
			b7.append(i)
	b8 = ''
	for i in range(len(b7)):
		b8 = b8 + b7[i]
	b7 = b8
	print ""
	print "A b6 = %s" % (b2)
	print "<",
	for letter in b3:
			print letter,
	print ">"
	return b7
def fonk3(str):
	for i in str:
		print i,
def fonk4(x):
	b9 = []
	for i in range(x):
		 b9.append(0)
	return b9
def fonk5(str):
	if len(str) != 1:
		print "That's not a letter!"
	elif str.isalpha():
		b1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		b10 = b1.index(str)
		return b10