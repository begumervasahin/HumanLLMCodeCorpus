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
        with open(self.b4 + '-symbol-model.pkl', 'rb') as pkl_file:
            b8 = pickle.load(pkl_file)
        b9 = b8.pop('b9')
        with open(self.b4 + '.bin', 'rb') as bin_file:
            b10 = bin_file.read()
        b5 = ''.join(bin(byte)[2:].zfill(8) for byte in b10)[:-b9]
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
def fonk6():
    b15 = argparse.ArgumentParser(description="Huffman Decompression Utility")
    b15.add_argument('infile', b16 = str, help="Input b4 for decompression")
    b17 = b15.parse_args()
    b18 = time.time()
    class2(b17.infile)
    b19 = time.time()
    print("Time taken to decode the compressed b4: {:.2f} seconds".format(b19 - b18))
if b20 = = '__main__':
    fonk6()