import pandas as pd
import numpy as np
df = pd.read_csv("multivar.csv", sep='\t')
print("First 6 rows of the DataFrame:")
print(df.head(6))
X = df['Mech Apt'].values
X1 = df['Consc'].values
Y = df['Job Perf'].values
X_mean = np.mean(X)
X1_mean = np.mean(X1)
Y_mean = np.mean(Y)
sumX = np.sum(X)
sumX1 = np.sum(X1)
sumY = np.sum(Y)
mulXY = np.multiply(X, Y)
mulX1Y = np.multiply(X1, Y)
sum_mul_XY = np.sum(mulXY)
sum_mul_X1Y = np.sum(mulX1Y)
Xsquare = np.multiply(X, X)
X1square = np.multiply(X1, X1)
Ysquare = np.multiply(Y, Y)
sum_X_square = np.sum(Xsquare)
sum_X1_square = np.sum(X1square)
mul_XX1 = np.multiply(X, X1)
sum_mul_XX1 = np.sum(mul_XX1)
b1 = (((sum_X1_square)*(sum_mul_XY))-((sum_mul_XX1)*(sum_mul_X1Y))) / (((sum_X_square)*(sum_X1_square))-(sum_mul_XX1*sum_mul_XX1))
b2 = (((sum_X_square)*(sum_mul_X1Y))-((sum_mul_XX1)*(sum_mul_XY))) / (((sum_X_square)*(sum_X1_square)) - (sum_mul_XX1*sum_mul_XX1))
a = Y_mean - (b1*X_mean) - (b2*X1_mean)
print("Coefficient of X1:", b1)
print("Coefficient of X2:", b2)
print("Constant Part:", a)
updated_y = b1*X + b2*X1 + a