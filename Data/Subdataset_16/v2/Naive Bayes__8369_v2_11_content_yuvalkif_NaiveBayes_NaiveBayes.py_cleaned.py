import pandas as pd
import numpy as np
import DataPreProcessing as dp
class class1:
    def fonk1(self, b5):
        self.a1 = 2
        self.b1 = {}
        self.b2 = {}
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
        self.fonk4(b7, list(self.b1.keys()))
        self.b6 = True
    def fonk3(self, b7):
        b8 = b7['class'].unique()
        self.b3 = b8
        b1 = {c: 0 for c in b8}
        for index, value in b7.iterrows():
            b1[value['class']] += 1
        return b1
    def fonk4(self, b7, class_values):
        b9 = []
        b10 = b7.columns[:-1]
        self.b4 = b10
        for col_name in b10:
            b11 = b7[col_name].unique()
            b9.append(1 / len(b11))
            b12 = {}
            for class_value in class_values:
                for value in b11:
                    b13 = f"{value}_{class_value}"
                    b12[b13] = sum((b7[col_name] == value) & (b7['class'] == class_value))
            self.b2[col_name] = b12
        self.a3 = b9
    def fonk5(self, b25, out_path):
        b14 = self.fonk6(b25)
        b15 = []
        for index, row in b14.iterrows():
            b16 = self.fonk7(row)
            b17 = self.fonk8(b16)
            b15.append(f"{index + 1} {b17}")
        self.fonk9(out_path, b15)
        return b15
    def fonk6(self, b25):
        b14 = pd.read_csv(b25)
        b14 = dp.fillDatasetNANumerical(b14)
        b14 = dp.fillDatasetNACategorical(b14)
        b14 = dp.discretizeDataset(b14, self.b5)
        return b14
    def fonk7(self, row):
        b16 = []
        for c in self.b3:
            b18 = []
            for attr_value, attr_name in zip(row, self.b4):
                b13 = f"{attr_value}_{c}"
                b19 = self.b2[attr_name].get(b13, 1 / self.a2)
                b20 = (b19 + self.a1 * self.a3[self.b4.index(attr_name)]) / (self.b1[c] + self.a1)
                b18.append(b20)
            b21 = self.b1[c] / self.a2
            for score in b18:
                b21 *= score
            b16.append(b21)
        return b16
    def fonk8(self, b16):
        b22 = max(b16)
        return self.b3[b16.index(b22)]
    def fonk9(self, path, b15):
        with open(path, 'w') as file:
            for result in b15:
                file.write(f"{result}\n")
if b23 = = "__main__":
    b24 = 'train.csv'
    b25 = 'test.csv'
    b26 = 'output.txt'
    b5 = 10
    b27 = pd.read_csv(b24)
    b28 = class1(b5)
    b28.fonk2(b27)
    b28.fonk5(b25, b26)