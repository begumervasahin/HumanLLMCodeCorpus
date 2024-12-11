import pandas as pd
import numpy as np
b23 = pd.read_csv("multivar.csv",sep='\t')
print(b23.head(6))
b24 = b23['Mech Apt'].values
b3 = b23['Consc'].values
b4 = b23['Job Perf'].values
b5 = len(b24)
b6 = np.mean(b24)
b7 = np.mean(b3)
b8 = np.mean(b4)
b9 = np.sum(b24)
b10 = np.sum(b3)
b11 = np.sum(b4)
b12 = np.multiply(b24,b4)
b13 = np.multiply(b3,b4)
b14 = np.sum(b12)
b15 = np.sum(b13)
b16 = np.multiply(b24,b24)
b17 = np.multiply(b3,b3)
b18 = np.multiply(b4,b4)
b19 = np.sum(b16)
b20 = np.sum(b17)
b21 = np.multiply(b24,b3)
b22 = np.sum(b21)
b23 = (((b20)*(b14))-((b22)*(b15))) / (((b19)*(b20))-(b22*b22))
b24 = (((b19)*(b15))-((b22)*(b14))) / (((b19)*(b20)) - (b22*b22))
b25 = b8-(b23*b6)-(b24*b7)
print("Coeffecient of b3",b23)
print("Coeffecient of X2 ",b24)
print("Constant Part",b25)
b26 = b23*b24 + b24*b3 + b25