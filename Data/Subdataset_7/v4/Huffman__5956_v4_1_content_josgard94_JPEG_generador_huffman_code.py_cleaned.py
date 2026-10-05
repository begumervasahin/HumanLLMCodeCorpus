
from decimal import Decimal
import sys
import os
import operator
b1 = "result.b6"
b2 = sys.argv[2]
def fonk1():
    b3 = {}
    b4 = {}
    b5 = ""
    with open(b1,'r') as archivo:
        for b16 in archivo:
            b5 = b16.split("\t")
            if b5[0] not in ["space", "salto"]:
                b3[b5[0]] = float(b5[1].rstrip())
    b4 = fonk3(b3)
    fonk4(b4)
    with open(b2,'r') as b6, open("comprimido.dat",'wb') as salida:
        b6 = b6.read().rstrip().lower()
        b7 = fonk5(b4, b6)
        b8 = fonk6(b7)
        b9 = fonk7(b8)
        salida.write(bytes(b9))
def fonk2(dic):
    b10 = sorted(dic.items(), key=operator.itemgetter(1), reverse=False)
    return b10[0][0], b10[1][0]
def fonk3(dic):
    if len(dic) == 2:
        return dict(zip(dic.keys(), ['0', '1']))
    b11 = dic.copy()
    K1, b12 = fonk2(dic)
    p1, b13 = b11.pop(K1), b11.pop(b12)
    b11[K1 + b12] = p1 + b13
    b14 = fonk3(b11)
    b15 = b14.pop(K1 + b12)
    b14[K1], b14[b12] = b15 + '0', b15 + '1'
    return b14
def fonk4(dic):
    with open("codigos.b6", "w") as file:
        for b16 in dic:
            if b16 = = '\n':
                file.write("salto" + "\t" + dic.get(b16, b16) + "\n")
            else:
                file.write(dic.get(0, b16) + "\t" + dic.get(b16, b16) + "\n")
def fonk5(codes, texto):
    b17 = ""
    for ch in texto.split():
        if ch in codes:
            b17 += codes[ch]
    return b17
def fonk6(b20):
    b18 = 8 - len(b20) % 8
    for b16 in range(b18):
        b20 += "0"
    b19 = "{0:08b}".format(b18)
    b20 = b19 + b20
    return b20
def fonk7(cadena_binaria):
    if len(cadena_binaria) % 8 != 0:
        exit(0)
    b9 = bytearray()
    for b16 in range(0, len(cadena_binaria), 8):
        b21 = cadena_binaria[b16:b16+8]
        b9.append(int(b21, 2))
    return b9
fonk1()
print("\n\n")
b22 = os.path.getsize(sys.argv[2])
b23 = os.path.getsize("comprimido.dat")
b22 = b22 / (1024 * 1024.0)
b23 = b23 / (1024 * 1024.0)
b24 = ((b23 / b22) * 100)
print("Texto original: " + str(sys.argv[2]) + " Tamaño: " + str(b22) + " MB")
print("Archivo comprimido: comprimido.dat Tamaño: " + str(b23) + " MB")
print("Archivo " + sys.argv[2] + " comprimido en " + str(round(b24)) + "%")
print("¡Archivo de texto comprimido! :) \n\n")