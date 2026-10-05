import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
from math import sqrt
def fonk1(sheet, name, column_number):
    b1 = []
    for i in range(sheet.nrows):
        if(sheet.cell(i, column_number).value != '') and (sheet.cell(i, column_number).value != name):
            b1.append(sheet.cell(i, column_number).value)
    return b1
def fonk2(input):
    b2 = np.fonk3(input)
    b3 = np.fonk4(input, b2)
    b4 = np.fonk5(b3)
    for i in range(len(input)):
        input[i] = (input[i] - b2) / float(b4)
    return input
def fonk3(input):
    return sum(input) / float(len(input))
def fonk4(input, mean):
    a1 = 0.0
    for i in range(len(input)):
        a1 += ((input[i] - mean) ** 2)
    return a1 / float(len(input))
def fonk5(b3):
    return sqrt(b3)
b5 = ['Win Percentage', 'Runs', 'Batting Walks', 'Stikeouts', 'Stolen Bases', 'Batting Average',
         'On Base Percentage', 'Slugging Percentage', 'Innings Pitched', 'Hits', 'Pitching Walks',
         'K/9', 'ERA', 'WHIP', 'Fielding Percentage']
b6 = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'b', 'g', 'r', 'c', 'm']
b7 = ['Curry', 'Eastern Nazarene', 'Endicott', 'Gordon', 'Nichols', 'Roger Williams',
         'Salve Regina', 'Wentworth', 'Western New England']
b8 = ['2017', '2016', '2015', '2014', '2013']
b9 = ['purple', 'red', 'lightgreen', 'lightskyblue', 'darkgreen', 'darkblue', 'cyan', 'gold', 'magenta']
b10 = ['*', 'v', '^', '+', 'o']
b11 = xlrd.open_workbook(sys.argv[1])
b12 = b11.sheet_by_index(0)
b13 = b11.sheet_by_index(1)
b14 = b11.sheet_by_index(2)
b15 = b11.sheet_by_index(3)
b16 = fonk1(b12, 'Percentage', 3)
b17 = fonk1(b13, 'Runs', 2)
b18 = fonk1(b13, 'Walks', 3)
b19 = fonk1(b13, 'Strikeouts', 4)
b20 = fonk1(b13, 'Stolen Bases', 5)
b21 = fonk1(b13, 'Batting Average', 6)
b22 = fonk1(b13, 'On Base Percentage', 7)
b23 = fonk1(b13, 'Slugging Percentage', 8)
b24 = fonk1(b14, 'Innings Pitched', 2)
b25 = fonk1(b14, 'Hits', 3)
b26 = fonk1(b14, 'Walks', 4)
b27 = fonk1(b14, 'Strikeouts Through 9', 5)
b28 = fonk1(b14, 'Earned Run Average', 6)
b29 = fonk1(b14, 'Walks Hits Per Inning Pitched', 7)
b30 = fonk1(b15, 'Fielding Percentage', 2)
b16 = fonk2(b16)
b17 = fonk2(b17)
b18 = fonk2(b18)
b19 = fonk2(b19)
b20 = fonk2(b20)
b21 = fonk2(b21)
b22 = fonk2(b22)
b23 = fonk2(b23)
b24 = fonk2(b24)
b25 = fonk2(b25)
b26 = fonk2(b26)
b27 = fonk2(b27)
b28 = fonk2(b28)
b29 = fonk2(b29)
b30 = fonk2(b30)
np.set_printoptions(b31 = True, precision=3)
b32 = np.vstack([b16, b17, b18, b19, b20,
                                 b21, b22, b23, b24,
                                 b25, b26, b27, b28, b29,
                                 b30])
assert b32.b33 = = (15, 45), 'Input matrix incorrect size'
b34 = sklearnPCA(n_components=2)
b35 = b34.fit_transform(b32.T)
b36 = np.cov(b32)
print("Covariance matrix:")
print(b36)
print("\n")
assert b36.b33 = = (15, 15), 'Covariance matrix incorrect size'
eigen_values, b37 = np.linalg.eig(b36)
b38 = sum(eigen_values)
for i in range(len(eigen_values)):
    print('Eigenvector {}: \n{}'.format(i+1, b37[i].reshape(15, 1)))
    print('Eigenvalue {}: {}'.format(i+1, eigen_values[i]))
b39 = eigen_values.argsort()[::-1]
b40 = eigen_values[b39][:2]
b41 = np.atleast_1d(b37[:, b39])[:, :2]
b42 = b41.T.dot(b32)
print('-------------')
print(b39)
print(b40)
print(b41)
print(b40[0] / b38)
print(b40[1] / b38)
print('------------')
print("Method 2 output:")
print(b42)
print('\n')
print("Sklearn output:")
print(b35)
print('\n')
a2 = 0
a3 = -1
for i in range(0, 45):
    a3 = i % 9
    if(a3 = = 0):
        a2 += 1
    plt.plot(b42[0][i], b42[1][i], b10[a2-1], b43 = b9[a3])
for i in range(len(b41)):
    b44 = plt.b44(0, 0, b41[i][0], b41[i][1], fc='k', ec=b6[i],
                      b45 = 0.001, head_length=0.01, facecolor='r', label=b5[i])
    plt.annotate(b5[i], b46 = (b41[i][0], b41[i][1]))
b47 = []
for i in range(len(b7)):
    b47.append(plt.Line2D([], [], b48 = 'o', b43='w', markerfacecolor=b9[i], markersize=10, label=b7[i]))
for i in range(len(b8)):
    b47.append(plt.Line2D([], [], b48 = b10[i], b43='w', markerfacecolor='black', markersize=10, label=b8[i]))
plt.legend(b49 = b47, bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
plt.axhline(b50 = 0, b43='k')
plt.axvline(b51 = 0, b43='k')
plt.show()