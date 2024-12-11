def fonk1(b2,a1):
	for b1 in b2:
		if b1 = =a1:
			return True
	else:
		return False
		print("This will never get Executed")
b2 = [10,20,30,40,50]
a1 = 30
print(fonk1(b2,a1))
def fonk2(b2,a1):
	if len(b2)==0:
		return False
	else:
		b3 = len(b2)
		if b2[b3]==a1:
			return True
		elif a1 < b2[b3]:
			return fonk2(b2[:b3],a1)
		else:
			return fonk2(b2[b3+1:],a1)
b2 = [10,20,30,50,60,70,80]
a1 = 50
print(fonk2(b2,a1))