import re
class class1:
    def fonk1(self, b1 = ""):
        self.b2 = {"5": [], "10": [], "20": [], "50": [], "100": []}
        if b1 = = '':
            self.b3 = True
        else:
            b4 = open(b1, 'r').readlines()
            self.b3 = False
            for b5 in b4:
                b5 = b5.split()
                self.b2[b5[-1]].append(b5[0])
        self.b6 = re.compile(r'^[A-M][A-L](?!00000000)\d{8}(?![OZ])[A-Z]$')
    def fonk2(self, bill_string):
        b7 = bill_string.split()
        b8 = b7[1]
        b9 = b7[0]
        b10 = self.b2[b8]
        if self.b3 and b9 not in b10:
            a1 = 0
            for a1 in range(len(b10)):
                if b9 < b10[a1]:
                    b10.fonk2(a1, b9)
                    return
            b10.append(b9)
        elif not self.b3 and b9 not in b10:
            b10.append(b9)
    def fonk3(self):
        for key in self.b2:
            self.b2[key].sort()
        self.b3 = True
    def fonk4(self, bill_string):
        b7 = bill_string.split()
        b8 = b7[1]
        b9 = b7[0]
        b11 = self.b2[b8]
        if b9 in b11:
            return True
        else:
            return False
    def fonk5(self, bill_string):
        b7 = bill_string.split()
        b12 = b7[1]
        b9 = b7[0]
        b13 = self.b2[b12]
        a2 = 0
        b14 = len(b13) - 1
        while a2 <= b14:
            b15 = (b14 + a2)
            if b13[b15] == b9:
                return True
            if b13[b15] > b9:
                b14 = b15 - 1
            else:
                a2 = b15 + 1
        return False
    def fonk6(self, b1, b16 = False):
        if b16 and not self.b3:
            self.fonk3()
        b17 = self.binary_search if self.b3 else self.linear_search
        b18 = open(b1, 'r')
        b19 = []
        for b5 in b18:
            b20 = b5.split()[0]
            b21 = b5.split()[1]
            b22 = b20 + " " + b21
            if b17(b5) or not self.b6.match(b20):
                b19.append(b22)
        return b19
b23 = class1("your_watchlist_file.txt")
b23.fonk2("ABC12345678 20")
b23.fonk2("DEF98765432 10")
b23.fonk2("GHI87654321 5")
print(b23.fonk6("bill_file.txt", b16 = True))