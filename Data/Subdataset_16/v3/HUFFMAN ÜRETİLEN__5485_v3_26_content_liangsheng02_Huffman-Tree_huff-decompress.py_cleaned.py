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
        print(f'Decompression complete: {len(self.b7)} characters')
    def fonk3(self):
        with open(f"{self.b4}-symbol-model.pkl", 'rb') as model_file:
            b8 = pickle.load(model_file)
        b9 = b8.pop('b9')
        with open(f"{self.b4}.bin", 'rb') as binary_file:
            b10 = binary_file.read()
        b11 = ''.join(f"{byte:08b}" for byte in b10)[:-b9]
        return b8, b11
    def fonk4(self):
        b6 = class1()
        for b1, code in self.b8.items():
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
        b14 = []
        b12 = self.b6
        for b13 in self.b5:
            b12 = b12.b2 if b13 == '0' else b12.b3
            if b12.b1:
                b14.append(b12.b1)
                b12 = self.b6
        b7 = ''.join(b14)
        b15 = f"{self.b4}-decompressed.txt"
        self.fonk6(b15, b7)
        return b7
    def fonk6(self, b4, text):
        with open(b4, 'w', b16 = 'utf-8', newline='\n') as output_file:
            output_file.write(text)
def fonk7():
    b17 = argparse.ArgumentParser(description="Huffman Decompression Tool")
    b17.add_argument('infile', b18 = str, help="Input file for Huffman decompression (without extension)")
    b19 = b17.parse_args()
    b20 = time.time()
    class2(b19.infile)
    b21 = time.time() - b20
    print(f"Time taken to decode the compressed file: {b21:.2f} seconds")
if b22 = = '__main__':
    fonk7()