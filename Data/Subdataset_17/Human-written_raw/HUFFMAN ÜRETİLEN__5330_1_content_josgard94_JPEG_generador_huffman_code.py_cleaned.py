
from decimal import Decimal
import sys
import os
import operator
result_probabilidades = "result.txt"
fichero = sys.argv[2]
def compresor_huffman():
	probabilidades = {}
	tabla_codigos = {}
	line = ""
	archivo = open(result_probabilidades,'r');
	for i in  archivo:
		line = i.split("\t")
		if(line[0] == "space"):
			pass
		elif(line[0]=="salto"):
			pass
		else:
			probabilidades[line[0]] = float(line[1].rstrip())
	archivo.close()
	tabla_codigos = huffmanCode(probabilidades)
	save_codes(tabla_codigos)
	with open(fichero,'r') as txt, open("comprimido.dat",'wb') as salida:
		txt = (txt.read().rstrip()).lower()
		encoded_text = TextEncode(tabla_codigos,txt)
		padded_encodded = PadEncode(encoded_text);
		CadenaBits = GeneraBitArray(padded_encodded)
		salida.write(bytes(CadenaBits))
def ordenar_probabilidades(dic):
	ordenado = sorted(dic.items(), key = operator.itemgetter(1), reverse=False)
	return ordenado[0][0], ordenado[1][0]
def huffmanCode(dic):
	if(len(dic) == 2):
		return dict(zip(dic.keys(), ['0', '1']))
	p_copy = dic.copy()
	K1, K2 = ordenar_probabilidades(dic)
	p1, p2 = p_copy.pop(K1), p_copy.pop(K2)
	p_copy[K1 + K2] = p1 + p2
	c = huffmanCode(p_copy)
	ca1a2 = c.pop(K1 + K2)
	c[K1], c[K2] = ca1a2 + '0', ca1a2 + '1'
	return c
def save_codes(dic):
	file = open("codigos.txt","w")
	for i in dic:
		if i == '\n':
			file.write("salto"+"\t"+ dic.get(i,i)+"\n");
		else:
			file.write(dic.get(0,i) +"\t"+ dic.get(i,i)+"\n");
	file.close();
def TextEncode(codes, texto):
	encode_text = ""
	for ch in texto.split():
		if ch in codes:
			encode_text += codes[ch]
	return encode_text
def PadEncode(encoded):
	padding = 8 - len(encoded) % 8
	for i in range(padding):
		encoded += "0"
	padded_info = "{0:08b}".format(padding)
	encoded = padded_info + encoded
	return encoded
def GeneraBitArray(cadena_binaria):
	if(len(cadena_binaria) % 8 != 0):
		exit(0)
	Cbits = bytearray()
	for i in range(0, len(cadena_binaria), 8):
		byte = cadena_binaria[i:i+8]
		Cbits.append(int(byte, 2))
	return Cbits
compresor_huffman()
print("\n\n")
sizefile = os.path.getsize(sys.argv[2])
sizefile2 = os.path.getsize("comprimido.dat")
sizefile= sizefile/(1024*1024.0)
sizefile2 = sizefile2/(1024*1024.0)
porcentaje  = ((sizefile2/sizefile) * 100)
print ("Texto original: " +str(sys.argv[2])+ " Tamanio: "+ str(sizefile)+" MB")
print ("File comprimido: comprimido.dat Tamanio: " + str(sizefile2)+" MB")
print("Archivo "+sys.argv[2]+" comprimido en "+ str(round(porcentaje))+"%")
print("Archivo de texto comprimido :) !!\n\n")