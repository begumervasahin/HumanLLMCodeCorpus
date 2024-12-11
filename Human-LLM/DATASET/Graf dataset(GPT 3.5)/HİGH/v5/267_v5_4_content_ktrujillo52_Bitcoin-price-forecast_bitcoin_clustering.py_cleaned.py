import os
import csv
import collections
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = []
        self.b4 = {}
        self.b5 = {}
        self.b6 = None
        self.b7 = None
    def fonk2(self):
        return self.b2
    def fonk3(self):
        os.chdir(self.b2)
    def fonk4(self):
        self.b3 = os.listdir(self.b2)
        for directory in self.b3:
            with open(directory, "r") as file:
                b8 = csv.reader(file)
                for row in b8:
                    try:
                        self.b4.setdefault(directory, []).append(float(row[1]))
                        self.b5.setdefault(directory, []).append(row[0])
                    except Exception as e:
                        print(f"Error reading CSV file: {e}")
    def fonk5(self):
        return self.b3
    def fonk6(self):
        self.b6 = pd.DataFrame.from_dict(self.b4)
    def fonk7(self):
        self.b5 = collections.OrderedDict(sorted(self.b5.items(), key=lambda t: t[1]))
    def fonk8(self):
        self.fonk7()
        b9 = datestr2num(list(self.b5.b10()))
        self.b10 = zip(b9, list(self.b5.keys()))
    def fonk9(self):
        b11 = self.b6.corr(method='pearson')
        self.b7 = linkage(self.b6, 'average')
    def fonk10(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        b12 = list(self.b5.keys())
        dendrogram(self.b7, b13 = 90., leaf_font_size=8., labels=b12)
        plt.show()
b14 = class1(b1)
b14.fonk3()
b14.fonk4()
b14.fonk6()
b14.fonk8()
b14.fonk9()
b14.fonk10()