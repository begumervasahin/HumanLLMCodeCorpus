from sklearn.neighbors import KNeighborsClassifier
import numpy as np
def convert_num(num):
    try:
        return float(num)
    except ValueError:
        return 0
def return_label(num):
    label_dist = ["Top 10 picks", "Mid 1st round", "Late 1st round",
                  "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"]
    return label_dist[(num - 1)
def read_nba_stats(start_year, end_year):
    nba_stat = []
    nba_labels = []
    for i in range(start_year, end_year + 1):
        filename = str(i) + ".txt"
        with open(filename, "r") as file:
            for line in file.readlines()[2:]:
                if line.split(",")[11] == "":
                    continue
                stat_list = line.split(",")
                stat = [
                    convert_num(stat_list[18]),
                    convert_num(stat_list[20]) * 20,
                    convert_num(stat_list[21])
                ]
                nba_stat.append(np.array(stat))
                nba_labels.append(return_label(int(stat_list[1])))
    return nba_stat, nba_labels
def predict_labels(test_year, nba_stat, nba_labels):
    with open(test_year + ".txt", "r") as file:
        for line in file.readlines()[2:60]:
            print([line.split(",")[3]])
            stat_list = line.split(",")
            stat = [
                convert_num(stat_list[18]),
                convert_num(stat_list[20]) * 20,
                convert_num(stat_list[21])
            ]
            neigh = KNeighborsClassifier(n_neighbors=50)
            neigh.fit(nba_stat, np.array(nba_labels))
            print(neigh.predict([np.array(stat)]))
def main():
    start_year = 1999
    end_year = 2016
    nba_stat, nba_labels = read_nba_stats(start_year, end_year)
    test_year = "2003"
    predict_labels(test_year, nba_stat, nba_labels)
if __name__ == '__main__':
    main()