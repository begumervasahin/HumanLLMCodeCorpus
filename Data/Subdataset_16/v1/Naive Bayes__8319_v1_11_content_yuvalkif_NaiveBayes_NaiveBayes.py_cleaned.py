import pandas as pd
import numpy as np
import DataPreProcessing as dp
class class1:
    def fonk1(self, b5):
        self.a1 = 2
        self.b1 = dict()
        self.b2 = dict()
        self.a2 = 0
        self.b3 = []
        self.b4 = []
        self.a3 = 0
        self.b5 = b5
        self.b6 = False
    def fonk2(self, b7):
        self.a2 = b7.shape[0]
        self.b1 = self.fonk3(b7)
        b7 = dp.fillDatasetNANumerical(b7)
        b7 = dp.fillDatasetNACategorical(b7)
        b7 = dp.discretizeDataset(b7, self.b5)
        self.fonk4(b7 = b7, classvalues=list(self.b1.keys()))
        self.b6 = True
    def fonk3(self, b7):
        b8 = b7['class'].unique()
        self.b3 = b8
        b1 = dict()
        for b13 in b8:
            b1[b13] = 0
        for index, value in b7.iterrows():
            b1[value['class']] += 1
        return b1
    def fonk4(self, b7, classvalues):
        b9 = []
        b10 = list(b7)
        b10 = b10[0:len(b10)-1]
        self.b4 = b10
        for colname in b10:
            b11 = list(b7[colname].unique())
            b9.append(float(1 / len(b11)))
            b12 = dict()
            for classvalue in classvalues:
                for b13 in b11:
                    b13 = str(b13)
                    b12[b13 + '_' + str(classvalue)] = 0
                    for index, value in b7.iterrows():
                        if (value[colname] == b13) and (value['class'] == classvalue):
                            b12[b13 + '_' + classvalue] += 1
            self.b2[colname] = b12
        self.a3 = b9
        return b11
    def fonk5(self, b24, out_path):
        b14 = []
        b15 = self.fonk6(b24)
        for index, row in b15.iterrows():
            b16 = self.fonk7(row)
            b17 = self.fonk8(b16)
            b14.append(str(index + 1) + " " + b17)
        self.fonk9(out_path, b14)
        return b14
    def fonk6(self, b24):
        b15 = pd.read_csv(b24)
        b15 = dp.fillDatasetNANumerical(b15)
        b15 = dp.fillDatasetNACategorical(b15)
        b15 = dp.discretizeDataset(b15, self.b5)
        return b15
    def fonk7(self, row):
        b18 = []
        for b13 in self.b3:
            b19 = []
            a4 = 0
            for att_value, att_name in zip(row, self.b4):
                try:
                    b20 = float(
                        (self.b2[att_name][str(att_value) + '_' + str(b13)] + float(self.a1) * float(
                            self.a3[a4])) / (self.b1[b13] + self.a1))
                    a4 += 1
                    b19.append(b20)
                except KeyError:
                    b19.append(float(1 / self.a2))
            b21 = float(self.b1[b13]) / float(self.a2)
            for att_score in b19:
                b21 *= att_score
            b18.append(b21)
        return b18
    def fonk8(self, classes_scores):
        a5 = -1
        a6 = -1
        for i in range(len(classes_scores)):
            if a5 < classes_scores[i]:
                a5 = classes_scores[i]
                a6 = i
        return self.b3[a6]
    def fonk9(self, path, b14):
        with open(path, 'w') as f:
            f.writelines("%s\n" % row for row in b14)
if b22 = = "__main__":
    b23 = 'train.csv'
    b24 = 'test.csv'
    b25 = 'output.txt'
    b5 = 10
    b26 = pd.read_csv(b23)
    b27 = class1(b5)
    b27.fonk2(b26)
    b27.fonk5(b24, b25)