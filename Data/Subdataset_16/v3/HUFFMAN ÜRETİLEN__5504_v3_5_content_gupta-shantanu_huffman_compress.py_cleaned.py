import struct
import sys
from HUFFMAN.components import HuffNode, LinkedList, HuffmanTree, encode_huffman_tree
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def fonk2():
    return [HuffNode(b8, 0) for b8 in range(256)]
def fonk3(b15, b16):
    for byte in b15:
        b16[byte].b3 += 1
    b16.sort(b1 = lambda node: node.b3)
def fonk4(b16):
    b2 = LinkedList(b16[0])
    for node in b16[1:]:
        if node.b3 = = 0:
            break
        b2 = LinkedList(node, b2)
    while b2 and b2.next:
        b4 = b2.pop_top()
        b5 = b2.pop_top()
        b6 = b4.b3 + b5.b3
        b7 = HuffNode(257, b6, b4, b5)
        b2 = b2.insert_sorted(LinkedList(b7))
    return b2.top()
def fonk5(file, b9):
    while len(b9) >= 8:
        b8 = int(b9[:8], 2)
        file.write(struct.pack('B', b8))
        b9 = b9[8:]
    return b9
def fonk6(file, b12, b11, b15):
    b10 = len(b12)
    file.write(struct.pack('BB', b10
    b9 = b12
    b9 = fonk5(file, b9)
    for byte in b15:
        b9 += b11[byte]
        b9 = fonk5(file, b9)
    b9 += "1"
    b9 += "0" * ((8 - len(b9) % 8) % 8)
    fonk5(file, b9)
def fonk7(tree, file, b15):
    b11 = {}
    encode_huffman_tree(tree, b11, "")
    b12 = ''.join(b11[byte] for byte in b11)
    fonk6(file, b12, b11, b15)
def fonk8():
    if len(sys.argv) < 2:
        print("Usage: python huffman.py <b13> [b14]")
        return
    b13 = sys.argv[1]
    b14 = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    try:
        b15 = fonk1(b13)
        b16 = fonk2()
        fonk3(b15, b16)
        b17 = fonk4(b16)
        with open(b14, 'wb') as b14:
            fonk7(b17, b14, b15)
        print("Compression completed successfully!")
    except Exception as error:
        print(f"An error occurred: {error}")
if b18 = = "__main__":
    fonk8()