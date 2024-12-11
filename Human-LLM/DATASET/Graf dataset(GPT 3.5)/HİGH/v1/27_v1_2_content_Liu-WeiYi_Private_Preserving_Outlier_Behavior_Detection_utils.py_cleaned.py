import time
import csv
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import median, mean
from datetime import datetime
def fonk1():
    b1 = ['device_data.csv', 'cookie_data.csv']
    all_user_id, b2 = extract_user_time(b1)
    b3 = extract_user_Devices_info(all_user_id, b1)
    b4 = ['201705040913', '201705040932', ...]
    b5 = find_median_delta_T(b4)
    print("Median Delta T:", b5)
    b6 = 60 * 60
    b7 = generate_time_group(b4, b6)
    print("Time Group:", b7)
    b8 = random.choice(list(b3.keys()))
    b9 = b3[b8]
    b10 = extract_devices_behavior_on_time_group(b7, b9)
    print("Grouped Devices Dictionary for User", b8, ":", b10)
    b11 = random.choice(list(b10.keys()))
    b12 = random.choice(list(b10.keys()))
    b13 = calculate_devices_weight(b11, b12, b10)
    print("Weight between", b11, "and", b12, ":", b13)
    b14 = b5
    b15 = datetime.now().strftime("%Y%m%d%H%M%S")
    a1 = 0
    b16 = nx.Graph()
    draw_graph(b14, b15, a1, b8, b16)
if b17 = = "__main__":
    fonk1()