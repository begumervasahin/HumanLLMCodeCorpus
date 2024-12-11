class class1:
    def fonk1(self, b1 = None, b2=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
class class2:
    def fonk2(self):
        self.b5 = None
    def fonk3(self, trieNode):
        if self.b5 is None:
            self.b5 = trieNode
            return
        b6 = self.b5
        while b6.b4:
            b6 = b6.b4
        b6.b4 = trieNode
        b6.b4.b3 = b6
    def fonk4(self, trieNode):
        if self.b5 is None:
            raise Exception("The trie is empty, cannot delete nodes!")
        if trieNode.b3:
            trieNode.b3.b4 = None
        else:
            self.b5 = None
def fonk5(plate):
    b7 = {}
    for b1 in plate:
        b1 = b1.lower()
        if b1.isalpha():
            b7[b1] = b7.get(b1, 0) + 1
    return b7
def fonk6(b7, b1):
    b8 = b7.copy()
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
            if b10.b5 is None:
                b10.fonk3(class1(b1, b12))
                b6 = b10.b5
            else:
                b6 = b10.b5
                while b6:
                    if b1 = = b6.b1:
                        break
                    b6 = b6.b4
                if b6 is None:
                    b10.fonk3(class1(b1, b12))
                    b6 = b10.b5
                else:
                    b6 = b6.b4
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