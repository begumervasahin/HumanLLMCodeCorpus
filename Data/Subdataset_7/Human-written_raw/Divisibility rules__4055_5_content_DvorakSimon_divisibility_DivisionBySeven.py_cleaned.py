
b1 = 1946;
b2 = str(b1);
while len(b2) != 2 and b1 >= 0 and b1 != 0:
	print(b2)
	b3 = b2[0:len(b2)-1]
	b4 = int(b2[len(b2)-1])
	b2 = str(int(b3) - (2*b4))
	b1 = int(b2)
if b1 % b5 = = 0:
	print("Number " + b2 + " is dividible by b5!")