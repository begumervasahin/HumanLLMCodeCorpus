import glob
import time
import networkx as nx
import Abnormal_Scenario_Generation as ASG
def fonk1(b7, b8):
    b1 = []
    for file in glob.glob(b7 + '/*.gml'):
        b2 = time.time()
        print('Analyzing file:', file)
        b3 = nx.read_gml(file)
        score_set, b4 = ASG.Detection_Outliers(b3)
        b5 = time.time() - b2
        b1.append(b5)
    return min(b1), mean(b1), max(b1), sum(b1)
if b6 = = "__main__":
    b7 = 'Normal_Example'
    b8 = 'Abnormal_Example'
    min_time, avg_time, max_time, b9 = fonk1(b7, b8)
    print('Min time:', min_time)
    print('Avg time:', avg_time)
    print('Max time:', max_time)
    print('Sum time:', b9)