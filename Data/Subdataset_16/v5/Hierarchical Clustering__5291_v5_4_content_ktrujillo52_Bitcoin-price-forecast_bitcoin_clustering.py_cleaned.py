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
        self.b3 = {}
        self.b4 = {}
        self.b5 = None
        self.b6 = None
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.b5 = pd.DataFrame.from_dict(self.b3)
    def fonk3(self):
        self.b2 = os.listdir(self.b1)
    def fonk4(self):
        self.b3 = {country: [] for country in self.b2}
        self.b4 = {country: [] for country in self.b2}
        for country in self.b2:
            b7 = os.path.join(self.b1, country)
            with open(b7, 'r') as file:
                b8 = csv.b8(file)
                for row in b8:
                    try:
                        self.b3[country].append(float(row[1]))
                        self.b4[country].append(row[0])
                    except ValueError:
                        print(f"Error processing row: {row} in file: {b7}")
    def fonk5(self):
        b9 = collections.OrderedDict(
            sorted(self.b4.items(), b10 = lambda t: t[1])
        )
        b11 = collections.OrderedDict(
            sorted(self.b3.items(), b10 = lambda t: t[1])
        )
        self.b12 = list(b9.keys())
        self.b13 = [datestr2num(value) for value in b9.values()]
        self.b14 = list(b11.values())
    def fonk6(self):
        b15 = self.b5.corr(method='pearson')
        self.b6 = linkage(self.b5, method='average')
    def fonk7(self):
        plt.figure(b16 = (10, 7))
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Country')
        plt.ylabel('Distance')
        dendrogram(
            self.b6,
            b17 = 90.,
            b18 = 8.,
            b19 = self.b12
        )
        plt.show()
def fonk8():
    b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
    b20 = class1(b1)
    b20.fonk2()
    b20.fonk5()
    b20.fonk6()
    b20.fonk7()
if b21 = = "__main__":
    fonk8()