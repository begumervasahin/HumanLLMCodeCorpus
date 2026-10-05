import numpy as np
import statistics as stat
import Cipher
def check_prime(k):
	if (k>1):
		for i in range(2,k):
			if(k%i==0):
				return False
		else:
			return True
	else:
		return False
def check_even(k):
	if(k%2==0):
		return True
	else:
		return False
def reduce(seeds):
	new_num = 0
	num = str(seeds)
	for i in num:
		new_num = new_num + int(i)*int(i)*int(i)
	if(new_num < 1000):
		return new_num*len(num)
	else:
		reduce(new_num)
def text():
	return "Hi there."
def random_generator(seeds):
	np.random.seed(seeds)
	k = np.random.rand(seeds).tolist()
	for i in range(0,seeds):
		temp = int((k[i]*100000)/37)
		if (check_prime(temp)):
			if(check_even(temp)):
				temp = (temp*temp)
			else:
				temp = (temp*temp)/((seeds-1)*100)
		else:
			if(check_even(temp)):
				temp = temp*(100-seeds)/(seeds**2)
			else:
				temp = temp*(temp**(0.5))/((seeds-1)**2)
		k[i] = int(temp)
	cyp = Cipher.chiper("Hi there.",round(stat.mean(k)))
	dcyp = Cipher.dechiper(cyp,round(stat.mean(k)))
	print(cyp,dcyp)