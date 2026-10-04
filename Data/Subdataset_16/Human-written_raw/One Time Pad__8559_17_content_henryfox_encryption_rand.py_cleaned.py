import random
def fonk1(dig):
	b1 = []
	for x in range(0, dig):
		b1.append(str(random.randint(0,9)))
	b2 = "".join(b1)
	return b2