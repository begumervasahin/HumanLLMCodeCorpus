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
        if not os.path.exists(b4) or not os.path.isfile(b4):
            self.fonk6(f"Error: {b4} does not exist.")
        self.b4 = b4
        self.b5 = b5
        self.b6 = self.class2()
        self.b7 = {}
        self.b8 = ""
        self.a1 = 0
    def fonk3(self):
        with open(self.b4, 'r') as encoded_file:
            serialized_map, self.b8, self.a1 = encoded_file.read().split('\n')
            self.b7 = json.loads(serialized_map)
    def fonk4(self):
        for b1, code in self.b7.items():
            b9 = self.b6
            for b10 in code:
                if b10 = = '0':
                    if b9.b2 is None:
                        b9.b2 = self.class2()
                    b9 = b9.b2
                else:
                    if b9.b3 is None:
                        b9.b3 = self.class2()
                    b9 = b9.b3
            b9.b1 = b1
    def fonk5(self):
        b11 = ''.join(f"{bin(ord(b1))[2:]:0>8}" for b1 in self.b8)
        b11 = b11[:-int(self.a1)]
        b12 = []
        b9 = self.b6
        for b10 in b11:
            b9 = b9.b2 if b10 == '0' else b9.b3
            if b9.b1 is not None:
                b12.append(b9.b1)
                b9 = self.b6
        with open(self.b5, 'w') as decoded_file:
            decoded_file.write(''.join(b12))
        print("Huffman decoding completed successfully.")
    @staticmethod
    def fonk6(message):
        print(message)
        sys.exit(0)
def fonk7():
    if len(sys.argv) != 3:
        class1.fonk6(f"Usage: python {sys.argv[0]} [encoded text path] [decoded text path]")
    b4 = sys.argv[1]
    b5 = sys.argv[2]
    b13 = class1(b4, b5)
    b13.fonk3()
    b13.fonk4()
    b13.fonk5()
if b14 = = '__main__':
    fonk7()