import random
class class1:
    def fonk1(self, b1 = None, lefff_additional_file_path=None):
        self.b2 = b1 or "<path to>/lefff-3.4.mlex"
        self.b3 = lefff_additional_file_path or "<path to>/lefff-3.4-addition.mlex"
        self.INFLECTED_FORM, self.POS, self.LEMMA, self.MISC, self.b4 = 0, 1, 2, 3, 4
        self.b5 = {'adj': 'a', 'adv': 'r', 'nc': 'n', 'np': 'n', 'v': 'v', 'auxAvoir': 'v', 'auxEtre': 'v'}
        self.fonk2()
    def fonk2(self):
        b6 = self.fonk3(self.b2)
        b13, b7 = self.fonk4()
        b6 = (b6 - b7) | b13
        self.b8 = self.fonk5(b6)
    def fonk3(self, file_path):
        b6 = set()
        with open(file_path, b9 = 'utf-8') as lefff_file:
            for b10 in lefff_file:
                b10 = b10.rstrip('\n')
                b11 = b10.split('\t')
                b12 = (b11[self.INFLECTED_FORM], b11[self.POS], b11[self.LEMMA])
                b6.add(b12)
        return b6
    def fonk4(self):
        b7 = set()
        b13 = set()
        with open(self.b3, b9 = 'utf-8') as lefff_additional_data_file:
            for b14 in lefff_additional_data_file:
                b14 = b14.rstrip('\n')
                b15 = b14.split('\t')
                b16 = (b15[self.INFLECTED_FORM], b15[self.POS],
                                   b15[self.LEMMA])
                try:
                    b17 = (b15[self.INFLECTED_FORM], b15[self.POS],
                                       b15[self.b4])
                except IndexError as err:
                    print("Error! ", err)
                    print("Length", len(b15))
                    print(self.INFLECTED_FORM, self.b4)
                    print(b15[self.INFLECTED_FORM])
                b7.add(b17)
                b13.add(b16)
        b7.update({('chiens', 'nc', 'chiens'), ('traductrice', 'nc', 'traductrice')})
        b13.update({('résidente', 'nc', 'résident'), ('résidentes', 'nc', 'résident')})
        return b13, b7
    def fonk5(self, b6):
        b18 = {}
        for a_triplet in b6:
            b18.setdefault(a_triplet[self.INFLECTED_FORM], set()).add(a_triplet)
        return b18
    def fonk6(self, b20):
        return b20 in ['a', 'n', 'r', 'v']
    def fonk7(self, sample_size):
        b19 = list(self.b8)
        return [self.b8[b19[i]] for i in random.sample(range(len(b19)), sample_size)]
    def fonk8(self, end):
        a1 = 0
        for element in self.b8:
            a1 += 1
            print(element)
            if a1 > end:
                break
    def fonk9(self, word, b20 = "n"):
        b21 = word.lower() if not (b20 == "np") else word
        if word in self.b8:
            b22 = self.b8[word]
        else:
            b22 = []
        if self.fonk6(b20):
            return self.fonk10(b22, b20)
        return self.fonk11(b22, b21, b20)
    def fonk10(self, b22, b20):
        for triplet in b22:
            if triplet[self.POS] in self.b5:
                b23 = self.b5[triplet[self.POS]]
                if b23 = = b20:
                    return triplet[self.LEMMA]
        return b21 if self.fonk6(b20) else [(triplet[self.LEMMA], triplet[self.POS]) for triplet in b22]
    def fonk11(self, b22, b21, b20):
        b24 = []
        for triplet in b22:
            b25 = (triplet[self.LEMMA], triplet[self.POS])
            if b25 not in b24:
                b24.append(b25)
        if not b24:
            if b21[0].isupper():
                b24 = (b21, 'np')
        return b24