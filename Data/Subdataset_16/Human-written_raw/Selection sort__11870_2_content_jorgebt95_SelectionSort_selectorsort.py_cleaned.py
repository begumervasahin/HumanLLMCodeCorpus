def fonk1(b3):
	for i in range(5):
		b1 = i
		for j in range(i,6):
			if b3[j] < b3[b1]:
				b1 = j
		b2 = b3[i]
		b3[i] = b3[b1]
		b3[b1] = b2
b3 = [5,6,4,3,7,8]
fonk1(b3)
def fonk2():
 assert b3 = = [3,4,4,6,7,8]