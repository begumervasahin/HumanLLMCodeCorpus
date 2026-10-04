def fonk1(b2) :
	b1 = even_counter = 0
	if b2 = = 0 :
		return b3
	elif b2 = = b3 :
		return 0
	while b2 :
		if b2 & b3 = = b3 :
			b1 += b3
		b2 = b2 >> b3
		if b2 & b3 = = b3 :
			even_counter += b3
		b2 = b2 >> b3
	return fonk1(abs(b1 - even_counter) )
print "Enter an integer : "
b2 = input()
if fonk1(abs(b2) ) :
	print "%d is divisible by 3." % b2
else :
	print "%d is not divisible by 3." % b2