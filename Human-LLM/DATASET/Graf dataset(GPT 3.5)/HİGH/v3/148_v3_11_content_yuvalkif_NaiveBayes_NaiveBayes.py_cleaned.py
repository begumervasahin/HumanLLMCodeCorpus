import pandas as pd
class class1:
    @staticmethod
    def fonk1(b9):
        return b9.fillna(b9.mean())
    @staticmethod
    def fonk2(b9):
        return b9.fillna(b9.mode().iloc[0])
    @staticmethod
    def fonk3(b9, b3):
        for col in b9.select_dtypes(b1 = ['number']):
            b9[col] = pd.cut(b9[col], b2 = b3, labels=False)
        return b9
class class2:
    def fonk4(self, b3):
        self.b3 = b3
        self.a1 = 2
        self.b4 = {}
        self.b5 = {}
        self.a2 = 0
        self.b6 = []
        self.b7 = []
        self.a3 = 0
        self.b8 = False
    def fonk5(self, b9):
        self.a2 = b9.shape[0]
        self.b4 = self.fonk6(b9)
        b9 = class1.fonk1(b9)
        b9 = class1.fonk2(b9)
        b9 = class1.fonk3(b9, self.b3)
        self.fonk7(b9)
        self.b8 = True
    def fonk6(self, b9):
        b10 = b9['class'].value_counts().to_dict()
        self.b6 = list(b10.keys())
        return b10
    def fonk7(self, b9):
        b11 = []
        b12 = b9.columns[:-1]
        self.b7 = b12
        for col_name in b12:
            b13 = b9[col_name].unique()
            b11.append(1 / len(b13))
            b14 = {}
            for class_value in self.b6:
                for b15 in b13:
                    b15 = str(b15)
                    b16 = b9[(b9['class'] == class_value) & (b9[col_name] == b15)].shape[0]
                    b14[f'{b15}_{class_value}'] = b16
            self.b5[col_name] = b14
        self.a3 = b11
    def fonk8(self, test_file, out_path):
        b17 = []
        b18 = self.fonk9(test_file)
        for index, row in b18.iterrows():
            b19 = self.fonk10(row)
            b20 = self.fonk11(b19)
            b17.append(f"{index+1} {b20}")
        self.fonk12(out_path, b17)
        return b17
    def fonk9(self, test_file):
        b18 = pd.read_csv(test_file)
        b18 = class1.fonk1(b18)
        b18 = class1.fonk2(b18)
        b18 = class1.fonk3(b18, self.b3)
        return b18
    def fonk10(self, row):
        b21 = []
        for c in self.b6:
            b22 = []
            for att_value, att_name in zip(row, self.b7):
                try:
                    b23 = self.b5[att_name][f'{att_value}_{c}'] + self.a1 * self.a3[k]
                    b24 = self.b4[c] + self.a1
                    b25 = b23 / b24
                    b22.append(b25)
                except KeyError:
                    b22.append(1 / self.a2)
            b26 = self.b4[c] / self.a2
            for att_score in b22:
                b26 *= att_score
            b21.append(b26)
        return b21
    def fonk11(self, classes_scores):
        b27 = max(classes_scores)
        b28 = classes_scores.index(b27)
        return self.b6[b28]
    @staticmethod
    def fonk12(path, b17):
        with open(path, 'w') as f:
            f.write('\n'.join(b17))
if b29 = = "__main__":
    b30 = class2(b3=5)
    b31 = pd.read_csv("b31.csv")
    b30.fonk5(b31)
    b32 = b30.fonk8("test_dataset.csv", "output.txt")
    print("Predictions written to output.txt")