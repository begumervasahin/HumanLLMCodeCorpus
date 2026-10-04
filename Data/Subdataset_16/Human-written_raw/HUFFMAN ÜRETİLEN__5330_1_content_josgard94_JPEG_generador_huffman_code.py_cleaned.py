
from decimal import Decimal
import sys
import os
import operator
b1 = "result.b7"
b2 = sys.argv[2]
def fonk1():
	b3 = {}
	b4 = {}
	b5 = ""
	b6 = open(b1,'r');
	for b18 in  b6:
		b5 = b18.split("\t")
		if(b5[0] == "space"):
			pass
		elif(b5[0]=="salto"):
			pass
		else:
			b3[b5[0]] = float(b5[1].rstrip())
	b6.close()
	b4 = fonk3(b3)
	fonk4(b4)
	with open(b2,'r') as b7, open("comprimido.dat",'wb') as salida:
		b7 = (b7.read().rstrip()).lower()
		b8 = fonk5(b4,b7)
		b9 = fonk6(b8);
		b10 = fonk7(b9)
		salida.write(bytes(b10))
def fonk2(dic):
	b11 = sorted(dic.items(), key = operator.itemgetter(1), reverse=False)
	return b11[0][0], b11[1][0]
def fonk3(dic):
	if(len(dic) == 2):
		return dict(zip(dic.keys(), ['0', '1']))
	b12 = dic.copy()
	K1, b13 = fonk2(dic)
	p1, b14 = b12.pop(K1), b12.pop(b13)
	b12[K1 + b13] = p1 + b14
	b15 = fonk3(b12)
	b16 = b15.pop(K1 + b13)
	b15[K1], b15[b13] = b16 + '0', b16 + '1'
	return b15
def fonk4(dic):
	b17 = open("codigos.b7","w")
	for b18 in dic:
		if b18 = = '\n':
			b17.write("salto"+"\t"+ dic.get(b18,b18)+"\n");
		else:
			b17.write(dic.get(0,b18) +"\t"+ dic.get(b18,b18)+"\n");
	b17.close();
def fonk5(codes, texto):
	b19 = ""
	for ch in texto.split():
		if ch in codes:
			b19 += codes[ch]
	return b19
def fonk6(b22):
	b20 = 8 - len(b22) % 8
	for b18 in range(b20):
		b22 += "0"
	b21 = "{0:08b}".format(b20)
	b22 = b21 + b22
	return b22
def fonk7(cadena_binaria):
	if(len(cadena_binaria) % 8 != 0):
		exit(0)
	b23 = bytearray()
	for b18 in range(0, len(cadena_binaria), 8):
		b24 = cadena_binaria[b18:b18+8]
		b23.append(int(b24, 2))
	return b23
fonk1()
print("\n\n")
b25 = os.path.getsize(sys.argv[2])
b26 = os.path.getsize("comprimido.dat")
b25 = b25/(1024*1024.0)
b26 = b26/(1024*1024.0)
b27 = ((b26/b25) * 100)
print ("Texto original: " +str(sys.argv[2])+ " Tamanio: "+ str(b25)+" MB")
print ("File comprimido: comprimido.dat Tamanio: " + str(b26)+" MB")
print("Archivo "+sys.argv[2]+" comprimido en "+ str(round(b27))+"%")
print("Archivo de texto comprimido :) !!\n\n")