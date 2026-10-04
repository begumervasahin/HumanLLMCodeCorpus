
import re
def fonk1(b5):
    b1 = {}
    for b13 in b5.lower():
        if b13.isalpha():
            b1[b13] = b1.get(b13, 0) + 1
    return b1
def fonk2(b4, b5):
    b1 = fonk1(b5)
    b2 = None
    for b21 in b4:
        b3 = fonk1(b21)
        for key in b1:
            if key in b3:
                b3[key] -= b1[key]
                if b3[key] < 0:
                    break
            else:
                break
        else:
            if b2 is None or len(b2) > len(b21):
                b2 = b21
    return b2
b4 = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
b5 = 'NY10NJ'
print(f"Working solution for the b2 b21: {fonk2(b4, b5)}\n")
class class1:
    def fonk3(self, b6 = None, b8=None):
        self.b7 = b6
        self.b8 = b8
        self.b9 = None
        self.b10 = None
class class2:
    def fonk4(self):
        self.b11 = None
    def fonk5(self, trie_node):
        if self.b11 is None:
            self.b11 = trie_node
            return
        b12 = self.b11
        while b12.b10:
            b12 = b12.b10
        b12.b10 = trie_node
        trie_node.b9 = b12
    def fonk6(self, trie_node):
        if self.b11 is None:
            raise Exception("There are no nodes left to delete!")
        if trie_node.b9:
            trie_node.b9.b10 = None
        else:
            self.b11 = None
def fonk7(b14, b21, b1):
    if b14.b11 is not None:
        b12 = b14.b11
    for b13 in b21:
        b1 = b1.copy()
        if b13 in b1:
            b1[b13] -= 1
        if b14.b11 is None:
            b14.fonk5(class1(b13, b1))
            b12 = b14.b11
        if b12 is None:
            b12 = class1(b13, b1)
            b14.fonk5(b12)
            b12 = b12.b10
        elif b13 = = b12.b7:
            b12 = b12.b10
        else:
            b14.fonk6(b12)
            b12 = class1(b13, b1)
            b14.fonk5(b12)
            b12 = b12.b10
    return b1
def fonk8(b4, b5):
    b2 = None
    b14 = class2()
    b1 = fonk1(b5)
    for b21 in b4:
        b15 = fonk7(b14, b21, b1)
        if not any(v > 0 for v in b15.values()):
            if b2 is None or len(b2) > len(b21):
                b2 = b21
        print(b21, b2, b15)
    return b2
print("Constructing...")
b16 = class2()
b17 = [
    class1('e', {'j': 1, 'n': 2, 'y': 1}),
    class1('n', {'j': 1, 'n': 1, 'y': 1}),
    class1('j', {'n': 1, 'y': 1})
]
for b18 in b17:
    b16.fonk5(b18)
b18 = b16.b11
while b18:
    print(b18.b9.b7 if b18.b9 else None, b18.b7, b18.b8)
    b18 = b18.b10
print("Deleting... and inserting...")
b16.fonk6(b17[2])
b19 = class1('o', {'n': 1, 'y': 1})
b20 = class1('y', {'n': 1})
b16.fonk5(b19)
b18 = b16.b11
while b18:
    print(b18.b7, b18.b8)
    b18 = b18.b10
print('\nTesting...')
b14 = class2()
b21 = 'enjoy'
b1 = {'j': 1, 'n': 2, 'y': 1}
fonk7(b14, b21, b1)
print(b21)
b18 = b14.b11
while b18:
    print(b18.b7, b18.b8)
    b18 = b18.b10
b21 = 'english'
fonk7(b14, b21, b1)
print(b21)
b18 = b14.b11
while b18:
    print(b18.b7, b18.b8)
    b18 = b18.b10
b22 = fonk8(b4, b5)
print(f"\nSolution...\nfor {b4} and {b5} is ...\n\n{b22}")