import pandas as pd
import numpy as np
def read_data(filename, separator='\t'):
    return pd.read_csv(filename, sep=separator)
def calculate_means(data):
    return data.mean()
def calculate_sums(data):
    return data.sum()
def calculate_sums_of_products(X, X1, Y):
    return np.sum(X * Y), np.sum(X1 * Y), np.sum(X * X1)
def calculate_coefficients(X, X1, Y, sumX, sumX1, sumY, sum_mul_XY, sum_mul_X1Y, sum_mul_XX1):
    X_mean = np.mean(X)
    X1_mean = np.mean(X1)
    Y_mean = np.mean(Y)
    X_square = np.sum(X * X)
    X1_square = np.sum(X1 * X1)
    X1_mean_square = X1_mean * X1_mean
    b1_numerator = (sumX1 * sum_mul_XY) - (sum_mul_XX1 * sum_mul_X1Y)
    b1_denominator = (sumX * X1_square) - (sum_mul_XX1 * sumX1)
    b1 = b1_numerator / b1_denominator
    b2_numerator = (sumX * sum_mul_X1Y) - (sum_mul_XX1 * sum_mul_XY)
    b2_denominator = (sumX_square * sumX1) - (sum_mul_XX1 * sumX)
    b2 = b2_numerator / b2_denominator
    a = Y_mean - (b1 * X_mean) - (b2 * X1_mean)
    return b1, b2, a
def print_results(b1, b2, a):
    print("Coefficient of X1:", b1)
    print("Coefficient of X2:", b2)
    print("Constant Part:", a)
def calculate_updated_Y(X, X1, b1, b2, a):
    return b1 * X + b2 * X1 + a
df = read_data("multivar.csv")
print("First 6 rows of the DataFrame:")
print(df.head(6))
X = df['Mech Apt'].values
X1 = df['Consc'].values
Y = df['Job Perf'].values
means = calculate_means(df)
X_mean, X1_mean, Y_mean = means['Mech Apt'], means['Consc'], means['Job Perf']
sums = calculate_sums(df)
sumX, sumX1, sumY = sums['Mech Apt'], sums['Consc'], sums['Job Perf']
sum_mul_XY, sum_mul_X1Y, sum_mul_XX1 = calculate_sums_of_products(X, X1, Y)
b1, b2, a = calculate_coefficients(X, X1, Y, sumX, sumX1, sumY, sum_mul_XY, sum_mul_X1Y, sum_mul_XX1)
print_results(b1, b2, a)
updated_y = calculate_updated_Y(X, X1, b1, b2, a)