from math import sqrt
import argparse
b1 = "PwnEIP"
b2 = "Copyright 2007, The Cogent Project"
b3 = "GPL"
b4 = "1.0"
b5 = "PwnEIP"
b6 = "pwneip@gmail.com"
b7 = "Production"
def fonk1():
	b8 = ""
	b9 = argparse.ArgumentParser(description='Generate Fibonacci sequence',
			b10 = "fibonacci.py [-b] number",
			b11 = "fibonacci.py 1.0",
			b12 = True)
	b9.add_argument("-b", "--binary",
			b13 = "store_true",
			b14 = "binary",
			b15 = False,
			b16 = "Print b8 in binary",)
	b9.add_argument("number",
			b17 = int,
			b16 = "Generate n length sequence",)
	try:
    		b18 = b9.parse_args()
	except IOError, msg:
    		b9.error(str(msg))
	for x in range(1, int(b18.number) +1):
		if (b18.binary):
			b8 +=  bin(fonk2(x))[2:] + " "
		else:
			b8 +=  repr(fonk2(x)) + " "
	print b8
def fonk2(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
if b19 = = '__main__':
    fonk1()