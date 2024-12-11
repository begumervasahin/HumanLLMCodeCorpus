import os
import csv
import collections
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
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
                    try:
                        self.b3[directory].append(float(row[1]))
                        self.b4[directory].append(row[0])
                    except Exception as e:
                        print(f"Error reading CSV file: {e}")
    def fonk5(self):
        return self.b2
    def fonk6(self):
        self.b5 = pd.DataFrame.from_dict(self.b3)
    def fonk7(self):
        self.b4 = collections.OrderedDict(sorted(self.b4.items(), key=lambda t: t[1]))
    def fonk8(self):
        self.fonk7()
        b8 = datestr2num(list(self.b4.b9()))
        self.b9 = zip(b8, list(self.b4.keys()))
    def fonk9(self):
        b10 = self.b5.corr(method='pearson')
        self.b6 = linkage(self.b5, 'average')
    def fonk10(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        b11 = list(self.b4.keys())
        dendrogram(self.b6, b12 = 90., leaf_font_size=8., labels=b11)
        plt.show()
b13 = class1(b1)
b13.fonk3()
b13.fonk4()
b13.fonk6()
b13.fonk8()
b13.fonk9()
b13.fonk10()