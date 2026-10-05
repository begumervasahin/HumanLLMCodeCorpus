import glob
import time
import networkx as nx
import Abnormal_Scenario_Generation as ASG
def analyze_files(normal_path, abnormal_path):
    analysis_time = []
    for file in glob.glob(normal_path + '/*.gml'):
        start_time = time.time()
        print('Analyzing file:', file)
        network = nx.read_gml(file)
        score_set, score_com = ASG.Detection_Outliers(network)
        time_interval = time.time() - start_time
        analysis_time.append(time_interval)
    return min(analysis_time), mean(analysis_time), max(analysis_time), sum(analysis_time)
if __name__ == "__main__":
    normal_path = 'Normal_Example'
    abnormal_path = 'Abnormal_Example'
    min_time, avg_time, max_time, sum_time = analyze_files(normal_path, abnormal_path)
    print('Min time:', min_time)
    print('Avg time:', avg_time)
    print('Max time:', max_time)
    print('Sum time:', sum_time)