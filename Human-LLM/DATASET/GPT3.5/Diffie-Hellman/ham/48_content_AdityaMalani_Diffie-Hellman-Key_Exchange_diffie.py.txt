import random
import numpy as np
def isPrime(num):
	for i in range(2,int(num/2)+1):
		if num%i == 0:
			return 0
	return 1
def isUnique(a):
	b=[]
	for i in a:
		if i not in b:
			b.append(i)
	if len(b) == len(a):
		return 1
	else:
		return 0
def driver():
	q = int(input('Enter prime value for q: '))
	while isPrime(q)==0:
		q = int(input("Please enter a PRIME NUMBER ONLY for q: "))
	prim = []
	for i in range(1,q):
		temp1=[]
		for j in range(1,q):
			temp = (i**j)%q
			temp1.append(temp)
		if isUnique(temp1):
			prim.append(i)
	print("Primitive roots are "+str(prim))
	alpha = random.choice(prim)
	print('Selected alpha is : '+ str(alpha))
	p = int(input('Enter the number of communications: '))
	priv = []
	for i in range(p):
		temp = int(input("Enter "+str((i+1))+" private key: "))
		while temp >= q:
			temp = int(input("Enter "+str((i+1))+" private key STRICTLY LESS THAN q: "))
		priv.append(temp)
	public =[]
	for i in priv:
		public.append((alpha**i)%q)
	print("Public keys are : "+str(public))
	one = int(input("Enter first person for communication: "))
	two = int(input("Enter second person for communication: "))
	while two == one:
		two = int(input("Same person cannot be used again. Enter another: "))
	print("Key exchange for 1st person... ")
	k1 = (public[one-1]**priv[two-1])%q
	print(k1)
	print("Key exchange for 2nd person... ")
	k2 = (public[two-1]**priv[one-1])%q
	print (k2)
	if k1 == k2:
		print("Key exchanges are same.")
	else:
		print("Error")
driver()
