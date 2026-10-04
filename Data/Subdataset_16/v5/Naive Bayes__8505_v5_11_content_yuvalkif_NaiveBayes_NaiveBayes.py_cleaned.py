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
        b1 = b8['class'].value_counts().to_dict()
        self.b3 = list(b1.keys())
        return b1
    def fonk4(self, b8, class_values):
        b9 = b8.columns[:-1]
        self.b4 = b9
        b10 = []
        for colname in b9:
            b11 = b8[colname].unique()
            b10.append(1 / len(b11))
            b12 = {f"{v}_{c}": 0 for c in class_values for v in b11}
            for _, row in b8.iterrows():
                b13 = f"{row[colname]}_{row['class']}"
                b12[b13] += 1
            self.b2[colname] = b12
        self.b5 = b10
    def fonk5(self, test_file, out_path):
        b14 = self.fonk6(test_file)
        b15 = []
        for index, row in b14.iterrows():
            b16 = self.fonk7(row)
            b17 = self.fonk8(b16)
            b15.append(f"{index + 1} {b17}")
        self.fonk9(out_path, b15)
        return b15
    def fonk6(self, test_file):
        b18 = pd.read_csv(test_file)
        b18 = dp.fillDatasetNANumerical(b18)
        b18 = dp.fillDatasetNACategorical(b18)
        b18 = dp.discretizeDataset(b18, self.b6)
        return b18
    def fonk7(self, row):
        b16 = []
        for c in self.b3:
            b19 = []
            for k, (att_value, att_name) in enumerate(zip(row, self.b4)):
                b13 = f"{att_value}_{c}"
                b20 = (self.b2[att_name].get(b13, 0) + self.a1 * self.b5[k]) / (self.b1[c] + self.a1)
                b19.append(b20)
            b21 = self.b1[c] / self.a2
            for score in b19:
                b21 *= score
            b16.append(b21)
        return b16
    def fonk8(self, b16):
        return self.b3[np.argmax(b16)]
    def fonk9(self, path, b15):
        with open(path, 'w') as file:
            for prediction in b15:
                file.write(f"{prediction}\n")
def fonk10():
    b22 = ['Sport', 'Entertainment', 'Household', 'House Property', 'Education', 'Fashion', 'Current Politics', 'Game', 'Science and Technology', 'Finance']
    b23 = './cnews/cnews.vocab.txt'
    b24 = './cnews/cnews.train.txt'
    b25 = './cnews/cnews.test.txt'
    b26 = class1(b6=10)
    raw_features, b27 = dp.loadDataSet(b24, b23)
    b28 = b26.create_unique_set(raw_features)
    b29 = [b26.words_to_vec(b28, features) for features in raw_features]
    b30 = pd.DataFrame(b29, columns=b28).assign(class=b27)
    b26.fonk2(b30)
    b15 = b26.fonk5(b25, 'output.txt')
    np.save('models/pos.npy', np.array(b26.b5))
    with open('models/b28.txt', 'w') as file:
        for word in b28:
            file.write(f"{word}\n")
    np.save('models/p_vectors.npy', np.array(b26.b2))
    print("Model training completed and parameters saved.")
if b31 = = "__main__":
    fonk10()