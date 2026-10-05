import random
class class1:
    def fonk1(self, b1 = None, lefff_additional_file_path=None):
        self.b2 = b1 or "<path to>/lefff-3.4.mlex"
        self.b3 = lefff_additional_file_path or "<path to>/lefff-3.4-addition.mlex"
        self.INFLECTED_FORM, self.POS, self.LEMMA, self.MISC, self.b4 = 0, 1, 2, 3, 4
        self.b5 = {'adj': 'a', 'adv': 'r', 'nc': 'n', 'np': 'n', 'v': 'v', 'auxAvoir': 'v', 'auxEtre': 'v'}
        self.fonk2()
    def fonk2(self):
        b6 = set()
        with open(self.b2, b7 = 'utf-8') as lefff_file:
            for b8 in lefff_file:
                b8 = b8[:-1]
                b9 = b8.split('\t')
                b10 = (b9[self.INFLECTED_FORM], b9[self.POS], b9[self.LEMMA])
                if b10 not in b6:
                    b6.add(b10)
        set_pos_triplets_to_remove, b11 = set(), set()
        with open(self.b3, b7 = 'utf-8') as lefff_additional_data_file:
            for b12 in lefff_additional_data_file:
                b12 = b12[:-1]
                b9 = b12.split('\t')
                b13 = (b9[self.INFLECTED_FORM], b9[self.POS], b9[self.LEMMA])
                try:
                    b14 = (b9[self.INFLECTED_FORM], b9[self.POS], b9[self.b4])
                except IndexError as err:
                    print("Error! ", err)
                    print("Length", len(b9))
                    print(self.INFLECTED_FORM, self.b4)
                    print(b9[self.INFLECTED_FORM])
                set_pos_triplets_to_remove.add(b14)
                b11.add(b13)
        set_pos_triplets_to_remove.add(('chiens', 'nc', 'chiens'))
        b11.add(('résidente', 'nc', 'résident'))
        b11.add(('résidentes', 'nc', 'résident'))
        set_pos_triplets_to_remove.add(('traductrice', 'nc', 'traductrice'))
        b6 = (b6 - set_pos_triplets_to_remove) | b11
        b15 = {triplet[self.INFLECTED_FORM]: {triplet} for triplet in b6}
        self.b16 = b15
    def fonk3(self, b18):
        return b18 in ['a', 'n', 'r', 'v']
    def fonk4(self, sample_size):
        b17 = list(self.b16)
        return [self.b16[b17[i]] for i in random.sample(range(len(b17)), sample_size)]
    def fonk5(self, end):
        for index, element in enumerate(self.b16):
            print(element)
            if index >= end:
                break
    def fonk6(self, word, b18 = "n"):
        b19 = word.lower() if not b18 == "np" else word
        b20 = self.b16.get(b19, [])
        b21 = []
        if self.fonk3(b18):
            return next((triplet[self.LEMMA] for triplet in b20
                         if triplet[self.POS] in self.b5 and
                         self.b5[triplet[self.POS]] == b18), b19)
        for triplet in b20:
            b22 = (triplet[self.LEMMA], triplet[self.POS])
            if b22 not in b21:
                b21.append(b22)
        return b21 if b21 else (b19, 'np')
b23 = class1()
b24 = "chat"
b25 = "n"
b26 = b23.fonk6(b24, b25)
print(f"Lemmatized b26 for '{b24}' with POS '{b25}': {b26}")