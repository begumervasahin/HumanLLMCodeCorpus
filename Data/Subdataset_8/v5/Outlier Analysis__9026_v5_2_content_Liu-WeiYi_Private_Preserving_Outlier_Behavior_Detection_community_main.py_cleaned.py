import sys
import os
import glob
import time
import networkx as nx
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def main(normal_path, abnormal_path, synthetic_type):
    normal_files = glob.glob(os.path.join(normal_path, '*.gml'))
    abnormal_files = glob.glob(os.path.join(abnormal_path, '*.gml'))
    analysis_times = []
    for file in normal_files:
        start_time = time.time()
        print('Processing file:', file)
        network = nx.read_gml(file)
        score_set, score_com = ASG.Detection_Outliers(network)
        time_interval = time.time() - start_time
        analysis_times.append(time_interval)
    min_time = min(analysis_times)
    max_time = max(analysis_times)
    avg_time = mean(analysis_times)
    total_time = sum(analysis_times)
    print('Minimum analysis time:', min_time)
    print('Average analysis time:', avg_time)
    print('Maximum analysis time:', max_time)
    print('Total analysis time:', total_time)
if __name__ == "__main__":
    normal_path = 'Normal_Example'
    abnormal_path = 'Abnormal_Example'
    synthetic_type = "Nodes"
    main(normal_path, abnormal_path, synthetic_type)