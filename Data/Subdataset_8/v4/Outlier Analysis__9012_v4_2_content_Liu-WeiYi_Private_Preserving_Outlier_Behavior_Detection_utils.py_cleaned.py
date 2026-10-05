import time
import csv
import json
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
from statistics import median, mean
from datetime import datetime
def to_second(time_str):
    format_time_str = "%s-%s-%s %s:%s:%s" % (
        time_str[0:4],
        time_str[4:6],
        time_str[6:8],
        time_str[8:10],
        time_str[10:12],
        time_str[12:]
    )
    seconds = datetime.strptime(format_time_str, "%Y-%m-%d %H:%M:%S")
    return time.mktime(seconds.timetuple())
def find_median_delta_T(all_time):
    all_delta_T = []
    for t1_idx in range(len(all_time) - 1):
        t1 = to_second(all_time[t1_idx])
        t2 = to_second(all_time[t1_idx + 1])
        all_delta_T.append(abs(t2 - t1))
    all_delta_T = [i for i in all_delta_T if i != 0]
    if all_delta_T == []:
        all_delta_T = [0]
    return mean(all_delta_T)
def generate_time_group(all_time, deltaT):
    interval_count = 1
    interval_dict = {}
    t1_idx = 0
    last_one_hit = False
    while t1_idx < len(all_time):
        t2_idx = t1_idx + 1
        if t2_idx >= len(all_time):
            break
        t1 = all_time[t1_idx]
        t2 = all_time[t2_idx]
        group = set()
        while abs(to_second(t1) - to_second(t2)) <= deltaT:
            group.add(t1)
            group.add(t2)
            t1_idx += 1
            if all_time[t1_idx] == all_time[-1]:
                last_one_hit = True
            t2_idx += 1
            if t2_idx >= len(all_time):
                interval_dict[interval_count] = list(group)
                interval_count += 1
                t1_idx = t2_idx
                break
            t1 = all_time[t1_idx]
            t2 = all_time[t2_idx]
        interval_dict[interval_count] = list(group)
        interval_count += 1
        t1_idx = t2_idx
    if not last_one_hit:
        interval_dict[interval_count] = [all_time[-1]]
    return interval_dict
