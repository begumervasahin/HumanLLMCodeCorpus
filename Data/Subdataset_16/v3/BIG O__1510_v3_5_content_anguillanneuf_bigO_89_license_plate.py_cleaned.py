import re
def fonk1(b5):
    b1 = {}
    for ch in b5.lower():
        if ch.isalpha():
            b1[ch] = b1.get(ch, 0) + 1
    return b1
def fonk2(b4, b5):
    b1 = fonk1(b5)
    b2 = None
    for b26 in b4:
        b3 = fonk1(b26)
        for key in b1:
            if key in b3:
                b3[key] -= b1[key]
                if b3[key] < 0:
                    break
            else:
                break
        else:
            if b2 is None or len(b2) > len(b26):
                b2 = b26
    return b2
b4 = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
b5 = 'NY10NJ'
print(f"Working solution for the b2 b26: {fonk2(b4, b5)}\n")
class class1:
    def fonk3(self, b6 = None, b7=None):
        self.b6 = b6
        self.b7 = b7
        self.b8 = None
        self.b9 = None
class class2:
    def fonk4(self):
        self.b10 = None
    def fonk5(self, b12):
        if self.b10 is None:
            self.b10 = b12
        else:
            b11 = self.b10
            while b11.b9:
                b11 = b11.b9
            b11.b9 = b12
            b12.b8 = b11
    def fonk6(self, b12):
        if self.b10 is None:
            raise Exception("There are no nodes left to delete!")
        if b12.b8:
            b12.b8.b9 = b12.b9
        if b12.b9:
            b12.b9.b8 = b12.b8
        if b12 = = self.b10:
            self.b10 = b12.b9
def fonk7(b16, b26, b1):
    b13 = b16.b10
    b14 = b1.copy()
    for ch in b26:
        if ch in b14:
            b14[ch] -= 1
        if b13 is None or ch != b13.b6:
            b15 = class1(ch, b14.copy())
            b16.fonk5(b15)
            b13 = b15
        else:
            b13 = b13.b9
    return b14
def fonk8(b4, b5):
    b2 = None
    b16 = class2()
    b1 = fonk1(b5)
    for b26 in b4:
        b17 = fonk7(b16, b26, b1)
        if all(v <= 0 for v in b17.values()):
            if b2 is None or len(b2) > len(b26):
                b2 = b26
        print(b26, b2, b17)
    return b2
if b18 = = "__main__":
    b19 = class1('e', {'j': 1, 'n': 2, 'y': 1})
    b20 = class1('n', {'j': 1, 'n': 1, 'y': 1})
    b21 = class1('j', {'n': 1, 'y': 1})
    b22 = class2()
    b22.fonk5(b19)
    b22.fonk5(b20)
    b22.fonk5(b21)
    print("Constructing...")
    b23 = b22.b10
    while b23:
        print(b23.b8.b6 if b23.b8 else None, b23.b6, b23.b7)
        b23 = b23.b9
    print("Deleting... and inserting...")
    b22.fonk6(b21)
    b24 = class1('o', {'n': 1, 'y': 1})
    b25 = class1('y', {'n': 1})
    b22.fonk5(b24)
    b23 = b22.b10
    while b23:
        print(b23.b6, b23.b7)
        b23 = b23.b9
    print('\nTesting...')
    b16 = class2()
    b26 = 'enjoy'
    b1 = {'j': 1, 'n': 2, 'y': 1}
    fonk7(b16, b26, b1)
    print(b26)
    b23 = b16.b10
    while b23:
        print(b23.b6, b23.b7)
        b23 = b23.b9
    b26 = 'english'
    fonk7(b16, b26, b1)
    print(b26)
    b23 = b16.b10
    while b23:
        print(b23.b6, b23.b7)
        b23 = b23.b9
    b27 = fonk8(b4, b5)
    print(f"\nSolution...\nfor {b4} and {b5} is ...\n\n{b27}")