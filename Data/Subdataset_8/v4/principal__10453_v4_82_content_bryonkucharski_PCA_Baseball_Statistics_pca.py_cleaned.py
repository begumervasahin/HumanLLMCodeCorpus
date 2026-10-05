import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
from math import sqrt
def populate_stat(sheet, name, column_number):
    arr = []
    for i in range(sheet.nrows):
        if(sheet.cell(i, column_number).value != '') and (sheet.cell(i, column_number).value != name):
            arr.append(sheet.cell(i, column_number).value)
    return arr
def standardize(input):
    mean_input = np.mean(input)
    variance = np.var(input, mean_input)
    sdev = np.std(variance)
    for i in range(len(input)):
        input[i] = (input[i] - mean_input) / float(sdev)
    return input
def mean(input):
    return sum(input) / float(len(input))
def var(input, mean):
    sum_var = 0.0
    for i in range(len(input)):
        sum_var += ((input[i] - mean) ** 2)
    return sum_var / float(len(input))
def std(variance):
    return sqrt(variance)
names = ['Win Percentage', 'Runs', 'Batting Walks', 'Stikeouts', 'Stolen Bases', 'Batting Average',
         'On Base Percentage', 'Slugging Percentage', 'Innings Pitched', 'Hits', 'Pitching Walks',
         'K/9', 'ERA', 'WHIP', 'Fielding Percentage']
colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'b', 'g', 'r', 'c', 'm']
teams = ['Curry', 'Eastern Nazarene', 'Endicott', 'Gordon', 'Nichols', 'Roger Williams',
         'Salve Regina', 'Wentworth', 'Western New England']
years = ['2017', '2016', '2015', '2014', '2013']
colors2 = ['purple', 'red', 'lightgreen', 'lightskyblue', 'darkgreen', 'darkblue', 'cyan', 'gold', 'magenta']
symbol = ['*', 'v', '^', '+', 'o']
data = xlrd.open_workbook(sys.argv[1])
winPercentagesSheet = data.sheet_by_index(0)
battingStatsSheet = data.sheet_by_index(1)
pitchingStatsSheet = data.sheet_by_index(2)
fieldingStatsSheet = data.sheet_by_index(3)
winPercentages = populate_stat(winPercentagesSheet, 'Percentage', 3)
runs = populate_stat(battingStatsSheet, 'Runs', 2)
batting_walks = populate_stat(battingStatsSheet, 'Walks', 3)
strikeouts = populate_stat(battingStatsSheet, 'Strikeouts', 4)
stolen_bases = populate_stat(battingStatsSheet, 'Stolen Bases', 5)
batting_average = populate_stat(battingStatsSheet, 'Batting Average', 6)
on_base_percentage = populate_stat(battingStatsSheet, 'On Base Percentage', 7)
slugging_percentage = populate_stat(battingStatsSheet, 'Slugging Percentage', 8)
innings_pitched = populate_stat(pitchingStatsSheet, 'Innings Pitched', 2)
hits = populate_stat(pitchingStatsSheet, 'Hits', 3)
pitching_walks = populate_stat(pitchingStatsSheet, 'Walks', 4)
strikeouts_through_nine = populate_stat(pitchingStatsSheet, 'Strikeouts Through 9', 5)
earned_run_average = populate_stat(pitchingStatsSheet, 'Earned Run Average', 6)
whip = populate_stat(pitchingStatsSheet, 'Walks Hits Per Inning Pitched', 7)
fielding_percentage = populate_stat(fieldingStatsSheet, 'Fielding Percentage', 2)
winPercentages = standardize(winPercentages)
runs = standardize(runs)
batting_walks = standardize(batting_walks)
strikeouts = standardize(strikeouts)
stolen_bases = standardize(stolen_bases)
batting_average = standardize(batting_average)
on_base_percentage = standardize(on_base_percentage)
slugging_percentage = standardize(slugging_percentage)
innings_pitched = standardize(innings_pitched)
hits = standardize(hits)
pitching_walks = standardize(pitching_walks)
strikeouts_through_nine = standardize(strikeouts_through_nine)
earned_run_average = standardize(earned_run_average)
whip = standardize(whip)
fielding_percentage = standardize(fielding_percentage)
np.set_printoptions(suppress=True, precision=3)
standardized_matrix = np.vstack([winPercentages, runs, batting_walks, strikeouts, stolen_bases,
                                 batting_average, on_base_percentage, slugging_percentage, innings_pitched,
                                 hits, pitching_walks, strikeouts_through_nine, earned_run_average, whip,
                                 fielding_percentage])
assert standardized_matrix.shape == (15, 45), 'Input matrix incorrect size'
sklearn_pca = sklearnPCA(n_components=2)
sklearn_transf = sklearn_pca.fit_transform(standardized_matrix.T)
covariance_matrix = np.cov(standardized_matrix)
print("Covariance matrix:")
print(covariance_matrix)
print("\n")
assert covariance_matrix.shape == (15, 15), 'Covariance matrix incorrect size'
eigen_values, eig_vectors = np.linalg.eig(covariance_matrix)
sum_eig = sum(eigen_values)
for i in range(len(eigen_values)):
    print('Eigenvector {}: \n{}'.format(i+1, eig_vectors[i].reshape(15, 1)))
    print('Eigenvalue {}: {}'.format(i+1, eigen_values[i]))
idx = eigen_values.argsort()[::-1]
eigenvalues = eigen_values[idx][:2]
eigenvectors = np.atleast_1d(eig_vectors[:, idx])[:, :2]
X_transformed = eigenvectors.T.dot(standardized_matrix)
print('-------------')
print(idx)
print(eigenvalues)
print(eigenvectors)
print(eigenvalues[0] / sum_eig)
print(eigenvalues[1] / sum_eig)
print('------------')
print("Method 2 output:")
print(X_transformed)
print('\n')
print("Sklearn output:")
print(sklearn_transf)
print('\n')
year_index = 0
name_index = -1
for i in range(0, 45):
    name_index = i % 9
    if(name_index == 0):
        year_index += 1
    plt.plot(X_transformed[0][i], X_transformed[1][i], symbol[year_index-1], color=colors2[name_index])
for i in range(len(eigenvectors)):
    arrow = plt.arrow(0, 0, eigenvectors[i][0], eigenvectors[i][1], fc='k', ec=colors[i],
                      head_width=0.001, head_length=0.01, facecolor='r', label=names[i])
    plt.annotate(names[i], xy=(eigenvectors[i][0], eigenvectors[i][1]))
patches = []
for i in range(len(teams)):
    patches.append(plt.Line2D([], [], marker='o', color='w', markerfacecolor=colors2[i], markersize=10, label=teams[i]))
for i in range(len(years)):
    patches.append(plt.Line2D([], [], marker=symbol[i], color='w', markerfacecolor='black', markersize=10, label=years[i]))
plt.legend(handles=patches, bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()