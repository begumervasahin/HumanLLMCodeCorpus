import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def fonk1(input):
    b1 = ''
    for i in range(0, len(input)):
        b2 = random.uniform(0, 1)
        if b2 < 0.1:
            b1 += str(1 - int(input[i]))
        else:
            b1 += input[i]
    return b1
def fonk2():
    b3 = HuffmanCoding()
    b4 = Convolutional()
    b5 = "negarmirgati"
    print('input:', b5)
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