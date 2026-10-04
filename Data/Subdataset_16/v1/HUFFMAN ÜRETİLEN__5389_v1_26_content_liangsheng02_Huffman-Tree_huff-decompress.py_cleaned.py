import os
import pickle
import argparse
import time
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b4):
        self.b4 = os.path.splitext(b4)[0]
        self.b8, self.b5 = self.fonk3()
        self.b6 = self.fonk4()
        self.b7 = self.fonk5()
        print('Decompression complete:', len(self.b7), 'characters')
    def fonk3(self):
        b8 = pickle.load(open(self.b4 + '-symbol-model.pkl', 'rb'))
        b9 = b8.pop('padding_length')
        b10 = open(self.b4 + '.bin', 'rb').read()
        b5 = (''.join([bin(byte)[2:].zfill(8) for byte in b10]))[:-b9]
        return b8, b5
    def fonk4(self):
        b6 = class1()
        for b1, code in self.b8.items():
            b11 = b6
            for b12 in code:
                if b12 = = '0':
                    if not b11.b2:
                        b11.b2 = class1()
                    b11 = b11.b2
                else:
                    if not b11.b3:
                        b11.b3 = class1()
                    b11 = b11.b3
            b11.b1 = b1
        return b6
    def fonk5(self):
        b7 = []
        b11 = self.b6
        for b12 in self.b5:
            b11 = b11.b2 if b12 == "0" else b11.b3
            if b11.b1:
                b7.append(b11.b1)
                b11 = self.b6
        b13 = ''.join(b7)
        with open(self.b4 + "-decompressed.txt", 'w', b14 = 'utf-8', newline='\n') as output_file:
            output_file.write(b13)
        return b13
if b15 = = '__main__':
    b16 = argparse.ArgumentParser(description="Huffman Decompression")
    b16.add_argument('infile', b17 = str, help="Input b4 for Huffman decompression (without extension)")
    b18 = b16.parse_args()
    b19 = time.time()
    class2(b18.infile)
    b20 = time.time()
    print(f"Time taken to decode the compressed b4: {b20 - b19:.2f} seconds")