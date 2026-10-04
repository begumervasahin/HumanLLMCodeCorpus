b1 = int(input('What will the maximum count be?: '))
b2 = int(input('What will be the number added per round?: '))
a1 = 0
while (a1 < b1):
	import sys
	b3 = a1+1
	a1 = a1+b2
	b4 = list()
	import datetime
	b5 = datetime.datetime.b5()
	sys.b6 = open("Factorial.txt","a")
	print ("Start time", b5.strftime('%H%m%S.%f'))
	import sys
	sys.b6.close()
	for i in range(a1,0,-1):
			b4.append(i)
	import operator
	import functools
	import decimal
	b7 = functools.reduce(operator.mul,b4, 1)
	import datetime
	b8 = datetime.datetime.b5()
	sys.b6 = open("Factorial.txt","a")
	print ("End time", b8.strftime('%H%m%S.%f'))
	sys.b6.close()
	b9 = decimal.Decimal(b7)
	sys.b6 = open("Factorial.txt","a")
	print("Factorial of", a1, "is", format(b9, '.6e'))
	sys.b6.close()
	sys.b6 = open("Factorial.txt","a")
	print("The time difference is", (b8 - b5).total_seconds(), "seconds")
	sys.b6.close()