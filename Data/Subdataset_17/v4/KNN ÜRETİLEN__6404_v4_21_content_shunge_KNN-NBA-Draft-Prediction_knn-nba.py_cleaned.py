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
nba_stats = []
nba_labels = []
for year in range(1999, 2017):
    filename = f"{year}.txt"
    with open(filename, "r") as file:
        for line in file.readlines()[2:]:
            stat_list = line.split(",")
            if stat_list[11] == "":
                continue
            stat = []
            stat.append(convert_num(stat_list[18]))
            stat.append(convert_num(stat_list[20]) * 20)
            stat.append(convert_num(stat_list[21]))
            nba_stats.append(np.array(stat))
            nba_labels.append(return_label(int(stat_list[1])))
test_year = 2003
filename = f"{test_year}.txt"
with open(filename, "r") as file:
    for line in file.readlines()[2:60]:
        print(line.split(",")[3])
        stat_list = line.split(",")
        stat = []
        stat.append(convert_num(stat_list[18]))
        stat.append(convert_num(stat_list[20]) * 20)
        stat.append(convert_num(stat_list[21]))
        knn = KNeighborsClassifier(n_neighbors=50)
        knn.fit(nba_stats, np.array(nba_labels))
        prediction = knn.predict([np.array(stat)])
        print(prediction)