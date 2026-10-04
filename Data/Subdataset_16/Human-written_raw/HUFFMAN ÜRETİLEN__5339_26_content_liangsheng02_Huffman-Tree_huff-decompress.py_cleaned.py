import os, pickle, argparse, time
class class1(object):
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2(object):
    def fonk2(self, b4):
        self.b4 = os.path.splitext(b4)[0]
        self.b8, self.b5 = self.fonk3()
        self.b6 = self.fonk4()
        self.b7 = self.fonk5()
        print('done:', len(self.b7), 'chars')
    def fonk3(self):
        b8 = pickle.load(open(self.b4 + '-symbol-model.pkl', 'rb'))
        b9 = b8.pop('padding_length')
        b10 = open(self.b4 + '.bin', 'rb').read()
        b5 = (''.join([bin(i)[2:].zfill(8) for i in b10]))[:-b9]
        return b8, b5
    def fonk4(self):
        b6 = class1(None)
        for b1 in self.b8.keys():
            b11 = b6
            for b12 in self.b8[b1]:
                if b12 = = '0':
                    b11.b2 = b11.b2 if b11.b2 else class1(None)
                    b11 = b11.b2
                else:
                    b11.b3 = b11.b3 if b11.b3 else class1(None)
                    b11 = b11.b3
            b11.b1 = b1
        return b6
    def fonk5(self):
        b7 = ''
        b11 = self.b6
        for i in self.b5:
            b11 = b11.b2 if i == "0" else b11.b3
            if b11.b1:
                b7 += b11.b1
                b11 = self.b6
        open(self.b4 + "-decompressed.txt", 'w', b13 = 'utf-8', newline='\n').write(b7)
        return b7
if b14 = = '__main__':
    b15 = argparse.ArgumentParser()
    b15.add_argument('infile', b16 = str, help="pass infile to huff-compress/b19 for compression/decompression")
    b17 = b15.parse_args()
    b18 = time.time()
    b19 = class2(b17.infile)
    b20 = time.time()
    print("decode the compressed b4: ", b20 - b18)