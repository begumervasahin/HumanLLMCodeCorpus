import re, os, pickle
class class1:
    def fonk1(self, b1 = ""):
        self.b2 = {"5":[], "10":[], "20":[], "50":[], "100":[]}
        if b1 = = '':
            self.b3 = True
        else:
            b4 = open(b1, 'r').readlines()
            self.b3 = False
            for b5 in b4:
                b5 = b5.split()
                self.b2[b5[-1]].append(b5[0])
        self.b6 = re.compile(r'^[A-M][A-L](?!00000000)\d{8}(?![OZ])[A-Z]''$')
        b7 = open('bill_file_77.txt', 'r').readlines()
    def fonk2(self, bill_string):
        b8 = bill_string.split()
        b9 = b8[1]
        b10 = b8[0]
        b11 = self.b2[b9]
        if self.b3 and b10 not in b11:
            a1 = 0
            for a1 in range(len(b11)):
                if b10 < b11[a1]:
                    b11.fonk2(a1, b10)
                    return
            b11.append(b10)
        elif not self.b3 and b10 not in b11:
            b11.append(b10)
    def fonk3(self):
        for key in self.b2:
            self.b2[key].sort()
        self.b3 = True
    def fonk4(self, bill_string):
        b8 = bill_string.split()
        b9 = b8[1]
        b10 = b8[0]
        b12 = self.b2[b9]
        if b10 in b12:
            return True
        else:
            return False
    def fonk5(self, bill_string):
        b8 = bill_string.split()
        b13 = b8[1]
        b10 = b8[0]
        b14 = self.b2[b13]
        a2 = 0
        b15 = len(b14) - 1
        while a2 <= b15:
            b16 = (b15 + a2)
            if b14[b16] == b10:
                return True
            if b14[b16] > b10:
                b15 = b16 - 1
            else:
                a2 = b16 + 1
        return False
    def fonk6(self, b1, b17 = False):
        if b17 and not self.b3:
            self.fonk3()
        b18 = self.binary_search if self.b3 else self.linear_search
        b19 = class1()
        b20 = open(b1, 'r')
        b21 = []
        for b5 in b20:
            b22 = b5.split()[0]
            b23 = b5.split()[1]
            b24 = b22 + " " + b23
            if b18(b5) or not self.b6.match(b22):
                b21.append(b24)
        return b21