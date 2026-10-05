import re
import os
import pickle
class class1:
    def fonk1(self, b1 = ""):
        self.b2 = {"5": [], "10": [], "20": [], "50": [], "100": []}
        if b1 = = '':
            self.b3 = True
        else:
            with open(b1, 'r') as file:
                self.b3 = False
                for line in file.readlines():
                    b4 = line.split()
                    self.b2[b4[-1]].append(b4[0])
        self.b5 = re.compile(r'^[A-M][A-L](?!00000000)\d{8}(?![OZ])[A-Z]$')
        with open('bill_file_77.txt', 'r') as serial_file:
            b6 = serial_file.readlines()
    def fonk2(self, bill_string):
        b4 = bill_string.split()
        b7 = b4[1]
        b8 = b4[0]
        b9 = self.b2[b7]
        if self.b3 and b8 not in b9:
            for i, value in enumerate(b9):
                if b8 < value:
                    b9.fonk2(i, b8)
                    return
            b9.append(b8)
        elif not self.b3 and b8 not in b9:
            b9.append(b8)
    def fonk3(self):
        for key in self.b2:
            self.b2[key].sort()
        self.b3 = True
    def fonk4(self, bill_string):
        b4 = bill_string.split()
        b7 = b4[1]
        b8 = b4[0]
        b10 = self.b2[b7]
        if b8 in b10:
            return True
        else:
            return False
    def fonk5(self, bill_string):
        b4 = bill_string.split()
        b11 = b4[1]
        b8 = b4[0]
        b10 = self.b2[b11]
        a1 = 0
        b12 = len(b10) - 1
        while a1 <= b12:
            b13 = (b12 + a1)
            if b10[b13] == b8:
                return True
            if b10[b13] > b8:
                b12 = b13 - 1
            else:
                a1 = b13 + 1
        return False
    def fonk6(self, b1, b14 = False):
        if b14 and not self.b3:
            self.fonk3()
        b15 = self.binary_search if self.b3 else self.linear_search
        b16 = class1()
        with open(b1, 'r') as serial_file:
            b17 = []
            for line in serial_file:
                b8, b7 = line.split()[0], line.split()[1]
                b18 = b8 + " " + b7
                if b15(line) or not self.b5.match(b8):
                    b17.append(b18)
        return b17