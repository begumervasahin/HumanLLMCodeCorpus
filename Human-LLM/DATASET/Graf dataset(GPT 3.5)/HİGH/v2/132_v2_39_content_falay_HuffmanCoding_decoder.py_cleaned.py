import os
import sys
import json
class class1:
    class class2:
        def fonk1(self, b1 = None):
            self.b1 = b1
            self.b2 = None
            self.b3 = None
    def fonk2(self, b5, b6):
        if not (os.path.exists(b5) and os.path.isfile(b5)):
            self.fonk6('Error: ' + b5 + ' does not exist.')
        self.b4 = self.class2()
        self.b5 = b5
        self.b6 = b6
        self.b7 = {}
        self.b8 = ""
        self.a1 = 0
    def fonk3(self):
        with open(self.b5) as encoded_file:
            serialized_map, self.b8, self.a1 = encoded_file.read().split('\n')
            self.b7 = json.loads(serialized_map)
    def fonk4(self):
        for b1, code in self.b7.items():
            b9 = self.b4
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
        b11 = ""
        for b1 in self.b8:
            b12 = bin(ord(b1))[2:]
            if len(b12) < 8:
                b12 = '0' * (8 - len(b12)) + b12
            b11 += b12
        b11 = b11[:-int(self.a1)]
        b13 = ""
        b9 = self.b4
        for b10 in b11:
            if b10 = = '0':
                b9 = b9.b2
            else:
                b9 = b9.b3
            if b9.b1 is not None:
                b13 += b9.b1
                b9 = self.b4
        with open(self.b6, 'w') as decoded_file:
            decoded_file.write(b13)
        print('Huffman decoding completed successfully.')
    @staticmethod
    def fonk6(message):
        print(message)
        sys.exit(0)
def fonk7(b5, b6):
    b14 = class1(b5, b6)
    b14.fonk3()
    b14.fonk4()
    b14.fonk5()
if b15 = = '__main__':
    if len(sys.argv) != 3:
        class1.fonk6('Usage: python ' + sys.argv[0] + ' [encoded text path] [decoded text path]')
    fonk7(b5 = sys.argv[1], b6=sys.argv[2])