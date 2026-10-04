import struct
import sys
from HUFFMAN.components import huffnode, lists, huffmantree, encodehufftree
def fonk1(b21, b1 = "compressed.huff"):
    try:
        with open(b21, 'rb') as file:
            b2 = file.read()
    except FileNotFoundError:
        print(f"Error: File '{b21}' not found.")
        return
    b3 = len(b2)
    b4 = [huffnode(i, 0) for i in range(256)]
    for byte in b2:
        b4[byte].freq += 1
    b4 = [node for node in b4 if node.freq > 0]
    b4.sort(b5 = lambda node: node.freq)
    b6 = lists(b4[0])
    for node in b4[1:]:
        b7 = lists(node)
        b7.b8 = b6
        b6 = b7
    b9 = fonk2(b6)
    try:
        with open(b1, 'wb') as comp:
            fonk3(b9, b2, comp)
        print("Compression completed successfully!")
    except Exception as e:
        print(f"An error occurred during compression: {e}")
def fonk2(b6):
    while b6 and b6.b8:
        b10 = b6.top()
        b6 = b6.b8
        b11 = b6.top()
        b6 = b6.b8
        b12 = huffnode(257, b10.freq + b11.freq)
        b12.left, b12.b13 = (b11, b10) if b10.freq > b11.freq else (b10, b11)
        b7 = lists(b12)
        b6 = b6.insert(b7) if b6 else b7
    return b6.top() if b6 else None
def fonk3(b9, b2, comp):
    b14 = {}
    huffmantree(b9, b14, "")
    b15 = fonk4(b9)
    fonk5(comp, b15)
    b16 = fonk6(b2, b14)
    fonk7(comp, b16)
def fonk4(b9):
    b17 = []
    encodehufftree(b9, 16)
    return ''.join(b17)
def fonk5(comp, b15):
    b18 = len(b15)
    comp.write(struct.pack('B', b18
    comp.write(struct.pack('B', b18 % 256))
    b19 = ""
    for bit in b15:
        b19 += bit
        if len(b19) >= 8:
            comp.write(struct.pack('B', int(b19[:8], 2)))
            b19 = b19[8:]
def fonk6(b2, b14):
    b16 = ""
    for byte in b2:
        b16 += b14[byte]
    b16 += "1"
    while len(b16) % 8 != 0:
        b16 += "0"
    return b16
def fonk7(comp, b16):
    while b16:
        comp.write(struct.pack('B', int(b16[:8], 2)))
        b16 = b16[8:]
if b20 = = "__main__":
    b21 = sys.argv[1]
    b1 = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    fonk1(b21, b1)