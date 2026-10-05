import random
class class1:
    def fonk1(self, b1 = None, b2=None):
        if b1 is None:
            b1 = "<path to>/lefff-3.4.mlex"
        if b2 is None:
            b2 = "<path to>/lefff-3.4-addition.mlex"
        self.b3 = b1
        self.b4 = b2
        self.a1 = 0
        self.a2 = 1
        self.a3 = 2
        self.a4 = 3
        self.a5 = 4
        self.b5 = {'adj': 'a', 'adv': 'r', 'nc': 'n', 'np': 'n', 'v': 'v', 'auxAvoir': 'v', 'auxEtre': 'v'}
        self.fonk2()
    def fonk2(self):
        b6 = set()
        with open(self.b3, b7 = 'utf-8') as lefff_file:
            for b8 in lefff_file:
                b8 = b8[:-1]
                b9 = b8.split('\t')
                b10 = (b9[self.a1], b9[self.a2], b9[self.a3])
                if b10 not in b6:
                    b6.add(b10)
        b11 = set()
        b12 = set()
        with open(self.b4, b7 = 'utf-8') as lefff_additional_data_file:
            for b13 in lefff_additional_data_file:
                b13 = b13[:-1]
                b14 = b13.split('\t')
                b15 = (b14[self.a1], b14[self.a2], b14[self.a3])
                try:
                    b16 = (b14[self.a1], b14[self.a2],
                                       b14[self.a5])
                except IndexError as err:
                    print("Error! ", err)
                    print("Length", len(b14))
                    print(self.a1, self.a5)
                    print(b14[self.a1])
                b11.add(b16)
                b12.add(b15)
        b11.add(('chiens', 'nc', 'chiens'))
        b12.add(('résidente', 'nc', 'résident'))
        b12.add(('résidentes', 'nc', 'résident'))
        b11.add(('traductrice', 'nc', 'traductrice'))
        b6 = (b6 - b11) | b12
        b17 = dict()
        for triplet in b6:
            if triplet[self.a1] not in b17:
                b17[triplet[self.a1]] = set()
                b17[triplet[self.a1]].add(triplet)
            else:
                b17[triplet[self.a1]].add(triplet)
        self.b18 = b17
    def fonk3(self, b20):
        return b20 in ['a', 'n', 'r', 'v']
    def fonk4(self, sample_size):
        b19 = list(self.b18)
        return [self.b18[b19[i]] for i in random.sample(range(len(b19)), sample_size)]
    def fonk5(self, end):
        a6 = 0
        for element in self.b18:
            a6 += 1
            print(element)
            if a6 > end:
                break
    def fonk6(self, b22, b20 = "n"):
        b21 = b22
        if not (b20 = = "np"):
            b22 = b22.lower()
        if b22 in self.b18.keys():
            b23 = self.b18[b22]
        else:
            b23 = []
        b24 = []
        if self.fonk3(b20):
            for triplet in b23:
                if triplet[self.a2] in self.b5.keys():
                    b25 = self.b5[triplet[self.a2]]
                    if b25 = = b20:
                        return triplet[self.a3]
        else:
            for triplet in b23:
                b26 = (triplet[self.a3], triplet[self.a2])
                if b26 not in b24:
                    b24.append(b26)
        if not b24:
            if self.fonk3(b20):
                return b21
            elif b21[0].isupper():
                b24 = (b21, 'np')
        return b24
b27 = class1()
b28 = "chat"
b29 = "n"
b30 = b27.fonk6(b28, b29)
print(f"Lemmatized b30 for '{b28}' with a2 '{b29}': {b30}")