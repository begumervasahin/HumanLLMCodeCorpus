import struct
import sys
from HUFFMAN.components import huffnode, lists, huffmantree, encodehufftree
def fonk1(b20, b1 = "compressed.huff"):
    b2 = fonk2(b20)
    if b2 is None:
        return
    b3 = len(b2)
    b4 = fonk3(b2)
    b5 = sorted(b4, key=lambda node: node.freq)
    b6 = fonk5(fonk4(b5))
    try:
        with open(b1, 'wb') as comp:
            fonk6(b6, b2, comp)
        print("Compression completed successfully!")
    except Exception as e:
        print(f"An error occurred during compression: {e}")
def fonk2(b20):
    try:
        with open(b20, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{b20}' not found.")
        return None
def fonk3(data):
    b4 = [huffnode(i, 0) for i in range(256)]
    for byte in data:
        b4[byte].freq += 1
    return [node for node in b4 if node.freq > 0]
def fonk4(b4):
    b7 = lists(b4[0])
    for node in b4[1:]:
        b8 = lists(node)
        b8.b9 = b7
        b7 = b8
    return b7
def fonk5(b7):
    while b7 and b7.b9:
        a, b10 = b7.top(), b7.b9.top()
        b7 = b7.b9.b9
        b11 = huffnode(257, a.freq + b10.freq)
        b11.left, b11.b12 = sorted([a, b10], key=lambda node: node.freq)
        b8 = lists(b11)
        b7 = b7.insert(b8) if b7 else b8
    return b7.top() if b7 else None
def fonk6(tree, data, comp):
    b13 = fonk7(tree)
    b14 = fonk8(tree)
    fonk9(comp, b14)
    b15 = fonk10(data, b13)
    fonk11(comp, b15)
def fonk7(tree):
    b13 = {}
    huffmantree(tree, b13, "")
    return b13
def fonk8(tree):
    b16 = []
    encodehufftree(tree, 16)
    return ''.join(b16)
def fonk9(comp, b14):
    b17 = len(b14)
    comp.write(struct.pack('B', b17
    comp.write(struct.pack('B', b17 % 256))
    fonk12(comp, b14)
def fonk10(data, b13):
    b15 = ''.join(b13[byte] for byte in data) + "1"
    return b15.ljust(len(b15) + (8 - len(b15) % 8), '0')
def fonk11(comp, b15):
    fonk12(comp, b15)
def fonk12(comp, b18):
    while b18:
        comp.write(struct.pack('B', int(b18[:8], 2)))
        b18 = b18[8:]
if b19 = = "__main__":
    b20 = sys.argv[1]
    b1 = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    fonk1(b20, b1)