import random
b1 = random.sample(range(1000000),100000)
b2 = sorted(b1)
b3 = random.choice(b2)
b4 = []
b5 = []
b6 = []
b7 = []
from time import time
a1 = 0
def fonk1(theValues,target):
	b8 = len(theValues)
	for i in range(b8):
		if theValues[i]==target:
			return True
	return False
def fonk2(theValues,target):
	b8 = len(theValues)
	for i in range(b8):
		if theValues[i]==target:
			return True
		elif theValues[i]>target:
			return False
	return False
def fonk3(theValues):
	b8 = len(theValues)
	b9 = theValues[0]
	for i in range(1,b8):
		if theValues[i]<b9:
			b9 = theValues[i]
	return b9
def fonk4(theValues,target):
	a2 = 0
	b10 = len(theValues)-1
	while a2<=b10:
		b11 = (b10+a2)/2
		b11 = int(b11)
		if theValues[b11]==target:
			return true
		elif target<theValues[b11]:
			b10 = b11-1
		else:
			a2 = b11+1
	return False
for i in range(10000,100001,10000):
	b12 = time( )
	fonk1(b1[0:i],b3)
	b13 = time( )
	b4.insert(a1,b13-b12)
	a1+=1
print ("\nUnsorted Linear Search times")
for i in range(10):
	print (b4[i])
print
for i in range(10000,100001,10000):
	b12 = time( )
	fonk2(b2[0:i],b3)
	b13 = time( )
	b5.insert(a1,b13-b12)
	a1+=1
print ("\nSorted Linear Search times")
for i in range(10):
	print (b5[i])
print
for i in range(10000,100001,10000):
	b12 = time( )
	fonk3(b1[0:i])
	b13 = time( )
	b6.insert(a1,b13-b12)
	a1+=1
print ("\nFinding Smallest element times")
for i in range(10):
	print (b6[i])
print
for i in range(10000,100001,10000):
	b12 = time( )
	fonk4(b1[0:i],b3)
	b13 = time( )
	b7.insert(a1,b13-b12)
	a1+=1
print ("\nBinary Search times")
for i in range(10):
	print (b7[i])