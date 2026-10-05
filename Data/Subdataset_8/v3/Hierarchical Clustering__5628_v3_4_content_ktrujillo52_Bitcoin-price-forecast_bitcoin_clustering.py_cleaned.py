import os
import csv
import collections
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
class DataProcessor:
    def __init__(self, pca_csv_path):
        self.pca_csv_path = pca_csv_path
        self.directories = []
        self.imports = {}
        self.exports = {}
        self.timeseries = None
        self.Z = None
    def get_data(self):
        return self.pca_csv_path
    def change_directory(self):
        os.chdir(self.pca_csv_path)
    def read_csv_files(self):
        self.directories = os.listdir(self.pca_csv_path)
        for directory in self.directories:
            with open(directory, "r") as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    self.imports.setdefault(directory, []).append(float(row[1]))
                    self.exports.setdefault(directory, []).append(row[0])
    def get_countries(self):
        return self.directories
    def create_timeseries(self):
        self.timeseries = pd.DataFrame.from_dict(self.imports)
    def sort_exports(self):
        sorted_exports = collections.OrderedDict(sorted(self.exports.items(), key=lambda t: t[1]))
        self.exports = sorted_exports
    def prepare_axes(self):
        self.sort_exports()
        importlist = datestr2num(list(self.exports.values()))
        self.values = zip(importlist, list(self.exports.keys()))
    def perform_clustering(self):
        correlation_matrix = self.timeseries.corr(method='pearson')
        self.Z = linkage(self.timeseries, 'average')
    def plot_dendrogram(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        country_labels = list(self.exports.keys())
        dendrogram(self.Z, leaf_rotation=90., leaf_font_size=8., labels=country_labels)
        plt.show()
pca_csv_path = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
data_processor = DataProcessor(pca_csv_path)
data_processor.change_directory()
data_processor.read_csv_files()
data_processor.create_timeseries()
data_processor.prepare_axes()
data_processor.perform_clustering()
data_processor.plot_dendrogram()