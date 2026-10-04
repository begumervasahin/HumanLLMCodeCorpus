import os
import csv
import collections
from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = {}
        self.b6 = {}
        self.b7 = None
        self.b8 = None
    def fonk2(self):
        self.b2 = os.listdir(self.b1)
        self.b4 = [item for item in self.b2]
    def fonk3(self):
        self.b5 = {country: [] for country in self.b4}
        self.b6 = {country: [] for country in self.b4}
        for country in self.b4:
            b9 = os.path.join(self.b1, country)
            with open(b9, 'r') as f:
                b10 = csv.b10(f)
                for row in b10:
                    try:
                        self.b5[country].append(float(row[1]))
                        self.b6[country].append(row[0])
                    except ValueError:
                        print(f"Error processing row: {row}")
        self.b7 = pd.DataFrame.from_dict(self.b5)
    def fonk4(self):
        b11 = collections.OrderedDict(
            sorted(self.b6.items(), b12 = lambda t: t[1])
        )
        b13 = collections.OrderedDict(
            sorted(self.b5.items(), b12 = lambda t: t[1])
        )
        self.b14 = [datestr2num(value) for value in b11.values()]
        self.b15 = [value for value in b13.values()]
        self.b16 = list(b11.keys())
    def fonk5(self):
        b17 = self.b7.corr(method='pearson')
        self.b8 = linkage(self.b7, method='average')
    def fonk6(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Country')
        plt.ylabel('Distance')
        dendrogram(self.b8, b18 = 90., leaf_font_size=8., labels=self.b16)
        plt.show()
def fonk7():
    b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
    b19 = class1(b1)
    b19.fonk2()
    b19.fonk3()
    b19.fonk4()
    b19.fonk5()
    b19.fonk6()
if b20 = = "__main__":
    fonk7()