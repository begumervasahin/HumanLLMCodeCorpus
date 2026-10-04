from sklearn.neighbors import KNeighborsClassifier
import numpy as np
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
nba_stats = []
nba_labels = []
for year in range(1999, 2017):
    filename = str(year) + ".txt"
    with open(filename, "r") as file:
        for line in file.readlines()[2:]:
            if line.split(",")[11] == "":
                continue
            stat_list = line.split(",")
            stats = [
                convert_to_number(stat_list[18]),
                convert_to_number(stat_list[20]) * 20,
                convert_to_number(stat_list[21])
            ]
            nba_stats.append(np.array(stats))
            nba_labels.append(assign_label(int(stat_list[1])))
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(nba_stats, np.array(nba_labels))
test_year = "2003"
with open(test_year + ".txt", "r") as file:
    for line in file.readlines()[2:60]:
        print([line.split(",")[3]])
        stat_list = line.split(",")
        stats = [
            convert_to_number(stat_list[18]),
            convert_to_number(stat_list[20]) * 20,
            convert_to_number(stat_list[21])
        ]
        prediction = knn.predict([np.array(stats)])
        print(prediction[0])
new_stats = [convert_to_number('22.5'), convert_to_number('8.2') * 20, convert_to_number('1.5')]
print("Prediction for new stats:", knn.predict([np.array(new_stats)]))