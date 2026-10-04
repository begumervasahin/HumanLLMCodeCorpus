import glob
import time
import networkx as nx
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def analyze_network_files(normal_path, abnormal_path):
    normal_files = glob.glob(f"{normal_path}/*.gml")
    analysis_times = []
    for file in normal_files:
        start_time = time.time()
        print(f'Analyzing file: {file}')
        network = nx.read_gml(file)
        score_set, score_com = ASG.Detection_Outliers(network)
        elapsed_time = time.time() - start_time
        analysis_times.append(elapsed_time)
    min_time = min(analysis_times)
    max_time = max(analysis_times)
    avg_time = mean(analysis_times)
    total_time = sum(analysis_times)
    print(f'Minimum analysis time: {min_time:.4f} seconds')
    print(f'Average analysis time: {avg_time:.4f} seconds')
    print(f'Maximum analysis time: {max_time:.4f} seconds')
    print(f'Total analysis time: {total_time:.4f} seconds')
if __name__ == "__main__":
    normal_path = 'Normal_Example'
    abnormal_path = 'Abnormal_Example'
    analyze_network_files(normal_path, abnormal_path)