import os
import csv
import collections
from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
import pandas as pd
class DataProcessor:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.directories = []
        self.data = []
        self.countries = []
        self.imports_dict = {}
        self.exports_dict = {}
        self.timeseries = None
        self.Z = None
    def load_data(self):
        self.directories = os.listdir(self.data_dir)
        self.countries = [item for item in self.directories]
    def process_csv_files(self):
        self.imports_dict = {country: [] for country in self.countries}
        self.exports_dict = {country: [] for country in self.countries}
        for country in self.countries:
            file_path = os.path.join(self.data_dir, country)
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        self.imports_dict[country].append(float(row[1]))
                        self.exports_dict[country].append(row[0])
                    except ValueError:
                        print(f"Error processing row: {row}")
        self.timeseries = pd.DataFrame.from_dict(self.imports_dict)
    def sort_axes(self):
        sorted_imports = collections.OrderedDict(
            sorted(self.exports_dict.items(), key=lambda t: t[1])
        )
        sorted_exports = collections.OrderedDict(
            sorted(self.imports_dict.items(), key=lambda t: t[1])
        )
        self.importlist = [datestr2num(value) for value in sorted_imports.values()]
        self.exportlist = [value for value in sorted_exports.values()]
        self.sorted_countries = list(sorted_imports.keys())
    def perform_clustering(self):
        correlation_matrix = self.timeseries.corr(method='pearson')
        self.Z = linkage(self.timeseries, method='average')
    def plot_dendrogram(self):
        plt.figure()
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Country')
        plt.ylabel('Distance')
        dendrogram(self.Z, leaf_rotation=90., leaf_font_size=8., labels=self.sorted_countries)
        plt.show()
def main():
    data_dir = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
    data_processor = DataProcessor(data_dir)
    data_processor.load_data()
    data_processor.process_csv_files()
    data_processor.sort_axes()
    data_processor.perform_clustering()
    data_processor.plot_dendrogram()
if __name__ == "__main__":
    main()