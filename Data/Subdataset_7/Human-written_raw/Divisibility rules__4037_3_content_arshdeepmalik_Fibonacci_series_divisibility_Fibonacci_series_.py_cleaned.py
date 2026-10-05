import random
a1 = 15
def fonk1(a1):
	if (a1 <= 1):
		return a1
	else:
		b1 = fonk1(a1 - 1) + fonk1(a1-b6)
		return b1
def fonk2(a1):
	b2 = ""
	if (fonk3(a1)):
		return "BuzzFizz"
	if (a1%b3 = = 0):
		b2 += "Fizz"
	if (a1%b4 = = 0):
		b2 += "Buzz"
	if b2 = = "":
		return a1
	return b2
def fonk3(a1):
	b5 = int(a1**0.b4) + 1
	if a1 < b6:
		return False
	if ( (a1 > b6) and (a1%b6 = = 0) ):
		return False
	for b7 in range(b3, b5, b6):
		if a1 % b7 = = 0:
			return False
	return True
if b8 = = "__main__":
	b9 = []
	b10 = []
	for f in range(0, a1):
		b1 = fonk1(f)
		b11 = fonk2(b1)
		b9.append(b1)
		b10.append(b11)
	print "Fibonacci -
	print "Fizzbuzz:"
	for r in range(0, a1):
		print b9[r], "->", b10[r]