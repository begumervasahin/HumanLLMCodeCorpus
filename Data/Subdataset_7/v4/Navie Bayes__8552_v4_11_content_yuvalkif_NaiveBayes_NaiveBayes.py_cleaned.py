import csv
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
        b7 = dp.fill_dataset_na_numerical(b7)
        b7 = dp.fill_dataset_na_categorical(b7)
        b7 = dp.discretize_dataset(b7, self.b5)
        self.fonk4(b7 = b7, class_values=list(self.b1.keys()))
        self.b6 = True
    def fonk3(self, b7):
        b8 = b7['class'].unique()
        self.b3 = b8
        b1 = {b13: 0 for b13 in b8}
        for _, value in b7.iterrows():
            b1[value['class']] += 1
        return b1
    def fonk4(self, b7, class_values):
        b9 = []
        b10 = list(b7)[:-1]
        self.b4 = b10
        for col_name in b10:
            b11 = list(b7[col_name].unique())
            b9.append(1 / len(b11))
            b12 = {str(b13) + '_' + str(class_value): 0 for class_value in class_values for b13 in b11}
            for _, value in b7.iterrows():
                for b13 in b11:
                    b13 = str(b13)
                    if (value[col_name] == b13) and (value['class'] in class_values):
                        b12[b13 + '_' + str(value['class'])] += 1
            self.b2[col_name] = b12
        self.a3 = b9
    def fonk5(self, test_file, out_path):
        b14 = []
        b15 = self.fonk6(test_file)
        for index, row in b15.iterrows():
            b16 = self.fonk7(row)
            b17 = self.fonk8(b16)
            b14.append(str(index + 1) + " " + b17)
        self.fonk9(out_path, b14)
        return b14
    def fonk6(self, test_file):
        b15 = pd.read_csv(test_file)
        b15 = dp.fill_dataset_na_numerical(b15)
        b15 = dp.fill_dataset_na_categorical(b15)
        b15 = dp.discretize_dataset(b15, self.b5)
        return b15
    def fonk7(self, row):
        b18 = []
        for b13 in self.b3:
            b19 = []
            a4 = 0
            for att_value, att_name in zip(row, self.b4):
                try:
                    b20 = (self.b2[att_name][str(att_value) + '_' + str(b13)] +
                                        float(self.a1) * float(self.a3[a4])) / \
                                       (self.b1[b13] + self.a1)
                    a4 += 1
                    b19.append(b20)
                except KeyError:
                    b19.append(1 / self.a2)
            b21 = self.b1[b13] / self.a2
            for att_score in b19:
                b21 *= att_score
            b18.append(b21)
        return b18
    def fonk8(self, classes_scores):
        a5 = -1
        a6 = -1
        for i, score in enumerate(classes_scores):
            if a5 < score:
                a5 = score
                a6 = i
        return self.b3[a6]
    def fonk9(self, path, b14):
        with open(path, 'w') as f:
            f.writelines("%s\n" % row for row in b14)