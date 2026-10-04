
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
    for b23 in b4:
        b3 = fonk1(b23)
        for key in b1:
            if key in b3:
                b3[key] -= b1[key]
                if b3[key] < 0:
                    break
            else:
                break
        else:
            if b2 is None or len(b2) > len(b23):
                b2 = b23
    return b2
b4 = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
b5 = 'NY10NJ'
print(f"Working solution for the b2 b23: {fonk2(b4, b5)}\n")
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
b13 = class1('e', {'j':1, 'n':2, 'y':1})
b14 = class1('n', {'j':1, 'n':1, 'y':1})
b15 = class1('j', {'n':1, 'y':1})
b16 = class2()
b16.fonk5(b13)
b16.fonk5(b14)
b16.fonk5(b15)
print("Constructing...")
b17 = b16.b10
while b17:
    print(b17.b8.b6 if b17.b8 else None, b17.b6, b17.b7)
    b17 = b17.b9
print("Deleting... and inserting...")
b16.fonk6(b15)
b18 = class1('o', {'n':1, 'y':1})
b19 = class1('y', {'n':1})
b16.fonk5(b18)
b17 = b16.b10
while b17:
    print(b17.b6, b17.b7)
    b17 = b17.b9
def fonk7(b22, b23, b1):
    b20 = b22.b10 if b22.b10 else None
    for ch in b23:
        b21 = b1.copy()
        if ch in b21:
            b21[ch] -= 1
        if b20 is None or ch != b20.b6:
            b22.fonk5(class1(ch, b21))
            b20 = b22.b10 if b22.b10 and b20 is None else b20.b9
        else:
            b20 = b20.b9
    return b21
print('\nTesting...')
b22 = class2()
b23 = 'enjoy'
b1 = {'j':1, 'n':2, 'y':1}
fonk7(b22, b23, b1)
print(b23)
b17 = b22.b10
while b17:
    print(b17.b6, b17.b7)
    b17 = b17.b9
b23 = 'english'
fonk7(b22, b23, b1)
print(b23)
b17 = b22.b10
while b17:
    print(b17.b6, b17.b7)
    b17 = b17.b9
def fonk8(b4, b5):
    b2 = None
    b22 = class2()
    b1 = fonk1(b5)
    for b23 in b4:
        b24 = fonk7(b22, b23, b1)
        if all(v <= 0 for v in b24.values()):
            if b2 is None or len(b2) > len(b23):
                b2 = b23
        print(b23, b2, b24)
    return b2
b25 = fonk8(b4, b5)
print(f"\nSolution...\nfor {b4} and {b5} is ...\n\n{b25}")