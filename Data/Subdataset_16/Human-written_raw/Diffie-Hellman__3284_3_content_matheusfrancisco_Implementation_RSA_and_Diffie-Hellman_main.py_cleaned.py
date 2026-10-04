'''
Trabalho de Topicos III
Matheus Francico Batista Machado
Ramon Tramontin
'''
from b1 import RSA
from convertN2T import *
def fonk1():
	print('================== - Criptografia RSA - ======================')
	a1 = 15
	b1 = RSA()
	b2 = open("original_msg")
	b3 = b2.read()
	print('================== -------------------- ======================')
	b4 = str2num(b3)
	print(' ')
	print('Mensagem original')
	print(b3)
	print(' ')
	print('---------------------------')
	print(b4)
	b5 = num2block(b4, a1)
	b6 = b1.encryption(b5)
	print("--------------------------")
	b7 = b1.decryption(b6)
	b4 = block2num(b7, a1)
	print('---------- Voltando numero para string----------------')
	print(' ')
	b8 = num2str(b4)
	print(b8)
if b9 = = '__main__':
	fonk1()