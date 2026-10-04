def fonk1(a, eps):
	b1 = (1+a) / 2
	b2 = (b1+a/b1) * 0.5
	b3 = (b2-b1) / b1
	if b3 < 0:
		b3 = -b3
	while b3 > eps:
		b1 = b2
		b2 = (b1+a/b1) * 0.5
		b3 = (b2-b1) / b1
		if b3 < 0:
			b3 = -b3
	b4 = "The square root of the number %s is %s" % (a, b2)
	print(b4)
def fonk2():
	fonk1(5,7)
fonk2()