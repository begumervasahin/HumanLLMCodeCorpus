import pandas as pd
import numpy as np
class class1:
    @staticmethod
    def fonk1(b9):
        return b9.fillna(b9.mean())
    @staticmethod
    def fonk2(b9):
        return b9.fillna(b9.mode().iloc[0])
    @staticmethod
    def fonk3(b9, b7):
        for col in b9.select_dtypes(b1 = ['number']):
            b9[col] = pd.cut(b9[col], b2 = b7, labels=False)
        return b9
class class2:
    def fonk4(self, b7):
        self.a1 = 2
        self.b3 = dict()
        self.b4 = dict()
        self.a2 = 0
        self.b5 = []
        self.b6 = []
        self.a3 = 0
        self.b7 = b7
        self.b8 = False
    def fonk5(self, b9):
        self.a2 = b9.shape[0]
        self.b3 = self.fonk6(b9)
        b9 = class1.fonk1(b9)
        b9 = class1.fonk2(b9)
        b9 = class1.fonk3(b9, self.b7)
        self.fonk7(b9 = b9, classvalues=list(self.b3.keys()))
        self.b8 = True
    def fonk6(self, b9):
        b10 = b9['class'].unique()
        self.b5 = b10
        b3 = dict()
        for b15 in b10:
            b3[b15] = 0
        for index, value in b9.iterrows():
            b3[value['class']] += 1
        return b3
    def fonk7(self, b9, classvalues):
        b11 = []
        b12 = list(b9)
        b12 = b12[0:len(b12)-1]
        self.b6 = b12
        for colname in b12:
            b13 = list(b9[colname].unique())
            b11.append(float(1/len(b13)))
            b14 = dict()
            for classvalue in classvalues:
                for b15 in b13:
                    b15 = str(b15)
                    b14[b15+'_'+str(classvalue)] = 0
                    for index,value in b9.iterrows():
                        if((value[colname] == b15) and (value['class'] == classvalue)):
                            b14[b15+'_'+classvalue] += 1
            self.b4[colname] = b14
        self.a3 = b11
        return b13
    def fonk8(self, test_file, out_path):
        b16 = []
        b17 = pd.read_csv(test_file)
        b17 = self.fonk9(b17)
        for index, row in b17.iterrows():
            b18 = self.fonk10(row)
            b19 = self.fonk11(b18)
            b16.append(str(index+1) + " " + b19)
        self.fonk12(out_path, b16)
        return b16
    def fonk9(self, test_file):
        b17 = pd.read_csv(test_file)
        b17 = class1.fonk1(b17)
        b17 = class1.fonk2(b17)
        b17 = class1.fonk3(b17, self.b7)
        return b17
    def fonk10(self, row):
        b20 = []
        for b15 in self.b5:
            b21 = []
            a4 = 0
            for att_value, att_name in zip(row, self.b6):
                try:
                    b22 = float((self.b4[att_name][str(att_value)+'_'+str(b15)] + float(self.a1)*float(self.a3[a4])) / (self.b3[b15]+self.a1))
                    a4 += 1
                    b21.append(b22)
                except KeyError:
                    b21.append(float(1/self.a2))
            b23 = float(self.b3[b15]) / float(self.a2)
            for att_score in b21:
                b23 = b23 * att_score
            b20.append(b23)
        return b20
    def fonk11(self, classes_scores):
        a5 = -1
        a6 = -1
        for i in range(0, len(classes_scores)):
            if a5 < classes_scores[i]:
                a5 = classes_scores[i]
                a6 = i
        return self.b5[a6]
    def fonk12(self, path, b16):
        with open(path, 'w') as f:
            f.writelines("%s\n" % row for row in b16)
if b24 = = "__main__":
    b25 = class2(b7=5)
    b26 = pd.read_csv("b26.csv")
    b25.fonk5(b26)
    b27 = b25.fonk8("test_dataset.csv", "output.txt")
    print("Predictions written to output.txt")