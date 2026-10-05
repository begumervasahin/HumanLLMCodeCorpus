import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def fonk1(input_text, b1 = 0.1):
    b2 = ''
    for bit in input_text:
        if random.random() < b1:
            b2 += str(1 - int(bit))
        else:
            b2 += bit
    return b2
def fonk2():
    b3 = HuffmanCoding()
    b4 = Convolutional()
    b5 = "negarmirgati"
    print('Original input:', b5)
    b6 = b3.encode(b5)
    print('Huffman coded:', b6)
    b7 = b4.encode(b6)
    print('Convolutional encoded:', b7)
    b8 = fonk1(b7)
    print('Noise added:', b8)
    b9 = b4.decode(b8)
    print('Convolutional decoded:', b9)
    b10 = b3.decode(b9)
    print('Huffman decoded:', b10)
if b11 = = "__main__":
    fonk2()