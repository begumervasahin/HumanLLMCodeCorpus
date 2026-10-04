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
    def fonk2(self, input_file):
        self.b4 = os.path.splitext(input_file)[0]
        self.text_code, self.b5 = self.fonk3()
        self.b6 = self.fonk4()
        self.b7 = self.fonk5()
        print(f'Decompression complete: {len(self.b7)} characters')
    def fonk3(self):
        with open(f'{self.b4}-symbol-model.pkl', 'rb') as pkl_file:
            b8 = pickle.load(pkl_file)
        b9 = b8.pop('b9')
        with open(f'{self.b4}.bin', 'rb') as bin_file:
            b10 = bin_file.read()
        b11 = ''.join(f'{byte:08b}' for byte in b10)[:-b9]
        return b8, b11
    def fonk4(self):
        b6 = class1()
        for b1, code in self.text_code.items():
            b12 = b6
            for b13 in code:
                if b13 = = '0':
                    if not b12.b2:
                        b12.b2 = class1()
                    b12 = b12.b2
                else:
                    if not b12.b3:
                        b12.b3 = class1()
                    b12 = b12.b3
            b12.b1 = b1
        return b6
    def fonk5(self):
        b7 = []
        b12 = self.b6
        for b13 in self.b5:
            b12 = b12.b2 if b13 == '0' else b12.b3
            if b12.b1:
                b7.append(b12.b1)
                b12 = self.b6
        b14 = ''.join(b7)
        with open(f'{self.b4}-decompressed.txt', 'w', b15 = 'utf-8') as output_file:
            output_file.write(b14)
        return b14
def fonk6():
    b16 = argparse.ArgumentParser(description="Huffman Decompression Utility")
    b16.add_argument('infile', b17 = str, help="Input file for decompression")
    b18 = b16.parse_args()
    b19 = time.time()
    class2(b18.infile)
    b20 = time.time()
    print(f"Time taken to decode the compressed file: {b20 - b19:.2f} seconds")
if b21 = = '__main__':
    fonk6()