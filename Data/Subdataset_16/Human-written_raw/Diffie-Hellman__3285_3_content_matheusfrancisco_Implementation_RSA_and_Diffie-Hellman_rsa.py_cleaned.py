import os
import sys
from euclidean import *
from numberPrime import *
from modular_arithmetic import *
class class1(object):
	a1 = 0
	a2 = 0
	a3 = 0
	def fonk1(self):
		self.a1, self.a2, self.a3 = GenParms(n_bits=100, DEBUG=True)
	def fonk2(self, msg):
		b1 = []
		for i in msg:
			b1.append(modExp(i,self.a3,self.a1))
		print(' \a1')
		print('Mensagem criptografada:', b1)
		return b1
	def fonk3(self, msg):
		b1 = []
		for i in msg:
			b1.append(modExp(i,self.a2,self.a1))
		print('Mensagem Decriptografada :',b1)
		return b1
	def fonk4(self):
		return(self.a1,self.a3)
	def fonk5(self):
		return(self.a1,self.a2)
if b2 = = '__main__':
	print("Rotina de testes:")
	b3 = class1()
	print('')