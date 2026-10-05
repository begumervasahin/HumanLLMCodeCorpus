class class1:
    def fonk1(self, b1 = None, b3=None):
        self.b2 = b1
        self.b3 = b3
        self.b4 = None
        self.b5 = None
class class2:
    def fonk2(self):
        self.b6 = None
    def fonk3(self, trieNode):
        if self.b6 is None:
            self.b6 = trieNode
            return
        b7 = self.b6
        while b7.b5 is not None:
            b7 = b7.b5
        b7.b5 = trieNode
        b7.b5.b4 = b7
    def fonk4(self, trieNode):
        if self.b6 is None:
            raise Exception("There are no nodes left to delete!")
        if trieNode.b4:
            trieNode.b4.b5 = None
        else:
            self.b6 = None
def fonk5(plate):
    b8 = {}
    for b1 in plate:
        b1 = b1.lower()
        if b1.isalpha():
            if b1 not in b8:
                b8[b1] = 1
            else:
                b8[b1] += 1
    return b8
def fonk6(b8, b1):
    b8 = b8.copy()
    if b1 in b8:
        b8[b1] -= 1
    return b8
def fonk7(b13, plate):
    b9 = None
    b10 = class2()
    b11 = fonk5(plate)
    for word in b13:
        b12 = b11.copy()
        for b1 in word:
            b12 = fonk6(b12, b1)
            if b10.b6 is None:
                b10.fonk3(class1(b1, b12))
                b7 = b10.b6
            else:
                b7 = b10.b6
                while b7:
                    if b1 = = b7.b2:
                        break
                    b7 = b7.b5
                if b7 is None:
                    b10.fonk3(class1(b1, b12))
                    b7 = b10.b6
                else:
                    b7 = b7.b5
        if not any(v > 0 for v in b12.values()):
            if b9 is None:
                b9 = word
            elif len(b9) > len(word):
                b9 = word
        print(word, b9, b12)
    return b9
b13 = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
b14 = 'NY10NJ'
b15 = fonk7(b13, b14)
print("\nSolution...\nfor {} and {} is ...\n\n{}".format(b13, b14, b15))