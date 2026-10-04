import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def convert_num(num):
    try:
        return float(num)
    except ValueError:
        return 0
def return_label(num):
    label_dist = ["Top 10 picks", "Mid 1st round", "Late 1st round",
                  "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"]
    return label_dist[(num - 1)
def extract_stats(stat_list):
    stats = [
        convert_num(stat_list[18]),
        convert_num(stat_list[20]) * 20,
        convert_num(stat_list[21])
    ]
    return np.array(stats)
nba_stats = []
nba_labels = []
for year in range(1999, 2017):
    filename = f"{year}.txt"
    with open(filename, "r") as file:
        for line in file.readlines()[2:]:
            stat_list = line.split(",")
            if stat_list[11] == "":
                continue
            nba_stats.append(extract_stats(stat_list))
            nba_labels.append(return_label(int(stat_list[1])))
test_year = 2003
filename = f"{test_year}.txt"
with open(filename, "r") as file:
    for line in file.readlines()[2:60]:
        stat_list = line.split(",")
        player_name = stat_list[3]
        player_stats = extract_stats(stat_list)
        knn = KNeighborsClassifier(n_neighbors=50)
        knn.fit(nba_stats, np.array(nba_labels))
        prediction = knn.predict([player_stats])
        print(f"Player: {player_name}, Prediction: {prediction[0]}")