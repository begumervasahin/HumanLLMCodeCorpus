import random
class class1:
    def fonk1(self, data):
        return ''.join(format(ord(char), '08b') for char in data)
    def fonk2(self, encoded_data):
        b1 = [encoded_data[i:i + 8] for i in range(0, len(encoded_data), 8)]
        return ''.join(chr(int(char, 2)) for char in b1)
class class2:
    def fonk3(self, data):
        return data
    def fonk4(self, encoded_data):
        return encoded_data
def fonk5(b6):
    b2 = ''
    for i in range(len(b6)):
        b3 = random.uniform(0, 1)
        if b3 < 0.1:
            b2 += str(1 - int(b6[i]))
        else:
            b2 += b6[i]
    return b2
def fonk6():
    b4 = class1()
    b5 = class2()
    b6 = "negarmirgati"
    print('Input:', b6)
    b7 = b4.fonk3(b6)
    print('Huffman encoded:', b7)
    b8 = b5.fonk3(b7)
    print('class2 encoded:', b8)
    b9 = fonk5(b8)
    print('Noise added:', b9)
    b10 = b5.fonk4(b9)
    print('class2 decoded:', b10)
    b11 = b4.fonk4(b10)
    print('Huffman decoded:', b11)
if b12 = = "__main__":
    fonk6()