
import pandas as pd
import numpy as np
b13 = pd.read_csv("multivar.csv", sep='\t')
print(b13.head(6))
b14 = b13['Mech Apt'].values
b3 = b13['Consc'].values
b4 = b13['Job Perf'].values
X_mean, X1_mean, b5 = np.mean(b14), np.mean(b3), np.mean(b4)
sumX, sumX1, b6 = np.sum(b14), np.sum(b3), np.sum(b4)
mulXY, b7 = np.multiply(b14, b4), np.multiply(b3, b4)
sum_mul_XY, b8 = np.sum(mulXY), np.sum(b7)
Xsquare, X1square, b9 = np.multiply(b14, b14), np.multiply(b3, b3), np.multiply(b4, b4)
sum_X_square, b10 = np.sum(Xsquare), np.sum(X1square)
b11 = np.multiply(b14, b3)
b12 = np.sum(b11)
b13 = (((b10 * sum_mul_XY) - (b12 * b8)) / ((sum_X_square * b10) - (b12 * b12)))
b14 = (((sum_X_square * b8) - (b12 * sum_mul_XY)) / ((sum_X_square * b10) - (b12 * b12)))
b15 = b5 - (b13 * X_mean) - (b14 * X1_mean)
print("Coefficient of b3:", b13)
print("Coefficient of X2:", b14)
print("Constant:", b15)
b16 = b13 * b14 + b14 * b3 + b15