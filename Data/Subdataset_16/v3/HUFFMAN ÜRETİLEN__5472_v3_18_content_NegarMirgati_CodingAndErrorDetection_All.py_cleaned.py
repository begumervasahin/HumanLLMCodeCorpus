import random
class class1:
    def fonk1(self, data):
        return ''.join(format(ord(char), '08b') for char in data)
    def fonk2(self, encoded_data):
        return ''.join(chr(int(encoded_data[i:i + 8], 2)) for i in range(0, len(encoded_data), 8))
class class2:
    def fonk3(self, data):
        return data
    def fonk4(self, encoded_data):
        return encoded_data
def fonk5(data, b1 = 0.1):
    return ''.join(
        str(1 - int(bit)) if random.uniform(0, 1) < b1 else bit
        for bit in data
    )
def fonk6():
    b2 = class1()
    b3 = class2()
    b4 = "negarmirgati"
    print('Input:', b4)
    b5 = b2.fonk3(b4)
    print('Huffman encoded:', b5)
    b6 = b3.fonk3(b5)
    print('Convolutional encoded:', b6)
    b7 = fonk5(b6)
    print('Noisy data:', b7)
    b8 = b3.fonk4(b7)
    print('Convolutional decoded:', b8)
    b9 = b2.fonk4(b8)
    print('Huffman decoded:', b9)
if b10 = = "__main__":
    fonk6()