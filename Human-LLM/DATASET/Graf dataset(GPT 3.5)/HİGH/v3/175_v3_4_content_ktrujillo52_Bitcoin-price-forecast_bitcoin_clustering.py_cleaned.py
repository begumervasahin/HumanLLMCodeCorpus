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
        self.b3 = {}
        self.b4 = {}
        self.b5 = None
        self.b6 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        os.chdir(self.b1)
    def fonk4(self):
        self.b2 = os.listdir(self.b1)
        for directory in self.b2:
            with open(directory, "r") as file:
                b7 = csv.reader(file)
                for row in b7:
                    self.b3.setdefault(directory, []).append(float(row[1]))
                    self.b4.setdefault(directory, []).append(row[0])
    def fonk5(self):
        return self.b2
    def fonk6(self):
        self.b5 = pd.DataFrame.from_dict(self.b3)
    def fonk7(self):
        b8 = collections.OrderedDict(sorted(self.b4.items(), key=lambda t: t[1]))
        self.b4 = b8
    def fonk8(self):
        self.fonk7()
        b9 = datestr2num(list(self.b4.b10()))
        self.b10 = zip(b9, list(self.b4.keys()))
    def fonk9(self):
        b11 = self.b5.corr(method='pearson')
        self.b6 = linkage(self.b5, 'average')
    def fonk10(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        b12 = list(self.b4.keys())
        dendrogram(self.b6, b13 = 90., leaf_font_size=8., labels=b12)
        plt.show()
b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
b14 = class1(b1)
b14.fonk3()
b14.fonk4()
b14.fonk6()
b14.fonk8()
b14.fonk9()
b14.fonk10()