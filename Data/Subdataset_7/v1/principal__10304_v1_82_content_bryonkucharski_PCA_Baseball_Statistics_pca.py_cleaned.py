import numpy as np
import xlrd
import sys
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from sklearn.decomposition import PCA
def fonk1(sheet, name, column_number):
    b1 = []
    for i in range(sheet.nrows):
        if(sheet.cell(i,column_number).value != '') and (sheet.cell(i,column_number).value != name):
            b1.append(sheet.cell(i,column_number).value)
    return b1
def fonk2(input):
    b2 = np.mean(input)
    b3 = np.var(input, ddof=1)
    b4 = np.sqrt(b3)
    for i in range(len(input)):
        input[i] = (input[i] - b2) / b4
    return input
b5 = xlrd.open_workbook(sys.argv[1])
b6 = b5.sheet_by_index(0)
b7 = b5.sheet_by_index(1)
b8 = b5.sheet_by_index(2)
b9 = b5.sheet_by_index(3)
b10 = fonk1(b6, 'Percentage', 3)
b11 = fonk1(b7, 'Runs', 2)
b12 = fonk1(b7, 'Walks', 3)
b13 = fonk1(b7, 'Strikeouts', 4)
b14 = fonk1(b7, 'Stolen Bases', 5)
b15 = fonk1(b7, 'Batting Average', 6)
b16 = fonk1(b7, 'On Base Percentage', 7)
b17 = fonk1(b7, 'Slugging Percentage', 8)
b18 = fonk1(b8, 'Innings Pitched', 2)
b19 = fonk1(b8, 'Hits', 3)
b20 = fonk1(b8, 'Walks', 4)
b21 = fonk1(b8, 'Strikeouts Through 9', 5)
b22 = fonk1(b8, 'Earned Run Average', 6)
b23 = fonk1(b8, 'Walks Hits Per Inning Pitched', 7)
b24 = fonk1(b9, 'Fielding Percentage', 2)
b10 = fonk2(b10)
b11 = fonk2(b11)
b12 = fonk2(b12)
b13 = fonk2(b13)
b14 = fonk2(b14)
b15 = fonk2(b15)
b16 = fonk2(b16)
b17 = fonk2(b17)
b18 = fonk2(b18)
b19 = fonk2(b19)
b20 = fonk2(b20)
b21 = fonk2(b21)
b22 = fonk2(b22)
b23 = fonk2(b23)
b24 = fonk2(b24)
b25 = np.vstack([
    b10, b11, b12, b13, b14, b15,
    b16, b17, b18, b19, b20,
    b21, b22, b23, b24
])
assert b25.b26 = = (15, 45), 'input matrix incorrect size'
b27 = PCA(n_components=2)
b28 = b27.fit_transform(b25.T)
fig, b29 = plt.subplots()
b29.scatter(b28[:, 0], b28[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA')
plt.show()