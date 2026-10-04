import os
import sys
import json
class class1:
    class class2:
        def fonk1(self, b1 = None):
            self.b1 = b1
            self.b2 = None
            self.b3 = None
    def fonk2(self, b4, b5):
        self.fonk3(b4)
        self.b4 = b4
        self.b5 = b5
        self.b6 = self.class2()
        self.b7 = {}
        self.b8 = ""
        self.a1 = 0
    def fonk3(self, file_path):
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            self.fonk8(f"Error: {file_path} does not exist.")
    def fonk4(self):
        with open(self.b4, 'r') as encoded_file:
            serialized_map, self.b8, b9 = encoded_file.read().split('\n')
            self.b7 = json.loads(serialized_map)
            self.a1 = int(b9)
    def fonk5(self):
        for b1, code in self.b7.items():
            b10 = self.b6
            for b11 in code:
                if b11 = = '0':
                    if b10.b2 is None:
                        b10.b2 = self.class2()
                    b10 = b10.b2
                else:
                    if b10.b3 is None:
                        b10.b3 = self.class2()
                    b10 = b10.b3
            b10.b1 = b1
    def fonk6(self):
        b12 = ''.join(f"{bin(ord(b1))[2:]:0>8}" for b1 in self.b8)
        b12 = b12[:-self.a1]
        b13 = []
        b10 = self.b6
        for b11 in b12:
            b10 = b10.b2 if b11 == '0' else b10.b3
            if b10.b1:
                b13.append(b10.b1)
                b10 = self.b6
        self.fonk7(b13)
        print("Huffman decoding completed successfully.")
    def fonk7(self, b13):
        with open(self.b5, 'w') as decoded_file:
            decoded_file.write(''.join(b13))
    @staticmethod
    def fonk8(message):
        print(message)
        sys.exit(1)
def fonk9():
    if len(sys.argv) != 3:
        class1.fonk8(f"Usage: python {sys.argv[0]} [encoded text path] [decoded text path]")
    b4 = sys.argv[1]
    b5 = sys.argv[2]
    b14 = class1(b4, b5)
    b14.fonk4()
    b14.fonk5()
    b14.fonk6()
if b15 = = '__main__':
    fonk9()