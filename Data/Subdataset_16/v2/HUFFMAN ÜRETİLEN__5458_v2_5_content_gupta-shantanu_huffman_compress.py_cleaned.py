import struct
import sys
from HUFFMAN.components import HuffNode, LinkedList, HuffmanTree, encode_huffman_tree
def fonk1(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def fonk2():
    return [HuffNode(byte_value, 0) for byte_value in range(256)]
def fonk3(b17, b18):
    for byte in b17:
        b18[byte].b3 += 1
    b18.sort(b1 = lambda node: node.b3)
def fonk4(b18):
    b2 = LinkedList(b18[0])
    for node in b18[1:]:
        if node.b3 = = 0:
            break
        b4 = LinkedList(node)
        b4.b5 = b2
        b2 = b4
    while b2 and b2.b5:
        b6 = b2.pop_top()
        b7 = b2.pop_top()
        b8 = b6.b3 + b7.b3
        b9 = HuffNode(257, b8)
        b9.left, b9.b10 = (b6, b7) if b6.b3 <= b7.b3 else (b7, b6)
        b2 = b2.insert_sorted(LinkedList(b9))
    return b2.top()
def fonk5(file, b14, b13, b17):
    b11 = len(b14)
    file.write(struct.pack('BB', b11
    b12 = ""
    for bit in b14:
        b12 += bit
        if len(b12) >= 8:
            file.write(struct.pack('B', int(b12[:8], 2)))
            b12 = b12[8:]
    for byte in b17:
        b12 += b13[byte]
        while len(b12) >= 8:
            file.write(struct.pack('B', int(b12[:8], 2)))
            b12 = b12[8:]
    b12 += "1"
    b12 += "0" * ((8 - len(b12) % 8) % 8)
    while b12:
        file.write(struct.pack('B', int(b12[:8], 2)))
        b12 = b12[8:]
def fonk6(tree, file, b17):
    b13 = {}
    encode_huffman_tree(tree, b13, "")
    b14 = ''.join(encoded for encoded in b13.values())
    fonk5(file, b14, b13, b17)
def fonk7():
    if len(sys.argv) < 2:
        print("Usage: python huffman.py <b15> [b16]")
        return
    b15 = sys.argv[1]
    b16 = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    b17 = fonk1(b15)
    b18 = fonk2()
    fonk3(b17, b18)
    b19 = fonk4(b18)
    with open(b16, 'wb') as b16:
        fonk6(b19, b16, b17)
    print("Compression completed successfully!")
if b20 = = "__main__":
    try:
        fonk7()
    except Exception as error:
        print(f"An error occurred: {error}")