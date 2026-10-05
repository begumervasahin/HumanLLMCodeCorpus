
import pandas as pd
import numpy as np
b22 = pd.read_csv("multivar.csv", sep='\t')
print(b22.head(6))
b23 = b22['Mech Apt'].values
b3 = b22['Consc'].values
b4 = b22['Job Perf'].values
b5 = np.mean(b23)
b6 = np.mean(b3)
b7 = np.mean(b4)
b8 = np.sum(b23)
b9 = np.sum(b3)
b10 = np.sum(b4)
b11 = np.multiply(b23, b4)
b12 = np.multiply(b3, b4)
b13 = np.sum(b11)
b14 = np.sum(b12)
b15 = np.multiply(b23, b23)
b16 = np.multiply(b3, b3)
b17 = np.multiply(b4, b4)
b18 = np.sum(b15)
b19 = np.sum(b16)
b20 = np.multiply(b23, b3)
b21 = np.sum(b20)
b22 = (((b19)*(b13)) - ((b21)*(b14))) / (((b18)*(b19)) - (b21*b21))
b23 = (((b18)*(b14)) - ((b21)*(b13))) / (((b18)*(b19)) - (b21*b21))
b24 = b7 - (b22*b5) - (b23*b6)
print("Coefficient of b3:", b22)
print("Coefficient of X2:", b23)
print("Constant:", b24)
b25 = b22*b23 + b23*b3 + b24