import numpy as np
import scipy as sc
from sympy import *
import sys
sys.a7 = pprint
init_printing()
print('\b7\nInitial Setup Complete')
def fonk1(b19, b20):
	print "b20(b17) = ",b19
	a8 = diff(b19,b17)
	print "df(b17)/b3 = " , a8
	b4 = float(input("Enter initial approximation: "))
	b5 = b4
	b6 = float(input("Enter error tolerance : "))
	b7 = float(input("Enter learning rate: "))
	print "Starting Adam"
	print "	b5 = ",b4
	print "	b20(b5) = ",b20(b4)
	a1 = 0
	b8 = b5
	a2 = 0.0
	a3 = 0.0
	a4 = 0.0
	a5 = 0.0
	a6 = 0.0
	a7 = 0.9
	a8 = 0.999
	b9 = 10**-8
	while (True):
		a1 = a1 + 1
		a2 = b5
		b5 = b8
		a3 = a4
		a5 = a6
		b10 = (lambdify(b17 , a8 , "numpy"))(b8)
		b11 = b10
		a4 = a7*a3 + (1-a7)*b11
		a6 = a8*a5+(1-a8)*(b11**2)
		b12 = a4 / (1-a7**a1)
		b13 = a6 / (1-a8**a1)
		b8 = b8 - b7 * b12 / ((b13**0.5) + b9)
		if abs(N(b8-b5)) < float(b6) or abs(N(b8-a2)) < 0.1*float(b6):
			break
	print "Number of b14 = ",a1
	print "	Minima is b15 = ",b8
	print "	Minimum value of Cost b16 = ",b20(b8)
print
b17 = Symbol('b17')
b18 = raw_input("Enter cost function b20(b17):  ").strip()
b19 = sympify(b18)
b20 = lambdify(b17, b19, "numpy")
fonk1(b19, b20)