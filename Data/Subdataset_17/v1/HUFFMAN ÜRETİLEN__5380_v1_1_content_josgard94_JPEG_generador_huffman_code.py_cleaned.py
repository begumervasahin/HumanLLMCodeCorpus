import sys
import os
import operator
from collections import defaultdict
result_probabilidades = "result.txt"
codigos_file = "codigos.txt"
compressed_file = "comprimido.dat"
fichero = sys.argv[2]
def compresor_huffman():
    probabilidades = {}
    tabla_codigos = {}
    with open(result_probabilidades, 'r') as archivo:
        for line in archivo:
            parts = line.split("\t")
            symbol = parts[0]
            probability = float(parts[1].strip())
            if symbol not in ["space", "salto"]:
                probabilidades[symbol] = probability
    tabla_codigos = huffmanCode(probabilidades)
    save_codes(tabla_codigos)
    with open(fichero, 'r') as txt, open(compressed_file, 'wb') as salida:
        txt_content = txt.read().rstrip().lower()
        encoded_text = TextEncode(tabla_codigos, txt_content)
        padded_encoded = PadEncode(encoded_text)
        binary_data = GeneraBitArray(padded_encoded)
        salida.write(bytes(binary_data))
def ordenar_probabilidades(dic):
    ordenado = sorted(dic.items(), key=operator.itemgetter(1), reverse=False)
    return ordenado[0][0], ordenado[1][0]
def huffmanCode(dic):
    if len(dic) == 2:
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
    with open(codigos_file, "w") as file:
        for symbol, code in dic.items():
            if symbol == '\n':
                file.write("salto\t" + code + "\n")
            else:
                file.write(symbol + "\t" + code + "\n")
def TextEncode(codes, texto):
    encode_text = ""
    for ch in texto:
        if ch in codes:
            encode_text += codes[ch]
    return encode_text
def PadEncode(encoded):
    padding = 8 - len(encoded) % 8
    encoded += "0" * padding
    padded_info = "{0:08b}".format(padding)
    encoded = padded_info + encoded
    return encoded
def GeneraBitArray(cadena_binaria):
    if len(cadena_binaria) % 8 != 0:
        exit(0)
    Cbits = bytearray()
    for i in range(0, len(cadena_binaria), 8):
        byte = cadena_binaria[i:i+8]
        Cbits.append(int(byte, 2))
    return Cbits
compresor_huffman()
sizefile = os.path.getsize(fichero)
sizefile2 = os.path.getsize(compressed_file)
sizefile_mb = sizefile / (1024 * 1024.0)
sizefile2_mb = sizefile2 / (1024 * 1024.0)
compression_ratio = (sizefile2_mb / sizefile_mb) * 100
print(f"\n\nTexto original: {fichero} Tamanio: {sizefile_mb:.2f} MB")
print(f"File comprimido: {compressed_file} Tamanio: {sizefile2_mb:.2f} MB")
print(f"Archivo {fichero} comprimido en {round(compression_ratio)}%")
print("Archivo de texto comprimido :) !!\n\n")