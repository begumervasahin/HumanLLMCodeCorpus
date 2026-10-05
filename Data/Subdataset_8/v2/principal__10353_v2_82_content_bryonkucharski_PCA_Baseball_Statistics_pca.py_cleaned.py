import numpy as np
import xlrd
import sys
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def populate_stat(sheet, name, column_number):
    data = []
    for i in range(sheet.nrows):
        value = sheet.cell(i, column_number).value
        if value != '' and value != name:
            data.append(value)
    return data
def standardize(data):
    mean = np.mean(data)
    variance = np.var(data, ddof=1)
    std_dev = np.sqrt(variance)
    standardized_data = [(x - mean) / std_dev for x in data]
    return standardized_data
def main():
    data = xlrd.open_workbook(sys.argv[1])
    win_percentages_sheet = data.sheet_by_index(0)
    batting_stats_sheet = data.sheet_by_index(1)
    pitching_stats_sheet = data.sheet_by_index(2)
    fielding_stats_sheet = data.sheet_by_index(3)
    win_percentages = populate_stat(win_percentages_sheet, 'Percentage', 3)
    runs = populate_stat(batting_stats_sheet, 'Runs', 2)
    batting_walks = populate_stat(batting_stats_sheet, 'Walks', 3)
    strikeouts = populate_stat(batting_stats_sheet, 'Strikeouts', 4)
    stolen_bases = populate_stat(batting_stats_sheet, 'Stolen Bases', 5)
    batting_average = populate_stat(batting_stats_sheet, 'Batting Average', 6)
    on_base_percentage = populate_stat(batting_stats_sheet, 'On Base Percentage', 7)
    slugging_percentage = populate_stat(batting_stats_sheet, 'Slugging Percentage', 8)
    innings_pitched = populate_stat(pitching_stats_sheet, 'Innings Pitched', 2)
    hits = populate_stat(pitching_stats_sheet, 'Hits', 3)
    pitching_walks = populate_stat(pitching_stats_sheet, 'Walks', 4)
    strikeouts_through_nine = populate_stat(pitching_stats_sheet, 'Strikeouts Through 9', 5)
    earned_run_average = populate_stat(pitching_stats_sheet, 'Earned Run Average', 6)
    whip = populate_stat(pitching_stats_sheet, 'Walks Hits Per Inning Pitched', 7)
    fielding_percentage = populate_stat(fielding_stats_sheet, 'Fielding Percentage', 2)
    win_percentages = standardize(win_percentages)
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
    standardized_matrix = np.vstack([
        win_percentages, runs, batting_walks, strikeouts, stolen_bases, batting_average,
        on_base_percentage, slugging_percentage, innings_pitched, hits, pitching_walks,
        strikeouts_through_nine, earned_run_average, whip, fielding_percentage
    ])
    assert standardized_matrix.shape == (15, 45), 'input matrix incorrect size'
    pca = PCA(n_components=2)
    pca_transformed_data = pca.fit_transform(standardized_matrix.T)
    fig, ax = plt.subplots()
    ax.scatter(pca_transformed_data[:, 0], pca_transformed_data[:, 1])
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA')
    plt.show()
if __name__ == "__main__":
    main()