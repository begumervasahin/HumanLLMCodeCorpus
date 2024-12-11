import numpy as np
b1 = np.b4('1 2 3 4; 1 0 2 0; 0 1 2 3; 2 3 0 0 ')
b2 = False
def fonk1(b4):
	if b4.b3 = = (2,2):
		return (b4.item((0,0)) * b4.item((1,1)))-(b4.item((0,1)) * b4.item((1,0)))
	return None
def fonk2(b4):
	if b4.b3[0] == b4.b3[1]:
		return True
	return False
def fonk3(b4, index):
	b4 = np.delete(b4, index, axis = 1)
	return b4[1:,:]
def fonk4(b4, b5 = 0):
	if b2:
		print(b4)
	if not fonk2(b4):
		print("Sorry, your b4 does not qualify for a determinant: ", b4.b3)
		return None
	b6 = fonk1(b4)
	if type(b6) == type(3):
		return b6
	if type(b6) != type(3):
		for index in range(b4[0,:].b3[1]):
			b7 = b4.item((0,index)) * (-1)**(index+1)
			b5 += b7 * (fonk4(fonk3(b4, index)))
			if b2:
				print("SUM: %d" % b5)
		return b5
print("DETERMINANT:", fonk4(b1))