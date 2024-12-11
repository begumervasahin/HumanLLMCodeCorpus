import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
def fonk1(sheet, name, column_number):
    b1 = [sheet.cell_value(i, column_number) for i in range(sheet.nrows)
            if sheet.cell_value(i, column_number) not in ['', name]]
    return b1
def fonk2(input_data):
    b2 = np.mean(input_data)
    b3 = np.var(input_data)
    b4 = np.std(input_data)
    b5 = [(b14 - b2) / b4 for b14 in input_data]
    return b5
def fonk3(file_path):
    b1 = xlrd.open_workbook(file_path)
    return b1
def fonk4(X, b49, b20, b16, b17, b18, b19, b15):
    a1 = 0
    a2 = -1
    for i in range(X.b41[1]):
        a2 = i % len(b17)
        if a2 = = 0:
            a1 += 1
        plt.plot(X[0][i], X[1][i], b20[a1 - 1], b6 = b19[a2])
    for i, vec in enumerate(b49):
        plt.arrow(0, 0, vec[0], vec[1], b7 = 'k', ec=b16[i], head_width=0.001, head_length=0.01,
                  b8 = 'r', label=b15[i])
        plt.annotate(b15[i], b9 = (vec[0], vec[1]))
    b10 = [plt.Line2D([], [], b11='o', b6='w', markerfacecolor=b19[i], markersize=10, label=team)
               for i, team in enumerate(b17)]
    b10 += [plt.Line2D([], [], b11 = b20[i], b6='w', markerfacecolor='black', markersize=10, label=year)
                for i, year in enumerate(b18)]
    plt.legend(b12 = b10, bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.axhline(b13 = 0, b6='k')
    plt.axvline(b14 = 0, b6='k')
    plt.show()
def fonk5(file_path):
    b15 = ['Win Percentage', 'Runs', 'Batting Walks', 'Stikeouts', 'Stolen Bases', 'Batting Average',
             'On Base Percentage', 'Slugging Percentage', 'Innings Pitched', 'Hits', 'Pitching Walks',
             'K/9', 'ERA', 'WHIP', 'Fielding Percentage']
    b16 = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'b', 'g', 'r', 'c', 'm']
    b17 = ['Curry', 'Eastern Nazarene', 'Endicott', 'Gordon', 'Nichols', 'Roger Williams',
             'Salve Regina', 'Wentworth', 'Western New England']
    b18 = ['2017', '2016', '2015', '2014', '2013']
    b19 = ['purple', 'red', 'lightgreen', 'lightskyblue', 'darkgreen', 'darkblue', 'cyan', 'gold', 'magenta']
    b20 = ['*', 'v', '^', '+', 'o']
    b1 = fonk3(file_path)
    b21 = b1.sheet_by_index(0)
    b22 = b1.sheet_by_index(1)
    b23 = b1.sheet_by_index(2)
    b24 = b1.sheet_by_index(3)
    b25 = fonk2(fonk1(b21, 'Percentage', 3))
    b26 = fonk2(fonk1(b22, 'Runs', 2)))
    b27 = fonk2(fonk1(b22, 'Walks', 3)))
    b28 = fonk2(fonk1(b22, 'Strikeouts', 4)))
    b29 = fonk2(fonk1(b22, 'Stolen Bases', 5)))
    b30 = fonk2(fonk1(b22, 'Batting Average', 6)))
    b31 = fonk2(fonk1(b22, 'On Base Percentage', 7)))
    b32 = fonk2(fonk1(b22, 'Slugging Percentage', 8)))
    b33 = fonk2(fonk1(b23, 'Innings Pitched', 2)))
    b34 = fonk2(fonk1(b23, 'Hits', 3)))
    b35 = fonk2(fonk1(b23, 'Walks', 4)))
    b36 = fonk2(fonk1(b23, 'Strikeouts Through 9', 5)))
    b37 = fonk2(fonk1(b23, 'Earned Run Average', 6)))
    b38 = fonk2(fonk1(b23, 'Walks Hits Per Inning Pitched', 7)))
    b39 = fonk2(fonk1(b24, 'Fielding Percentage', 2)))
    b40 = np.vstack([b25, b26, b27, b28, b29,
                                      b30, b31, b32, b33,
                                      b34, b35, b36, b37, b38,
                                      b39])
    assert b40.b41 = = (15, 45), 'Input matrix incorrect size'
    b42 = sklearnPCA(n_components=2)
    b43 = b42.fit_transform(b40.T)
    b44 = np.cov(b40)
    print("Covariance matrix:")
    print(b44)
    print("\n")
    assert b44.b41 = = (15, 15), 'Covariance matrix incorrect size'
    eigen_values, b45 = np.linalg.eig(b44)
    b46 = sum(eigen_values)
    for i in range(len(eigen_values)):
        print('Eigenvector {}: \n{}'.format(i+1, b45[i].reshape(15, 1)))
        print('Eigenvalue {}: {}'.format(i+1, eigen_values[i]))
    b47 = eigen_values.argsort()[::-1]
    b48 = eigen_values[b47][:2]
    b49 = np.atleast_1d(b45[:, b47])[:, :2]
    b50 = b49.T.dot(b40)
    print('-------------')
    print(b47)
    print(b48)
    print(b49)
    print(b48[0] / b46)
    print(b48[1] / b46)
    print('------------')
    print("Method 2 output:")
    print(b50)
    print('\n')
    print("Sklearn output:")
    print(b43)
    print('\n')
    fonk4(b50, b49, b20, b16, b17, b18, b19, b15)
if b51 = = "__main__":
    fonk5(sys.argv[1])