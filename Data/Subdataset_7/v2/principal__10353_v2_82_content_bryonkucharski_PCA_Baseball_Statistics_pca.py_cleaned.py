import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def fonk1(sheet, name, column_number):
    b1 = []
    for i in range(sheet.nrows):
        b2 = sheet.cell(i, column_number).b2
        if b2 != '' and b2 != name:
            b1.append(b2)
    return b1
def fonk2(b1):
    b3 = np.b3(b1)
    b4 = np.var(b1, ddof=1)
    b5 = np.sqrt(b4)
    b6 = [(x - b3) / b5 for x in b1]
    return b6
def fonk3():
    b1 = xlrd.open_workbook(sys.argv[1])
    b7 = b1.sheet_by_index(0)
    b8 = b1.sheet_by_index(1)
    b9 = b1.sheet_by_index(2)
    b10 = b1.sheet_by_index(3)
    b11 = fonk1(b7, 'Percentage', 3)
    b12 = fonk1(b8, 'Runs', 2)
    b13 = fonk1(b8, 'Walks', 3)
    b14 = fonk1(b8, 'Strikeouts', 4)
    b15 = fonk1(b8, 'Stolen Bases', 5)
    b16 = fonk1(b8, 'Batting Average', 6)
    b17 = fonk1(b8, 'On Base Percentage', 7)
    b18 = fonk1(b8, 'Slugging Percentage', 8)
    b19 = fonk1(b9, 'Innings Pitched', 2)
    b20 = fonk1(b9, 'Hits', 3)
    b21 = fonk1(b9, 'Walks', 4)
    b22 = fonk1(b9, 'Strikeouts Through 9', 5)
    b23 = fonk1(b9, 'Earned Run Average', 6)
    b24 = fonk1(b9, 'Walks Hits Per Inning Pitched', 7)
    b25 = fonk1(b10, 'Fielding Percentage', 2)
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
    b25 = fonk2(b25)
    b26 = np.vstack([
        b11, b12, b13, b14, b15, b16,
        b17, b18, b19, b20, b21,
        b22, b23, b24, b25
    ])
    assert b26.b27 = = (15, 45), 'input matrix incorrect size'
    b28 = PCA(n_components=2)
    b29 = b28.fit_transform(b26.T)
    fig, b30 = plt.subplots()
    b30.scatter(b29[:, 0], b29[:, 1])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    plt.show()
if b31 = = "__main__":
    fonk3()