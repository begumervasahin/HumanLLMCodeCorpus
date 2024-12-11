import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.pyplot import cm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import os
import glob
plt.close('all')
b1 = "DATA_001_House"
b2 = "data1_filtered_wifis/"+b1+"/"
b3 = "data2_divided_parts/"+b1+"/part01/"
b4 = "data2_divided_parts/"+b1+"/part02/"
b5 = "data2_divided_parts/"+b1+"/part03/"
b6 = "data2_divided_parts/"+b1+"/part04/"
b7 = "data2_divided_parts/"+b1+"/part05/"
b8 = "data2_divided_parts/"+b1+"/part06/"
b9 = "data2_divided_parts/"+b1+"/part07/"
b10 = "data2_divided_parts/"+b1+"/part08/"
b11 = "data2_divided_parts/"+b1+"/part09/"
b12 = "data2_divided_parts/"+b1+"/part10/"
a1 = 0
for fullname in glob.glob(b2+"*.csv"):
    b13 = pd.read_csv(fullname, b19=" ")
    b14 = len(b13.columns)
    a1 = a1+1
b15 = ["R%.3d" % i for i in range(1,a1+1)]
b16 = ["W%.3d" % i for i in range(1,b14+1)]
b17 = {}
for r in b15:
    b18 = r+".csv"
    b17[r+"_"] = pd.read_csv(b2+b18, b19 = " ")
    b17[r] = b17[r+"_"][b16]
    print("reading: "+b2+b18)
for r in b15:
    b17[r] = b17[r].sample(b20 = 1)
    print("Shuffling "+r)
b21 = {}
for r in b15:
    print("Dividing "+r)
    b22 = int(0.1*len(b17[r]))
    b21[r+"_part01"] = b17[r].iloc[0*b22:1*b22].reset_index(b23 = True)
    b21[r+"_part02"] = b17[r].iloc[1*b22:2*b22].reset_index(b23 = True)
    b21[r+"_part03"] = b17[r].iloc[2*b22:3*b22].reset_index(b23 = True)
    b21[r+"_part04"] = b17[r].iloc[3*b22:4*b22].reset_index(b23 = True)
    b21[r+"_part05"] = b17[r].iloc[4*b22:5*b22].reset_index(b23 = True)
    b21[r+"_part06"] = b17[r].iloc[0*b22:1*b22].reset_index(b23 = True)
    b21[r+"_part07"] = b17[r].iloc[1*b22:2*b22].reset_index(b23 = True)
    b21[r+"_part08"] = b17[r].iloc[2*b22:3*b22].reset_index(b23 = True)
    b21[r+"_part09"] = b17[r].iloc[3*b22:4*b22].reset_index(b23 = True)
    b21[r+"_part10"] = b17[r].iloc[4*b22:5*b22].reset_index(b23 = True)
if (not os.path.exists(b3)):
    os.makedirs(b3)
if (not os.path.exists(b4)):
    os.makedirs(b4)
if (not os.path.exists(b5)):
    os.makedirs(b5)
if (not os.path.exists(b6)):
    os.makedirs(b6)
if (not os.path.exists(b7)):
    os.makedirs(b7)
if (not os.path.exists(b8)):
    os.makedirs(b8)
if (not os.path.exists(b9)):
    os.makedirs(b9)
if (not os.path.exists(b10)):
    os.makedirs(b10)
if (not os.path.exists(b11)):
    os.makedirs(b11)
if (not os.path.exists(b12)):
    os.makedirs(b12)
for r in b15:
    b18 = r+".csv"
    b21[r+"_part01"].to_csv(b3+b18, b19 = ' ', index=False)
    print("Saving " + b3 + b18)
    b21[r+"_part02"].to_csv(b4+b18, b19 = ' ', index=False)
    print("Saving " + b4 + b18)
    b21[r+"_part03"].to_csv(b5+b18, b19 = ' ', index=False)
    print("Saving " + b5 + b18)
    b21[r+"_part04"].to_csv(b6+b18, b19 = ' ', index=False)
    print("Saving " + b6 + b18)
    b21[r+"_part05"].to_csv(b7+b18, b19 = ' ', index=False)
    print("Saving " + b7 + b18)
    b21[r+"_part06"].to_csv(b8+b18, b19 = ' ', index=False)
    print("Saving " + b8 + b18)
    b21[r+"_part07"].to_csv(b9+b18, b19 = ' ', index=False)
    print("Saving " + b9 + b18)
    b21[r+"_part08"].to_csv(b10+b18, b19 = ' ', index=False)
    print("Saving " + b10 + b18)
    b21[r+"_part09"].to_csv(b11+b18, b19 = ' ', index=False)
    print("Saving " + b11 + b18)
    b21[r+"_part10"].to_csv(b12+b18, b19 = ' ', index=False)
    print("Saving " + b12 + b18)