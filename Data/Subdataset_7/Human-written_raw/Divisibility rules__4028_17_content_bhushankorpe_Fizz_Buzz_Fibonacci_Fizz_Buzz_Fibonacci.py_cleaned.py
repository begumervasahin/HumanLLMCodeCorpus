def fonk1(N):
	b1 = False
	if N > 1:
	 	for x in range(2,N):
	  		if (N % x) == 0:
	  			return b1
	   	b1 = True
	  	return b1
def fonk2(num):
	b2 = []
	if num%b3 = = 0 or num%b4 == 0 or num%b5 == 0 or fonk1(num):
		if num%b3 = = 0:
			b2.append("Buzz")
		if num%b4 = = 0:
			b2.append("Fizz")
		if num%b5 = = 0:
			b2.append("FizzBuzz")
		if fonk1(num):
			b2.append("BuzzFizz")
		for b7 in b2:
			print b7
	else:
		b6 = []
		a1 = 0
		a2 = 1
		for b7 in range(0,num):
			if b7 = = 0:
				b6.append(a1)
			if b7 = = 1:
				b6.append(a2)
			if b7 > 1:
				b8 = a1+a2
				b6.append(b8)
				a1 = a2
				a2 = b8
		print b6
if b9 = = '__main__':
	print "How many fibonacci numbers do you want to see? "
	b10 = input()
	fonk2(b10)