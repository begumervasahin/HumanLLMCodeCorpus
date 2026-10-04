import os
import sys
'''
Algumas implementaÃ§Ãµes nÃ£o estÃ£o sendo usadas,
sÃ£o apenas para testes
'''
def fonk1(b2, b3):
	if (b3>b2):
		b1 = b2
		b2 = b3
		b3 = b1
	a1 = 1
	a2 = 0
	while not(a1 = =0):
		a2 = b2
		a1 = b2 - a2*b3
		b2 = b3
		b3 = a1
	return b2
def fonk2(p,a2):
	while a2 != 0:
		(p,a2) = (a2,p % a2)
	return p
def fonk3(b2,b3):
	return (b2*b3)
def fonk4(b2,b3):
	u,v,b5,b4 = 1, 0 ,0 ,1
	if (b3<b2):
		b1 = b3
		b3 = b2
		b2 = b1
	while b3!=0:
		a2 = b2
		b2,b3 = b3,b2-a2*b3
		u,b5 = b5,u-a2*b5
		v,b4 = b4,v-a2*b4
	return b2,u,v
if b6 = = '__main__':
	print('Rotina de test dos algoritmos')
	b7 = fonk4(5023,1487)
	b8 = fonk2(18,102)
	print(b7)
	print(' ')
	print(' \n : ',b8)