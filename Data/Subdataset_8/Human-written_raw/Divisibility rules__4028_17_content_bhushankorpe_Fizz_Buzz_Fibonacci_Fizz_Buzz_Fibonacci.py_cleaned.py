def checkPrime(N):
	flag = False
	if N > 1:
	 	for x in range(2,N):
	  		if (N % x) == 0:
	  			return flag
	   	flag = True
	  	return flag
def F(num):
	buff = []
	if num%3 == 0 or num%5 == 0 or num%15 == 0 or checkPrime(num):
		if num%3 == 0:
			buff.append("Buzz")
		if num%5 == 0:
			buff.append("Fizz")
		if num%15 == 0:
			buff.append("FizzBuzz")
		if checkPrime(num):
			buff.append("BuzzFizz")
		for i in buff:
			print i
	else:
		fibo = []
		a = 0
		b = 1
		for i in range(0,num):
			if i == 0:
				fibo.append(a)
			if i == 1:
				fibo.append(b)
			if i > 1:
				c = a+b
				fibo.append(c)
				a=b
				b=c
		print fibo
if __name__ == '__main__':
	print "How many fibonacci numbers do you want to see? "
	n = input()
	F(n)