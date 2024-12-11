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
        else:
            b6 = self.b5
            while b6.b4:
                b6 = b6.b4
            b6.b4 = trieNode
            trieNode.b3 = b6
    def fonk4(self, trieNode):
        if self.b5 is None:
            raise Exception("The trie is empty. Cannot delete nodes.")
        if trieNode.b3:
            trieNode.b3.b4 = trieNode.b4
        else:
            self.b5 = trieNode.b4
        if trieNode.b4:
            trieNode.b4.b3 = trieNode.b3
def fonk5(plate):
    b7 = {}
    for b1 in plate.lower():
        if b1.isalpha():
            b7[b1] = b7.get(b1, 0) + 1
    return b7
def fonk6(b15, plate):
    b8 = fonk5(plate)
    b9 = None
    for word in b15:
        b10 = fonk5(word)
        for key in b8:
            if key in b10:
                b10[key] -= b8[key]
                if b10[key] < 0:
                    break
        else:
            if b9 is None or len(b9) > len(word):
                b9 = word
    return b9
def fonk7(b13, word, b11):
    if b13.b5:
        b6 = b13.b5
    else:
        b6 = None
    for b1 in word:
        b11 = b11.copy()
        if b1 in b11:
            b11[b1] -= 1
        if not b6:
            b6 = class1(b1, b11)
            b13.fonk3(b6)
        elif b1 != b6.b1:
            b13.fonk4(b6)
            b6 = class1(b1, b11)
            b13.fonk3(b6)
        b6 = b6.b4
    return b11
def fonk8(b15, plate):
    b12 = None
    b13 = class2()
    b11 = fonk5(plate)
    for word in b15:
        b14 = fonk7(b13, word, b11)
        if not any(v > 0 for v in b14.values()):
            if b12 is None or len(b12) > len(word):
                b12 = word
    return b12
b15 = ['enjoy', 'enjoying', 'joy', 'joyful', 'joyous', 'joyousness']
b16 = 'NY10NJ'
print("Shortest word found:", fonk6(b15, b16))
print("Solution for '{}' and '{}' is '{}'".format(b15, b16, fonk8(b15, b16)))