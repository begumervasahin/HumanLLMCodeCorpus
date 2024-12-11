import pandas as pd
import re
class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, structure_file, df, num_of_intervals):
        b2 = self.fonk4(structure_file)
        b3 = self.fonk5(df, b2)
        b4 = self.fonk8(b2, b3, num_of_intervals)
        return b4
    def fonk3(self, structure_file, df):
        b2 = self.fonk4(structure_file)
        b3 = self.fonk5(df, b2)
        b4 = self.fonk9(self.b1, b3)
        return b4
    def fonk4(self, structure_file):
        b2 = {}
        for line in structure_file:
            b5 = re.split('\s', line)
            if b5[2] == "NUMERIC":
                b6 = "N"
            else:
                b6 = "C"
            b2[b5[1]] = b6
        return b2
    def fonk5(self, df, b2):
        for key in b2:
            if b2[key] == "N":
                df[key].fillna(df.groupby("class")[key].transform("mean"), b7 = True)
        for key in b2:
            if b2[key] == "C":
                df[key] = df[key].fillna(df[key].mode()[0])
        return df
    def fonk6(self, col, num_bins, key):
        b8 = col.min()
        b9 = col.max()
        b10 = []
        b11 = (b9 - b8) / num_bins
        for i in range(0, num_bins-1):
            if (b8 + (i+1)*b11) != b8 and (b8 + (i+1)*b11) != b9:
                b10.append(b8 + (i+1)*b11)
        b12 = [b8] + b10 + [b9]
        b13 = range(len(b10) + 1)
        b14 = [b12, b13]
        self.b1[key] = b14
        b15 = pd.cut(col, bins=b12, b13=b13, include_lowest=True)
        return b15
    def fonk7(self, col, b12, b13):
        b15 = pd.cut(col, bins=b12, b13=b13, include_lowest=True)
        return b15
    def fonk8(self, b2, df, num_of_intervals):
        for key in b2:
            if b2[key] == "N":
                df[key] = self.fonk6(df[key], num_of_intervals, key)
        return df
    def fonk9(self, b1, df):
        for key in b1:
            df[key] = self.fonk7(df[key], b1[key][0], b1[key][1])
        return df