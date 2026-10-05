import os
import csv
import collections
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = None
        self.b6 = []
        self.b7 = {}
        self.b8 = None
        self.b9 = {}
        self.b10 = []
        self.b11 = []
        self.b12 = []
        self.b13 = []
        self.b14 = []
        self.b15 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        os.chdir(self.b1)
    def fonk4(self):
        self.b3 = os.listdir(self.b1)
        for item in self.b3:
            self.b2.append(item)
        for item in self.b2:
            with open(item, "r+") as f:
                self.b5 = csv.reader(f)
                for row in self.b5:
                    self.b4.append(row)
                f.close()
        return self.b4
    def fonk5(self):
        for item in self.b2:
            self.b6.append(item)
        return self.b6
    def fonk6(self):
        for i in self.b2:
            with open(i, "r+") as f:
                b16 = csv.reader(f)
                for row in b16:
                    try:
                        self.b7[i].append(float(row[1]))
                    except:
                        print("Error")
        self.b8 = pd.DataFrame.from_dict(self.b7)
        print("Timeseries:", str(self.b8))
    def fonk7(self):
        for i in self.b2:
            with open(i, "r+") as f:
                b16 = csv.reader(f)
                for row in b16:
                    try:
                        self.b9[i].append(row[0])
                    except:
                        print("Error")
        for key in self.b9:
            self.b10.append(key)
    def fonk8(self):
        b17 = collections.OrderedDict(sorted(self.b9.items(), key=lambda t: t[1]))
        b18 = collections.OrderedDict(sorted(self.b7.items(), key=lambda t: t[1]))
        for key, value in b17.items():
            self.b11.append(value)
            self.b13.append(key)
        for key,value in b18.items():
            self.b12.append(value)
        self.b11 = datestr2num(self.b11)
        self.b14 = zip(self.b11, self.b12)
        return self.b14
    def fonk9(self):
        b19 = self.b8.corr(method='pearson')
        self.b15 = linkage(self.b8, 'average')
    def fonk10(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        print(len(self.b13))
        dendrogram(self.b15, b20 = 90., leaf_font_size=8., labels=self.b13)
        plt.show()
b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
b4 = class1(b1)
b4.fonk3()
b4.fonk4()
b4.fonk5()
b4.fonk6()
b4.fonk7()
b4.fonk8()
b4.fonk9()
b4.fonk10()