from AEstrela import AEstrela
from BestFirst import BestFirst
from TipoNo import TipoNo
import logging
import minesweeper as mns
import testeImagem as ti
import sys
class class1:
	def fonk1(self):
		logging.basicConfig(b1 = 'minesweeperIa.log', level=logging.DEBUG,
		b2 = '%(levelname)s %(funcName)s => %(message)s')
		if(b3 = =1):
			self.b4 = AEstrela()
		elif(b3 = =2):
			self.b4 = BestFirst()
	def fonk2(self):
		b5 = [[' ' for i in range(b14)] for i in range(b14)]
		b6 = []
		b7 = []
		b8 = None
		b9 = True
		b10 = True
		b11 = self.b4.jogadaInicial()
		b12 = (b11.getX(),b11.getY())
		if not b6:
			b6, b13 = mns.setupgrid(b14, b12, b15)
		while(b10):
			b11 = self.b4.definirJogada(b5)
			if str(type(b11)) == "<class 'NoneType'>":
				print('Perdeu, a lista de abertos ficou vazia')
				b9 = False
				b10 = False
			else:
				b12 = (b11.getX(),b11.getY())
				print(b12, b11.getData())
				if b11.getData()=='F':
					b10 = mns.jogar(b12,b5,b6,b7,b13, flag=True)
				else:
					b10 = mns.jogar(b12,b5,b6,b7,b13)
					b8 = b11
		return b9
if len(sys.argv) > 1:
	b3 = sys.argv[1]
	b14 = sys.argv[2]
	b15 = sys.argv[3]
else:
	print('Algoritmos:\nA*:1\nBestFirst:2')
	b3 = input('Selecione o Algoritmo(1 ou 2):')
	b14 = input('Selecione o tamanho do tabuleiro:')
	b15 = input('Selecione o numero de bombas:')
b3 = int(b3)
b14 = int(b14)
b15 = int(b15)
'''
a1 = 0
for x in range(0,101):
	b16 = class1()
	if b16.fonk2():
		a1+=1
print(str(a1/100))
'''
b16 = class1()
b16.fonk2()