import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def fonk1(sheet_index):
    b1 = xlrd.open_workbook(sys.argv[1])
    b2 = b1.sheet_by_index(sheet_index)
    return b2
def fonk2(b2, column_number):
    b3 = [b2.cell(row, column_number).value for row in range(1, b2.nrows)
            if b2.cell(row, column_number).value != '']
    return b3
def fonk3(b3):
    b4 = np.b4(b3)
    b5 = np.sqrt(np.var(b3, ddof=1))
    b6 = [(value - b4) / b5 for value in b3]
    return b6
def fonk4():
    b7 = {
        0: ('Percentage', 3),
        1: [('Runs', 2), ('Walks', 3), ('Strikeouts', 4), ('Stolen Bases', 5), ('Batting Average', 6),
            ('On Base Percentage', 7), ('Slugging Percentage', 8)],
        2: [('Innings Pitched', 2), ('Hits', 3), ('Walks', 4), ('Strikeouts Through 9', 5),
            ('Earned Run Average', 6), ('Walks Hits Per Inning Pitched', 7)],
        3: [('Fielding Percentage', 2)]
    }
    b6 = []
    for sheet_index, stats in b7.items():
        b2 = fonk1(sheet_index)
        for stat_name, column_number in stats:
            b8 = fonk2(b2, column_number)
            b9 = fonk3([float(value) for value in b8])
            b6.append(b9)
    b10 = np.vstack(b6)
    assert b10.shape[1] == len(b6[0]), 'Data matrix has inconsistent row lengths'
    return b10
def fonk5(b3):
    b11 = PCA(n_components=2)
    b12 = b11.fit_transform(b3.T)
    plt.figure(b13 = (8, 6))
    plt.scatter(b12[:, 0], b12[:, 1], b14 = 0.7)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA of Baseball Team Statistics')
    plt.grid(True)
    plt.show()
def fonk6():
    b10 = fonk4()
    fonk5(b10)
if b15 = = "__main__":
    fonk6()