import random
from Huffman import HuffmanCoding
from Convolutional import Convolutional
def fonk1(encoded_data, b1 = 0.1):
    return ''.join(
        str(1 - int(bit)) if random.uniform(0, 1) < b1 else bit
        for bit in encoded_data
    )
def fonk2():
    b2 = HuffmanCoding()
    b3 = Convolutional()
    b4 = "negarmirgati"
    print('Input:', b4)
    b5 = b2.encode(b4)
    print('Huffman Encoded:', b5)
    b6 = b3.encode(b5)
    print('Convolutional Encoded:', b6)
    b7 = fonk1(b6)
    print('Noisy Input:', b7)
    b8 = b3.decode(b7)
    print('Convolutional Decoded:', b8)
    b9 = b2.decode(b8)
    print('Huffman Decoded:', b9)
if b10 = = "__main__":
    fonk2()