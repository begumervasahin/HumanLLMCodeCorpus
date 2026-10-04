import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
import binascii
def fonk1(b5):
    b1 = ''
    for i in range(0, len(b5)):
        b2 = random.uniform(0, 1)
        if(b2 < 0.1):
            b1 += str(1 - int(b5[i]))
        else:
            b1 += (b5[i])
    return b1
def fonk2() :
    b3 = HuffmanCoding()
    b4 = Convolutional()
    b5 = "negarmirgati"
    print('b5', b5)
    b6 = b3.encode(b5)
    print('huffman coded', b6)
    b7 = b4.encode(b6)
    print('Convolutional encoded', b7)
    b8 = fonk1(b7)
    print('noise added', b8)
    b9 = b4.decode(b8)
    print('convolutional decode', b9)
    b10 = b3.decode(b9)
    print('huffman decode', b10)
if b11 = = "__main__":
      fonk2()