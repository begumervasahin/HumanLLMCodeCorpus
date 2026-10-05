from matplotlib import pyplot as plt
from matplotlib.dates import datestr2num
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist
import pandas as pd
import numpy as np
import os
import csv
import collections
b1 = "/home/kevin/Desktop/Bitcoin/simulations/MCHMC/24hour/5_16_17/pca_csv/"
class class1:
	def fonk1(self):
		print "test"
		self.b2 = b1
		return self.b2
	def fonk2(self):
		os.chdir(self.b2)
	def fonk3(self):
		self.b3 = []
		self.b4 = os.listdir(self.b2)
		for item in self.b4:
			self.b3.append(item)
		self.b5 = []
		for item in self.b3:
			with open(item, "r+") as f:
				self.b6 = csv.reader(f)
				for row in self.b6:
					self.b5.append(row)
				f.close()
		return self.b5
	def fonk4(self):
		self.b7 = []
		for item in self.b3:
			self.b7.append(item)
		return self.b7
	def fonk5(self):
		self.b8 = {key : [] for key in self.b7}
		for i in self.b3:
			with open(i, "r+") as f:
				b9 = csv.reader(f)
				for row in b9:
					try:
						self.b8[i].append(float(row[1]))
					except:
						print "Error"
		self.b10 = pd.DataFrame.from_dict(self.b8)
		print "Timeseries:"+str(self.b10)
	def fonk6(self):
		self.b11 = {key : []  for key in self.b7}
		for i in self.b3:
			with open(i, "r+") as f:
				b9 = csv.reader(f)
				for row in b9:
					try:
						self.b11[i].append(row[0])
					except:
						print "Error"
		self.b12 = []
		for key in self.b11:
			self.b12.append(key)
	def fonk7(self):
		b13 = collections.OrderedDict(sorted(self.b11.items(), key=lambda t: t[1]))
		b14 = collections.OrderedDict(sorted(self.b8.items(), key=lambda t: t[1]))
		self.b15 = []
		self.b16 = []
		self.b17 = []
		for key, value in b13.items():
			self.b15.append(value)
			self.b17.append(key)
		for key,value in b14.items():
			self.b16.append(value)
		self.b15 = datestr2num(self.b15)
		self.b18 = zip(self.b15, self.b16)
		return self.b18
	def fonk8(self):
		b19 = self.b10.corr(method = 'pearson')
		self.b20 = linkage(self.b10, 'average')
	def fonk9(self):
		plt.figure()
		plt.title('Hierarchical Clustering Dendrogram')
		plt.xlabel('sample index')
		plt.ylabel('distance')
		print len(self.b17)
		fonk9(self.b20, b21 = 90., leaf_font_size= 8., labels = self.b17)
		plt.show()
b5 = class1()
b22 = b5.fonk1()
b23 = b5.fonk2()
b24 = b5.fonk3()
b25 = b5.fonk4()
b26 = b5.fonk5()
b27 = b5.fonk6()
b28 = b5.fonk7()
b29 = b5.fonk8()
b30 = b5.fonk9()