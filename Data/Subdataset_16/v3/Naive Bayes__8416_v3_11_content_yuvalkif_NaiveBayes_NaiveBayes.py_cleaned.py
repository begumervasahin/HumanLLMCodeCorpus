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
        self.fonk4(b7)
        self.b6 = True
    def fonk3(self, b7):
        b1 = b7['class'].value_counts().to_dict()
        self.b3 = list(b1.keys())
        return b1
    def fonk4(self, b7):
        b8 = b7.columns[:-1]
        self.b4 = b8
        self.a3 = []
        for col_name in b8:
            b9 = b7[col_name].unique()
            self.a3.append(1 / len(b9))
            b10 = {}
            for class_value in self.b3:
                for value in b9:
                    b11 = f"{value}_{class_value}"
                    b12 = sum((b7[col_name] == value) & (b7['class'] == class_value))
                    b10[b11] = b12
            self.b2[col_name] = b10
    def fonk5(self, b24, out_path):
        b13 = self.fonk6(b24)
        b14 = []
        for index, row in b13.iterrows():
            b15 = self.fonk7(row)
            b16 = self.fonk8(b15)
            b14.append(f"{index + 1} {b16}")
        self.fonk9(out_path, b14)
        return b14
    def fonk6(self, b24):
        b13 = pd.read_csv(b24)
        b13 = dp.fillDatasetNANumerical(b13)
        b13 = dp.fillDatasetNACategorical(b13)
        b13 = dp.discretizeDataset(b13, self.b5)
        return b13
    def fonk7(self, row):
        b15 = []
        for class_label in self.b3:
            b17 = []
            for attr_value, attr_name in zip(row, self.b4):
                b11 = f"{attr_value}_{class_label}"
                b18 = self.b2[attr_name].get(b11, 1 / self.a2)
                b19 = (b18 + self.a1 * self.a3[self.b4.index(attr_name)]) / (self.b1[class_label] + self.a1)
                b17.append(b19)
            b20 = self.b1[class_label] / self.a2
            for score in b17:
                b20 *= score
            b15.append(b20)
        return b15
    def fonk8(self, b15):
        b21 = max(b15)
        return self.b3[b15.index(b21)]
    def fonk9(self, path, b14):
        with open(path, 'w') as file:
            for result in b14:
                file.write(f"{result}\n")
if b22 = = "__main__":
    b23 = 'train.csv'
    b24 = 'test.csv'
    b25 = 'output.txt'
    b5 = 10
    b26 = pd.read_csv(b23)
    b27 = class1(b5)
    b27.fonk2(b26)
    b27.fonk5(b24, b25)