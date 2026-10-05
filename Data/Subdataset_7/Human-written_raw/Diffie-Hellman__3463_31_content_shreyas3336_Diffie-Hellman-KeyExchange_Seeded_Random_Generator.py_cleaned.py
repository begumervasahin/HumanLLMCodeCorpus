import numpy as np
import statistics as stat
import Cipher
def fonk1(b4):
	if (b4>1):
		for b1 in range(b2,b4):
			if(b4%b1 = =0):
				return False
		else:
			return True
	else:
		return False
def fonk2(b4):
	if(b4%b2 = =0):
		return True
	else:
		return False
def fonk3(seeds):
	a1 = 0
	b3 = str(seeds)
	for b1 in b3:
		a1 = a1 + int(b1)*int(b1)*int(b1)
	if(a1 < 1000):
		return a1*len(b3)
	else:
		fonk3(a1)
def fonk4():
	return "Hi there."
def fonk5(seeds):
	np.random.seed(seeds)
	b4 = np.random.rand(seeds).tolist()
	for b1 in range(0,seeds):
		b5 = int((b4[b1]*100000)/37)
		if (fonk1(b5)):
			if(fonk2(b5)):
				b5 = (b5*b5)
			else:
				b5 = (b5*b5)/((seeds-1)*100)
		else:
			if(fonk2(b5)):
				b5 = b5*(100-seeds)/(seeds**b2)
			else:
				b5 = b5*(b5**(0.5))/((seeds-1)**b2)
		b4[b1] = int(b5)
	b6 = Cipher.chiper("Hi there.",round(stat.mean(b4)))
	b7 = Cipher.dechiper(b6,round(stat.mean(b4)))
	print(b6,b7)