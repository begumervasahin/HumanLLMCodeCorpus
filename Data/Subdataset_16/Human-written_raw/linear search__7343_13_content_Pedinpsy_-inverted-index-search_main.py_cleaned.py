from hash import hash
import unicodedata
import sys
import os
import re
import time
def fonk1(pasta):
	b1 = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
	b2 = [b3 for b3 in b1 if os.path.isfile(b3)]
	return b2
def fonk2(arquivo,num,hashing):
	b3 = open(arquivo,'r')
	b4 = b3.read()
	b3.close()
	b4 = b4.lower()
	b4 = b4.replace(",","").replace(".","").replace("!","").replace("?","").replace("\r","").replace("\t","").replace("\n","")
	b4 = b4.split(" ")
	for i in b4:
		b5 = i
		b6 = b4.b6(b5)
		b7 = True
		if hashing.getValue(b5):
			for k in hashing.getValue(b5):
				if k[0] == b6 and k[1]== num+1:
					b7 = False
			if b7:
				hashing.insertValue(b5,[b6, num+1])
		else:
			hashing.insertValue(b5,[b6, num+1])
b8 = hash(1000000,3,'multiplication','quadratic')
b9 = hash(1000000,3,'multiplication')
b10 = hash(1000000,3)
b11 = hash(1000000,3,"division","linear")
b12 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
	fonk2(b2[i],i,b9)
for i in sorted(b9.getKeys()):
	print(i,b9.getValue(i)[0][0], b2[(b9.getValue(i)[0][1])-1])
b13 = time.time()
print('tempo para Hashing ultilizando metodo da multiplicacao e colizao linear :',b13 - b12)
b12 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
	fonk2(b2[i],i,b8)
for i in sorted(b8.getKeys()):
	print(i,b8.getValue(i)[0][0], b2[(b8.getValue(i)[0][1])-1])
b13 = time.time()
print('tempo para Hashing ultilizando metodo da multiplicacao e colizao Quadratica :',b13 - b12)
b12 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
	fonk2(b2[i],i,b11)
for i in sorted(b11.getKeys()):
	print(i,b11.getValue(i)[0][0], b2[(b11.getValue(i)[0][1])-1])
b13 = time.time()
print('tempo para Hashing ultilizando metodo da Divisao e colizao linear :',b13 - b12)
b12 = time.time()
b2 = fonk1('base')
for i in range(len(b2)):
	fonk2(b2[i],i,b10	)
for i in sorted(b10.getKeys()):
	print(i,b10.getValue(i)[0][0], b2[(b10.getValue(i)[0][1])-1])
b13 = time.time()
print('tempo para Hashing ultilizando metodo da Divisao e colizao Quadratica :',b13 - b12)
while True:
	b14 = input("digite uma palvra:\n")
	print(b9.getValue(b14))