import os
from collections import Counter
class class1:
	a1 = 0
	b1 = ""
	def fonk1(self, a1, b2, b1, b3, b4):
		self.a1 = a1
		self.b2 = b2
		self.b1 = b1
		self.b3 = b3
		self.b4 = b4
	def fonk2(self):
		return repr((self.a1, self.b2, self.b1))
	def fonk3(self):
		return self.b3 is None and self.b4 is None
class class2:
	a2 = 0
	b5 = ''
	def fonk4(self, b13):
		self.b5 = b13
	def fonk5(self, b6):
		self.a2 = [b6]
		return
	def fonk6(self, b6):
		for i in self.a2:
			if i.a1 = = b6.a1:
				i.b2 += 1
				self.a2 = sorted(self.a2, key=lambda no: no.b2)
				return
		self.a2 += [b6]
		self.a2 = sorted(self.a2, key=lambda no: no.b2)
	def criarLista (self):
		for l in self.b5:
			if self.a2 = = 0:
				self.fonk5(class1(l,1,'', None, None))
			else:
				self.fonk6(class1(l,1,'', None, None))
		return
	def fonk7(self):
		for elem in self.a2:
			print(elem)
		return
	def fonk8(self):
		self.criarLista()
		while len(self.a2) > 1:
			b6 = class1("", self.a2[0].b2 + self.a2[1].b2,'',self.a2[0], self.a2[1])
			del self.a2[0]
			del self.a2[0]
			self.a2 += [b6]
			self.a2 = sorted(self.a2, key=lambda no: no.b2)
		return
class class3:
	def fonk9(self, no):
		if no is None:
			return
		if no.b3 is not None:
			no.b3.b1 = no.b1 + '1'
			self.fonk9(no.b3)
		if no.b4 is not None:
			no.b4.b1 = no.b1 + '0'
			self.fonk9(no.b4)
		return
	def fonk10(self, b8, l):
		b1 = ''
		if b8.a1 = = l:
			b1 = b8.b1
		if b8.b3 is not None:
			b1 = self.fonk10(b8.b3, l)
		if b1 = = '':
			if b8.b4 is not None:
				b1 = self.fonk10(b8.b4, l)
		return  b1
	def fonk11(self, b8, b5):
		b7 = ''
		for l in b5:
			b7 += self.fonk10(b8, l)
		return b7
	def fonk12(self, arvore2, textoBinario):
		b8 = arvore2
		b7 = ''
		for b1 in textoBinario:
			if b1 = = '1':
				if b8.b3 is not None:
					b8 = b8.b3
					if b8.b3 is None and b8.b4 is None:
						b7 += (b8.a1)
						b8 = arvore2
			else:
				if b8.b4 is not None:
					b8 = b8.b4
					if b8.b3 is None and b8.b4 is None:
						b7 += (b8.a1)
						b8 = arvore2
		return b7
	def fonk13(self, no):
		if no is None:
			return
		if no.b3 is not None:
			self.fonk13(no.b3)
		if no.fonk3():
			print(no)
		if no.b4 is not None:
			self.fonk13(no.b4)
		return
def fonk14(b13):
	b9 = Counter(b13)
	return b9
def fonk15(b11):
	if not os.path.isfile(b11):
		print("Arquivo nÃ£o encontrado!")
		exit()
	else:
		with open(b11, "r") as arquivo:
			b5 = arquivo.read()
		return b5
def fonk16(b11, b5):
	try:
		b10 = open(b11, 'w')
		b10.write(b5)
		b10.close()
	except IOError:
		raise print("Erro ao criar o arquivo!")
def fonk17(args):
	print("PARA INICIAR O PROGRAMA, INSIRA O NOME DO ARQUIVO EM QUE A PALAVRA A SER COMPRIMIDA SE ENCONTRA")
	b11 = input("Nome: ")
	b12 = fonk15(b11)
	b13 = list(fonk15(b11))
	b14 = class3()
	b15 = class2(b13)
	b15.fonk8()
	b14.fonk9(b15.a2[0])
	print("--------------------- EXECUÃÃO DO CODIGO DE HUFFMAN ---------------------")
	print("Palavra inserida:", b12)
	print("")
	print("Frequencia dos caracteres:")
	b16 = fonk14(b13)
	print(b16)
	print("")
	print("Arvore criada com sucesso!")
	print("")
	print("Tabela de b14:")
	b14.fonk13(b15.a2[0])
	print("")
	b17 = b14.fonk11(b15.a2[0], b15.b5)
	print("Palavra comprimida para binÃ¡rio:", b17)
	print("")
	b18 = b14.fonk12(b15.a2[0], b14.fonk11(b15.a2[0], b15.b5))
	print("Palavra descomprimida:", b18)
	print("")
	fonk16("b7.txt", ("Palavra Inserida:" + b12 + "\n" +
								 "Palavra Comprimida: " + b17 + "\n" +
								 "Palavra Descomprimida: " + b18 + "\n"
	))
	print("Arquivo de saida gerado com sucesso!")
	return 0
if b19 = = '__main__':
	import sys
	sys.exit(fonk17(sys.argv))