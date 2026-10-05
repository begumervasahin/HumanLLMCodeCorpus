def fonk1(x):
	for b1 in range(2,x):
		if x % b1 = = 0:
			break
		else:
			if b1+b2 = = x:
				return x
b3 = filter(g,range(9,201))
b4 = [b2]
b5 = len(b3)
for b1 in range(0,b5):
	b6 = b3[b1]*b3[b1]
	if  b6 < 201:
		b4.append(b6)
		for j in range(b1,b5):
			b7 = b3[b1]*b3[j+b2]
			if b7 < 201:
				b4.append(b7)
			else: break
	else: break
print(b4)
b3 = b3 + b4
b3.sort()
print(b3)
print(b5)