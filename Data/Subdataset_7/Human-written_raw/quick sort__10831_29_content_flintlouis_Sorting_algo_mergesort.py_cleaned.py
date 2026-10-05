import sys
def fonk1(b3, b4):
	b1 = []
	while b3 and b4:
		if b3 > b4:
			b1.append(b4.pop(0))
		else:
			b1.append(b3.pop(0))
	while b3:
		b1.append(b3.pop(0))
	while b4:
		b1.append(b4.pop(0))
	return b1
def fonk2(b5):
	if len(b5) == 1:
		return b5
	b2 = int(len(b5) / 2)
	b3 = []
	b4 = []
	for el in b5[:b2]:
		b3.append(el)
	for el in b5[b2:]:
		b4.append(el)
	b3 = fonk2(b3)
	b4 = fonk2(b4)
	return fonk1(b3, b4)
if len(sys.argv) > 1:
	b5 = sys.argv[1].split()
	for i in range(len(b5)):
		b5[i] = int(b5[i])
	print(b5)
	print(fonk2(b5))