import time
import csv
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import median, mean
from datetime import datetime
def main():
    filenames = ['device_data.csv', 'cookie_data.csv']
    all_user_id, all_user_time_info = extract_user_time(filenames)
    all_user_info = extract_user_Devices_info(all_user_id, filenames)
    all_time = ['201705040913', '201705040932', ...]
    median_deltaT = find_median_delta_T(all_time)
    print("Median Delta T:", median_deltaT)
    deltaT = 60 * 60
    time_group = generate_time_group(all_time, deltaT)
    print("Time Group:", time_group)
    user = random.choice(list(all_user_info.keys()))
    current_user_info = all_user_info[user]
    grouped_devices_dict = extract_devices_behavior_on_time_group(time_group, current_user_info)
    print("Grouped Devices Dictionary for User", user, ":", grouped_devices_dict)
    d1 = random.choice(list(grouped_devices_dict.keys()))
    d2 = random.choice(list(grouped_devices_dict.keys()))
    weight = calculate_devices_weight(d1, d2, grouped_devices_dict)
    print("Weight between", d1, "and", d2, ":", weight)
    median_T = median_deltaT
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    user_idx = 0
    graph = nx.Graph()
    draw_graph(median_T, current_time, user_idx, user, graph)
if __name__ == "__main__":
    main()