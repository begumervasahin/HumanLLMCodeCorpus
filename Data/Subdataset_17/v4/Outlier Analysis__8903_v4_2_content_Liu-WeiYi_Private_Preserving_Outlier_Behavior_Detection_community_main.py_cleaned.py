import glob
import time
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def analyze_files(file_paths, detection_function):
    analysis_times = []
    for file_path in file_paths:
        start_time = time.time()
        print(f'Analyzing file: {file_path}')
        network = nx.read_gml(file_path)
        score_set, score_com = detection_function(network)
        analysis_times.append(time.time() - start_time)
    return analysis_times
def main(normal_path, abnormal_path):
    normal_files = glob.glob(f'{normal_path}/*.gml')
    abnormal_files = glob.glob(f'{abnormal_path}/*.gml')
    normal_analysis_times = analyze_files(normal_files, ASG.Detection_Outliers)
    min_time = min(normal_analysis_times)
    max_time = max(normal_analysis_times)
    avg_time = mean(normal_analysis_times)
    sum_time = sum(normal_analysis_times)
    print(f'Minimum analysis time: {min_time:.2f} seconds')
    print(f'Average analysis time: {avg_time:.2f} seconds')
    print(f'Maximum analysis time: {max_time:.2f} seconds')
    print(f'Total analysis time: {sum_time:.2f} seconds')
if __name__ == "__main__":
    normal_path = 'Normal_Example'
    abnormal_path = 'Abnormal_Example'
    main(normal_path, abnormal_path)