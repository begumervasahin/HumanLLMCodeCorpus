import os
import sys
'''
Algumas implementaÃ§Ãµes nÃ£o estÃ£o sendo usadas,
sÃ£o apenas para testes
'''
def gcf(n1, n2):
	if (n2>n1):
		aux = n1
		n1 = n2
		n2 = aux
	r =1
	q =0
	while not(r==0):
		q = n1
		r = n1 - q*n2
		n1 = n2
		n2 = r
	return n1
def gcd(p,q):
	while q != 0:
		(p,q) = (q,p % q)
	return p
def lcm(n1,n2):
	return (n1*n2)
def euclideanExtendedGCD(n1,n2):
	u,v,s,t = 1, 0 ,0 ,1
	if (n2<n1):
		aux = n2
		n2 =n1
		n1 = aux
	while n2!=0:
		q =n1
		n1,n2 = n2,n1-q*n2
		u,s = s,u-q*s
		v,t = t,v-q*t
	return n1,u,v
if __name__ == '__main__':
	print('Rotina de test dos algoritmos')
	b = euclideanExtendedGCD(5023,1487)
	d = gcd(18,102)
	print(b)
	print(' ')
	print(' \n : ',d)