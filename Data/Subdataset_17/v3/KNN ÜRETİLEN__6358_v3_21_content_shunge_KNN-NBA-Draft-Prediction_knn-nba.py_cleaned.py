import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def convert_to_number(num):
    try:
        return float(num)
    except ValueError:
        return 0
def assign_label(num):
    label_distribution = [
        "Top 10 picks", "Mid 1st round", "Late 1st round",
        "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"
    ]
    return label_distribution[(num - 1)
def read_nba_stats(filename):
    stats = []
    labels = []
    with open(filename, "r") as file:
        for line in file.readlines()[2:]:
            if line.split(",")[11] == "":
                continue
            stat_list = line.split(",")
            player_stats = [
                convert_to_number(stat_list[18]),
                convert_to_number(stat_list[20]) * 20,
                convert_to_number(stat_list[21])
            ]
            stats.append(np.array(player_stats))
            labels.append(assign_label(int(stat_list[1])))
    return stats, labels
nba_stats = []
nba_labels = []
for year in range(1999, 2017):
    filename = f"{year}.txt"
    yearly_stats, yearly_labels = read_nba_stats(filename)
    nba_stats.extend(yearly_stats)
    nba_labels.extend(yearly_labels)
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(nba_stats, np.array(nba_labels))
def test_model(year):
    filename = f"{year}.txt"
    with open(filename, "r") as file:
        for line in file.readlines()[2:60]:
            player_name = line.split(",")[3]
            print(player_name)
            stat_list = line.split(",")
            player_stats = [
                convert_to_number(stat_list[18]),
                convert_to_number(stat_list[20]) * 20,
                convert_to_number(stat_list[21])
            ]
            prediction = knn.predict([np.array(player_stats)])
            print(prediction[0])
test_model(2003)
new_stats = [convert_to_number('22.5'), convert_to_number('8.2') * 20, convert_to_number('1.5')]
prediction = knn.predict([np.array(new_stats)])
print("Prediction for new stats:", prediction[0])