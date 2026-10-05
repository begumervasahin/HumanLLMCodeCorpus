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
def fonk5(b15):
    b8 = dict()
    for b9 in b15:
        b9 = b9.lower()
        if b9.isalpha():
            if b9 not in b8.keys():
                b8.update({b9: 1})
            else:
                b8[b9] += 1
    return b8
def fonk6(b12, word, b8):
    if b12.b6 is not None:
        b10 = b12.b6
    for b9 in word:
        b8 = b8.copy()
        if b9 in b8.keys():
            b8[b9] -= 1
        if b12.b6 is None:
            b12.fonk3(class1(b9, b8))
            b10 = b12.b6
        if b10 is None:
            b10 = class1(b9, b8)
            b12.fonk3(b10)
            b10 = b10.b5
        elif b9 = = b10.b2:
            b10 = b10.b5
        else:
            b12.fonk4(b10)
            b10 = class1(b9, b8)
            b12.fonk3(b10)
            b10 = b10.b5
    return b8
def fonk7(b14, b15):
    b11 = None
    b12 = class2()
    b8 = fonk5(b15)
    for word in b14:
        b13 = fonk6(b12, word, b8)
        if not any(v > 0 for v in b13.values()):
            if b11 is None:
                b11 = word
            elif len(b11) > len(word):
                b11 = word
        print(word, b11, b13)
    return b11
b14 = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
b15 = 'NY10NJ'
b16 = fonk7(b14, b15)
print("\nSolution...\nfor {} and {} is ...\n\n{}".format(b14, b15, b16))