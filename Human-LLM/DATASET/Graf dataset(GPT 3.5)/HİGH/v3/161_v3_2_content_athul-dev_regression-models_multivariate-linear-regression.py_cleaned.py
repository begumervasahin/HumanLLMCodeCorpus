import pandas as pd
import numpy as np
def fonk1(filename, b11 = '\t'):
    return pd.read_csv(filename, b14 = b11)
def fonk2(data):
    return data.mean()
def fonk3(data):
    return data.sum()
def fonk4(b17, b18, b19):
    return np.sum(b17 * b19), np.sum(b18 * b19), np.sum(b17 * b18)
def fonk5(b17, b18, b19, sumX, sumX1, b22, sum_mul_XY, sum_mul_X1Y, b23):
    b3 = np.mean(b17)
    b4 = np.mean(b18)
    b5 = np.mean(b19)
    b6 = np.sum(b17 * b17)
    b7 = np.sum(b18 * b18)
    b8 = b4 * b4
    b9 = (sumX1 * sum_mul_XY) - (b23 * sum_mul_X1Y)
    b10 = (sumX * b7) - (b23 * sumX1)
    b11 = b9 / b10
    b12 = (sumX * sum_mul_X1Y) - (b23 * sum_mul_XY)
    b13 = (sumX_square * sumX1) - (b23 * sumX)
    b14 = b12 / b13
    b15 = b5 - (b11 * b3) - (b14 * b4)
    return b11, b14, b15
def fonk6(b11, b14, b15):
    print("Coefficient of b18:", b11)
    print("Coefficient of X2:", b14)
    print("Constant Part:", b15)
def fonk7(b17, b18, b11, b14, b15):
    return b11 * b17 + b14 * b18 + b15
b16 = fonk1("multivar.csv")
print("First 6 rows of the DataFrame:")
print(b16.head(6))
b17 = b16['Mech Apt'].values
b18 = b16['Consc'].values
b19 = b16['Job Perf'].values
b20 = fonk2(b16)
b3, b4, b5 = b20['Mech Apt'], b20['Consc'], b20['Job Perf']
b21 = fonk3(b16)
sumX, sumX1, b22 = b21['Mech Apt'], b21['Consc'], b21['Job Perf']
sum_mul_XY, sum_mul_X1Y, b23 = fonk4(b17, b18, b19)
b11, b14, b15 = fonk5(b17, b18, b19, sumX, sumX1, b22, sum_mul_XY, sum_mul_X1Y, b23)
fonk6(b11, b14, b15)
b24 = fonk7(b17, b18, b11, b14, b15)