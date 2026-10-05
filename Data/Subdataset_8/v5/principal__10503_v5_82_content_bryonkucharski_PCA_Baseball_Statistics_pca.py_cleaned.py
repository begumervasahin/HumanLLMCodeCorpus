import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
def populate_stat(sheet, name, column_number):
    data = [sheet.cell_value(i, column_number) for i in range(sheet.nrows)
            if sheet.cell_value(i, column_number) not in ['', name]]
    return data
def standardize(input_data):
    mean_input = np.mean(input_data)
    variance = np.var(input_data)
    std_dev = np.std(input_data)
    standardized = [(x - mean_input) / std_dev for x in input_data]
    return standardized
def load_data(file_path):
    data = xlrd.open_workbook(file_path)
    return data
def plot_data(X, eigenvectors, symbol, colors, teams, years, colors2, names):
    year_index = 0
    name_index = -1
    for i in range(X.shape[1]):
        name_index = i % len(teams)
        if name_index == 0:
            year_index += 1
        plt.plot(X[0][i], X[1][i], symbol[year_index - 1], color=colors2[name_index])
    for i, vec in enumerate(eigenvectors):
        plt.arrow(0, 0, vec[0], vec[1], fc='k', ec=colors[i], head_width=0.001, head_length=0.01,
                  facecolor='r', label=names[i])
        plt.annotate(names[i], xy=(vec[0], vec[1]))
    patches = [plt.Line2D([], [], marker='o', color='w', markerfacecolor=colors2[i], markersize=10, label=team)
               for i, team in enumerate(teams)]
    patches += [plt.Line2D([], [], marker=symbol[i], color='w', markerfacecolor='black', markersize=10, label=year)
                for i, year in enumerate(years)]
    plt.legend(handles=patches, bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
def main(file_path):
    names = ['Win Percentage', 'Runs', 'Batting Walks', 'Stikeouts', 'Stolen Bases', 'Batting Average',
             'On Base Percentage', 'Slugging Percentage', 'Innings Pitched', 'Hits', 'Pitching Walks',
             'K/9', 'ERA', 'WHIP', 'Fielding Percentage']
    colors = ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'b', 'g', 'r', 'c', 'm']
    teams = ['Curry', 'Eastern Nazarene', 'Endicott', 'Gordon', 'Nichols', 'Roger Williams',
             'Salve Regina', 'Wentworth', 'Western New England']
    years = ['2017', '2016', '2015', '2014', '2013']
    colors2 = ['purple', 'red', 'lightgreen', 'lightskyblue', 'darkgreen', 'darkblue', 'cyan', 'gold', 'magenta']
    symbol = ['*', 'v', '^', '+', 'o']
    data = load_data(file_path)
    win_percentages_sheet = data.sheet_by_index(0)
    batting_stats_sheet = data.sheet_by_index(1)
    pitching_stats_sheet = data.sheet_by_index(2)
    fielding_stats_sheet = data.sheet_by_index(3)
    win_percentages = standardize(populate_stat(win_percentages_sheet, 'Percentage', 3))
    runs = standardize(populate_stat(batting_stats_sheet, 'Runs', 2)))
    batting_walks = standardize(populate_stat(batting_stats_sheet, 'Walks', 3)))
    strikeouts = standardize(populate_stat(batting_stats_sheet, 'Strikeouts', 4)))
    stolen_bases = standardize(populate_stat(batting_stats_sheet, 'Stolen Bases', 5)))
    batting_average = standardize(populate_stat(batting_stats_sheet, 'Batting Average', 6)))
    on_base_percentage = standardize(populate_stat(batting_stats_sheet, 'On Base Percentage', 7)))
    slugging_percentage = standardize(populate_stat(batting_stats_sheet, 'Slugging Percentage', 8)))
    innings_pitched = standardize(populate_stat(pitching_stats_sheet, 'Innings Pitched', 2)))
    hits = standardize(populate_stat(pitching_stats_sheet, 'Hits', 3)))
    pitching_walks = standardize(populate_stat(pitching_stats_sheet, 'Walks', 4)))
    strikeouts_through_nine = standardize(populate_stat(pitching_stats_sheet, 'Strikeouts Through 9', 5)))
    earned_run_average = standardize(populate_stat(pitching_stats_sheet, 'Earned Run Average', 6)))
    whip = standardize(populate_stat(pitching_stats_sheet, 'Walks Hits Per Inning Pitched', 7)))
    fielding_percentage = standardize(populate_stat(fielding_stats_sheet, 'Fielding Percentage', 2)))
    standardized_matrix = np.vstack([win_percentages, runs, batting_walks, strikeouts, stolen_bases,
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
    plot_data(X_transformed, eigenvectors, symbol, colors, teams, years, colors2, names)
if __name__ == "__main__":
    main(sys.argv[1])