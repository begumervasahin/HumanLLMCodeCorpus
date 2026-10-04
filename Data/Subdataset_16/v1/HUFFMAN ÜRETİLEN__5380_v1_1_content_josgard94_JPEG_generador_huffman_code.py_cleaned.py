import sys
import os
import operator
from collections import defaultdict
b1 = "result.txt"
b2 = "codigos.txt"
b3 = "comprimido.dat"
b4 = sys.argv[2]
def fonk1():
    b5 = {}
    b6 = {}
    with open(b1, 'r') as archivo:
        for line in archivo:
            b7 = line.split("\t")
            b8 = b7[0]
            b9 = float(b7[1].strip())
            if b8 not in ["space", "salto"]:
                b5[b8] = b9
    b6 = fonk3(b5)
    fonk4(b6)
    with open(b4, 'r') as txt, open(b3, 'wb') as salida:
        b10 = txt.read().rstrip().lower()
        b11 = fonk5(b6, b10)
        b12 = fonk6(b11)
        b13 = fonk7(b12)
        salida.write(bytes(b13))
def fonk2(dic):
    b14 = sorted(dic.items(), key=operator.itemgetter(1), reverse=False)
    return b14[0][0], b14[1][0]
def fonk3(dic):
    if len(dic) == 2:
        return dict(zip(dic.keys(), ['0', '1']))
    b15 = dic.copy()
    K1, b16 = fonk2(dic)
    p1, b17 = b15.pop(K1), b15.pop(b16)
    b15[K1 + b16] = p1 + b17
    b18 = fonk3(b15)
    b19 = b18.pop(K1 + b16)
    b18[K1], b18[b16] = b19 + '0', b19 + '1'
    return b18
def fonk4(dic):
    with open(b2, "w") as file:
        for b8, code in dic.items():
            if b8 = = '\n':
                file.write("salto\t" + code + "\n")
            else:
                file.write(b8 + "\t" + code + "\n")
def fonk5(codes, texto):
    b20 = ""
    for ch in texto:
        if ch in codes:
            b20 += codes[ch]
    return b20
def fonk6(b23):
    b21 = 8 - len(b23) % 8
    b23 += "0" * b21
    b22 = "{0:08b}".format(b21)
    b23 = b22 + b23
    return b23
def fonk7(cadena_binaria):
    if len(cadena_binaria) % 8 != 0:
        exit(0)
    b24 = bytearray()
    for i in range(0, len(cadena_binaria), 8):
        b25 = cadena_binaria[i:i+8]
        b24.append(int(b25, 2))
    return b24
fonk1()
b26 = os.path.getsize(b4)
b27 = os.path.getsize(b3)
b28 = b26 / (1024 * 1024.0)
b29 = b27 / (1024 * 1024.0)
b30 = (b29 / b28) * 100
print(f"\n\nTexto original: {b4} Tamanio: {b28:.2f} MB")
print(f"File comprimido: {b3} Tamanio: {b29:.2f} MB")
print(f"Archivo {b4} comprimido en {round(b30)}%")
print("Archivo de texto comprimido :) !!\n\n")