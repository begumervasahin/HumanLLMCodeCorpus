
import pandas as pd
import numpy as np
df = pd.read_csv("multivar.csv", sep='\t')
print(df.head(6))
X = df['Mech Apt'].values
X1 = df['Consc'].values
Y = df['Job Perf'].values
X_mean, X1_mean, Y_mean = np.mean(X), np.mean(X1), np.mean(Y)
sumX, sumX1, sumY = np.sum(X), np.sum(X1), np.sum(Y)
mulXY, mulX1Y = np.multiply(X, Y), np.multiply(X1, Y)
sum_mul_XY, sum_mul_X1Y = np.sum(mulXY), np.sum(mulX1Y)
Xsquare, X1square, Ysquare = np.multiply(X, X), np.multiply(X1, X1), np.multiply(Y, Y)
sum_X_square, sum_X1_square = np.sum(Xsquare), np.sum(X1square)
mul_XX1 = np.multiply(X, X1)
sum_mul_XX1 = np.sum(mul_XX1)
b1 = (((sum_X1_square * sum_mul_XY) - (sum_mul_XX1 * sum_mul_X1Y)) / ((sum_X_square * sum_X1_square) - (sum_mul_XX1 * sum_mul_XX1)))
b2 = (((sum_X_square * sum_mul_X1Y) - (sum_mul_XX1 * sum_mul_XY)) / ((sum_X_square * sum_X1_square) - (sum_mul_XX1 * sum_mul_XX1)))
a = Y_mean - (b1 * X_mean) - (b2 * X1_mean)
print("Coefficient of X1:", b1)
print("Coefficient of X2:", b2)
print("Constant:", a)
updated_y = b1 * X + b2 * X1 + a