from pathlib import Path
from preprocess_data import split_into_sentences
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = self.fonk2(open(b2))
    def fonk2(self, f):
        b3 = []
        for sentence in split_into_sentences(f.readlines()):
            b4 = []
            for line in sentence:
                if line and not line.startswith('
                    b5 = line.split('\t')
                    assert len(b5) == 10
                    b6 = b5[1].replace(' ', '')
                    b7 = b5[2].replace(' ', '')
                    b8 = b5[9] != 'SpaceAfter=No'
                    b4.append(class2(b6, b7, b5[3], b8))
            b3.append(class3(b4))
        return b3
    def fonk3(self):
        return sum(b10.fonk9() for b10 in self.b3)
class class2:
    def fonk4(self, b6, b7, b9, b8):
        self.b6 = b6
        self.b7 = b7
        self.b9 = b9
        self.b8 = b8
class class3:
    def fonk5(self, b4):
        self.b4 = b4
    def fonk6(self):
        b10 = []
        for t in self.b4:
            b10.append(t.b6)
            if t.b8:
                b10.append(' ')
        return ''.join(b10).rstrip(' ')
    def fonk7(self):
        return [t.b7 for t in self.b4]
    def fonk8(self):
        return [t.b9 for t in self.b4]
    def fonk9(self):
        return len(self.b4)
def fonk10(testset_name):
    return {
        'UD_Finnish_TDT': Path('data/preprocessed/UD_Finnish-TDT/fi_tdt-ud-test.conllu'),
        'ftb1u': Path('data/preprocessed/ftb1/ftb1u_sample.tsv'),
        'ftb2-news': Path('data/preprocessed/ftb2/FinnTreeBank_2/news-samples_tab.txt'),
        'ftb2-sofie': Path('data/preprocessed/ftb2/FinnTreeBank_2/sofie12_tab.txt'),
        'ftb2-wikipedia': Path('data/preprocessed/ftb2/FinnTreeBank_2/wikipedia-samples_tab.txt'),
    }.get(testset_name)
b11 = [
    class1('UD_Finnish_TDT', fonk10('UD_Finnish_TDT')),
    class1('ftb1u', fonk10('ftb1u')),
    class1('ftb2-news', fonk10('ftb2-news')),
    class1('ftb2-sofie', fonk10('ftb2-sofie')),
    class1('ftb2-wikipedia', fonk10('ftb2-wikipedia'))
]
for dataset in b11:
    print(f"class1: {dataset.b1}")
    print(f"Number of b3: {len(dataset.b3)}")
    print(f"Number of b4: {dataset.fonk9()}")
    print()