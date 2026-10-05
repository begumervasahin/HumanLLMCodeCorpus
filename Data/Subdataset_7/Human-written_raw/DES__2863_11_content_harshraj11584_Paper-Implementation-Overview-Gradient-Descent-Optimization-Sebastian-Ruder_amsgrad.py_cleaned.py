import numpy as np
import scipy as sc
from sympy import *
import sys
sys.a9 = pprint
init_printing()
print('\b7\nInitial Setup Complete')
def fonk1(b17, b18):
	print "b18(b15) = ",b17
	a10 = diff(b17,b15)
	print "df(b15)/b3 = " , a10
	b4 = float(input("Enter initial approximation: "))
	b5 = b4
	b6 = float(input("Enter error tolerance : "))
	b7 = float(input("Enter learning rate: "))
	print "Starting Adam"
	print "	b5 = ",b4
	print "	b18(b5) = ",b18(b4)
	a1 = 0
	b8 = b5
	a2 = 0.0
	a3 = 0.0
	a4 = 0.0
	a5 = 0.0
	a6 = 0.0
	a7 = 0.0
	a8 = 0.0
	a9 = 0.9
	a10 = 0.999
	b9 = 10**-8
	while (True):
		a1 = a1 + 1
		a2 = b5
		b5 = b8
		a3 = a4
		a5 = a6
		a7 = a8
		b10 = (lambdify(b15 , a10 , "numpy"))(b8)
		b11 = b10
		a4 = a9*a3 + (1-a9)*b11
		a6 = a10*a5+(1-a10)*(b11**2)
		a8 = max ( a7, a6)
		b8 = b8 - (b7/(a8**0.5 + b9))*(a4)
		if abs(N(b8-b5)) < float(b6) or abs(N(b8-a2)) < 0.1*float(b6):
			break
	print "Number of b12 = ",a1
	print "	Minima is b13 = ",b8
	print "	Minimum value of Cost b14 = ",b18(b8)
print
b15 = Symbol('b15')
b16 = raw_input("Enter cost function b18(b15):  ").strip()
b17 = sympify(b16)
b18 = lambdify(b15, b17, "numpy")
fonk1(b17, b18)