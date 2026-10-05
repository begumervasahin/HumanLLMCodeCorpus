def isDivisibleByThree(n) :
	odd_counter = even_counter = 0
	if n == 0 :
		return 1
	elif n == 1 :
		return 0
	while n :
		if n & 1 == 1 :
			odd_counter += 1
		n = n >> 1
		if n & 1 == 1 :
			even_counter += 1
		n = n >> 1
	return isDivisibleByThree(abs(odd_counter - even_counter) )
print "Enter an integer : "
n = input()
if isDivisibleByThree(abs(n) ) :
	print "%d is divisible by 3." % n
else :
	print "%d is not divisible by 3." % n