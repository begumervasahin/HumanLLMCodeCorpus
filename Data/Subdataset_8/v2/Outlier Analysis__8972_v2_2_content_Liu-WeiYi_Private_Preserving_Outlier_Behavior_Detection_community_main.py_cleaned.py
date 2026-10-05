import sys
import os
import glob
import json
import pickle
import time
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def main(normal_path, abnormal_path, synthetic_type):
    normal_files = glob.glob(normal_path + '/*.gml')
    abnormal_files = glob.glob(abnormal_path + '/*.gml')
    analysis_time = []
    for file in normal_files:
        start_time = time.time()
        print('Analyzing file:', file)
        network = nx.read_gml(file)
        score_set, score_com = ASG.Detection_Outliers(network)
        time_interval = time.time() - start_time
        analysis_time.append(time_interval)
    min_time = min(analysis_time)
    max_time = max(analysis_time)
    avg_time = mean(analysis_time)
    sum_time = sum(analysis_time)
    print('Min time:', min_time)
    print('Avg time:', avg_time)
    print('Max time:', max_time)
    print('Sum time:', sum_time)
if __name__ == "__main__":
    normal_path = 'Normal_Example'
    abnormal_path = 'Abnormal_Example'
    synthetic_type = "Nodes"
    main(normal_path, abnormal_path, synthetic_type)