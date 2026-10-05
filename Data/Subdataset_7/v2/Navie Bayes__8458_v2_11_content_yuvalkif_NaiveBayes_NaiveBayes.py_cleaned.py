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
        self.fonk7(b9 = b9, class_values=list(self.b3.keys()))
        self.b8 = True
    def fonk6(self, b9):
        b10 = b9['class'].unique()
        self.b5 = b10
        b3 = {c: 0 for c in b10}
        for _, value in b9.iterrows():
            b3[value['class']] += 1
        return b3
    def fonk7(self, b9, class_values):
        b11 = []
        b12 = list(b9)
        b12 = b12[:-1]
        self.b6 = b12
        for col_name in b12:
            b13 = list(b9[col_name].unique())
            b11.append(1 / len(b13))
            b14 = {f'{c}_{str(b15)}': 0 for c in class_values for b15 in b13}
            for class_value in class_values:
                for b15 in b13:
                    b15 = str(b15)
                    for _, value in b9.iterrows():
                        if value[col_name] == b15 and value['class'] == class_value:
                            b14[f'{b15}_{class_value}'] += 1
            self.b4[col_name] = b14
        self.a3 = b11
    def fonk8(self, test_file, out_path):
        b16 = []
        b17 = pd.read_csv(test_file)
        b17 = self.fonk9(b17)
        for index, row in b17.iterrows():
            b18 = self.fonk10(row)
            b19 = self.fonk11(b18)
            b16.append(f"{index+1} {b19}")
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
        for c in self.b5:
            b21 = []
            a4 = 0
            for att_value, att_name in zip(row, self.b6):
                try:
                    b22 = (self.b4[att_name][f'{att_value}_{c}'] + self.a1 * self.a3[a4]) / (self.b3[c] + self.a1)
                    a4 += 1
                    b21.append(b22)
                except KeyError:
                    b21.append(1 / self.a2)
            b23 = self.b3[c] / self.a2
            for att_score in b21:
                b23 *= att_score
            b20.append(b23)
        return b20
    def fonk11(self, classes_scores):
        b24 = max(classes_scores)
        b25 = classes_scores.index(b24)
        return self.b5[b25]
    @staticmethod
    def fonk12(path, b16):
        with open(path, 'w') as f:
            f.write('\n'.join(b16))
if b26 = = "__main__":
    b27 = class2(b7=5)
    b28 = pd.read_csv("b28.csv")
    b27.fonk5(b28)
    b29 = b27.fonk8("test_dataset.csv", "output.txt")
    print("Predictions written to output.txt")