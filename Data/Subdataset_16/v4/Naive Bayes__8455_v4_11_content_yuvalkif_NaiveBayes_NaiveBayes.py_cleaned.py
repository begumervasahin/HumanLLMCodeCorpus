import csv
import pandas as pd
import numpy as np
import DataPreProcessing as dp
class class1:
    def fonk1(self, b6):
        self.a1 = 2
        self.b1 = {}
        self.b2 = {}
        self.a2 = 0
        self.b3 = []
        self.b4 = []
        self.b5 = []
        self.b6 = b6
        self.b7 = False
    def fonk2(self, b8):
        self.a2 = b8.shape[0]
        self.b1 = self.fonk3(b8)
        b8 = dp.fillDatasetNANumerical(b8)
        b8 = dp.fillDatasetNACategorical(b8)
        b8 = dp.discretizeDataset(b8, self.b6)
        self.fonk4(b8, list(self.b1.keys()))
        self.b7 = True
    def fonk3(self, b8):
        b9 = b8['class'].unique()
        self.b3 = b9
        b1 = {c: 0 for c in b9}
        for _, row in b8.iterrows():
            b1[row['class']] += 1
        return b1
    def fonk4(self, b8, class_values):
        b10 = b8.b32[:-1]
        self.b4 = b10
        b11 = []
        for colname in b10:
            b12 = b8[colname].unique()
            b11.append(1 / len(b12))
            b13 = {f"{v}_{c}": 0 for c in class_values for v in b12}
            for _, row in b8.iterrows():
                b14 = f"{row[colname]}_{row['class']}"
                b13[b14] += 1
            self.b2[colname] = b13
        self.b5 = b11
    def fonk5(self, test_file, out_path):
        b15 = self.fonk6(test_file)
        b16 = []
        for index, row in b15.iterrows():
            b17 = self.fonk7(row)
            b18 = self.fonk8(b17)
            b16.append(f"{index + 1} {b18}")
        self.fonk9(out_path, b16)
        return b16
    def fonk6(self, test_file):
        b19 = pd.read_csv(test_file)
        b19 = dp.fillDatasetNANumerical(b19)
        b19 = dp.fillDatasetNACategorical(b19)
        b19 = dp.discretizeDataset(b19, self.b6)
        return b19
    def fonk7(self, row):
        b17 = []
        for c in self.b3:
            b20 = []
            for k, (att_value, att_name) in enumerate(zip(row, self.b4)):
                b14 = f"{att_value}_{c}"
                b21 = (self.b2[att_name].get(b14, 0) + self.a1 * self.b5[k]) / (self.b1[c] + self.a1)
                b20.append(b21)
            b22 = self.b1[c] / self.a2
            for score in b20:
                b22 *= score
            b17.append(b22)
        return b17
    def fonk8(self, b17):
        return self.b3[np.argmax(b17)]
    def fonk9(self, path, b16):
        with open(path, 'w') as file:
            for prediction in b16:
                file.write(f"{prediction}\n")
if b23 = = "__main__":
    b24 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b25 = './cnews/cnews.vocab.txt'
    b26 = './cnews/cnews.train.txt'
    b27 = './cnews/cnews.test.txt'
    b28 = class1(b6=10)
    raw_features, b29 = dp.loadDataSet(b26, b25)
    b30 = b28.create_unique_set(raw_features)
    b31 = [b28.words_to_vec(b30, features) for features in raw_features]
    b28.fonk2(pd.DataFrame(b31, b32 = b30).assign(class=b29))
    b16 = b28.fonk5(b27, 'output.txt')
    np.save('models/pos.npy', np.array(b28.b5))
    with open('models/b30.txt', 'w') as file:
        for word in b30:
            file.write(f"{word}\n")
    np.save('models/p_vectors.npy', np.array(b28.b2))