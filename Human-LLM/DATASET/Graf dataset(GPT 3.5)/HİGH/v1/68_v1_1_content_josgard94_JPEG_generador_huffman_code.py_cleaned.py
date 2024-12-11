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
    b6 = open(b1, 'r')
    for b17 in b6:
        b5 = b17.split("\t")
        if b5[0] == "space" or b5[0] == "salto":
            continue
        b3[b5[0]] = float(b5[1].rstrip())
    b6.close()
    b4 = fonk3(b3)
    fonk4(b4)
    with open(b2, 'r') as b7, open("comprimido.dat", 'wb') as salida:
        b7 = (b7.read().rstrip()).lower()
        b8 = fonk5(b4, b7)
        b9 = fonk6(b8)
        b10 = fonk7(b9)
        salida.write(bytes(b10))
def fonk2(dic):
    b11 = sorted(dic.items(), key=operator.itemgetter(1), reverse=False)
    return b11[0][0], b11[1][0]
def fonk3(dic):
    if len(dic) == 2:
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
    with open("codigos.b7", "w") as file:
        for b17 in dic:
            if b17 = = '\n':
                file.write("salto" + "\t" + dic.get(b17, b17) + "\n")
            else:
                file.write(dic.get(0, b17) + "\t" + dic.get(b17, b17) + "\n")
def fonk5(codes, texto):
    b18 = ""
    for ch in texto.split():
        if ch in codes:
            b18 += codes[ch]
    return b18
def fonk6(encoded):
    b19 = 8 - len(encoded) % 8
    for _ in range(b19):
        encoded += "0"
    b20 = "{0:08b}".format(b19)
    return b20 + encoded
def fonk7(cadena_binaria):
    if len(cadena_binaria) % 8 != 0:
        exit(0)
    b21 = bytearray()
    for b17 in range(0, len(cadena_binaria), 8):
        b22 = cadena_binaria[b17:b17+8]
        b21.append(int(b22, 2))
    return b21
fonk1()
print("\n\n")
b23 = os.path.getsize(sys.argv[2])
b24 = os.path.getsize("comprimido.dat")
b23 = b23 / (1024 * 1024.0)
b24 = b24 / (1024 * 1024.0)
b25 = ((b24 / b23) * 100)
print("Texto original: " + str(sys.argv[2]) + " Tamanio: " + str(b23) + " MB")
print("File comprimido: comprimido.dat Tamanio: " + str(b24) + " MB")
print("Archivo " + sys.argv[2] + " comprimido en " + str(round(b25)) + "%")
print("Archivo de texto comprimido :) !!\n\n")