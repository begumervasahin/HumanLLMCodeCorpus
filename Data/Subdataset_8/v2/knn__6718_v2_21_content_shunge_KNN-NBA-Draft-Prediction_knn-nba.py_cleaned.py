from sklearn.neighbors import KNeighborsClassifier
import numpy as np
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0
def get_label_for_pick(pick_number):
    label_distribution = [
        "Top 10 picks", "Mid 1st round", "Late 1st round",
        "Early 2nd round", "Mid 2nd round", "Late 2nd round/undrafted"
    ]
    return label_distribution[(pick_number - 1)
nba_stats = []
nba_labels = []
for year in range(1999, 2017):
    filename = f"{year}.txt"
    with open(filename, "r") as file:
        for line in file.readlines()[2:]:
            if not line.split(",")[11]:
                continue
            stat_list = line.split(",")
            stat = [
                convert_to_float(stat_list[18]),
                convert_to_float(stat_list[20]) * 20,
                convert_to_float(stat_list[21])
            ]
            nba_stats.append(np.array(stat))
            nba_labels.append(get_label_for_pick(int(stat_list[1])))
test_year = "2003"
test_data = []
with open(f"{test_year}.txt", "r") as file:
    for line in file.readlines()[2:60]:
        stat_list = line.split(",")
        stat = [
            convert_to_float(stat_list[18]),
            convert_to_float(stat_list[20]) * 20,
            convert_to_float(stat_list[21])
        ]
        test_data.append(np.array(stat))
neigh = KNeighborsClassifier(n_neighbors=50)
neigh.fit(nba_stats, np.array(nba_labels))
for stat in test_data:
    print(neigh.predict([stat]))