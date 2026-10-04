import glob
import time
import networkx as nx
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def fonk1(b12, b13):
    b1 = glob.glob(f"{b12}/*.gml")
    b2 = []
    for file in b1:
        b3 = time.time()
        print(f'Analyzing file: {file}')
        b4 = nx.read_gml(file)
        score_set, b5 = ASG.Detection_Outliers(b4)
        b6 = time.time() - b3
        b2.append(b6)
    b7 = min(b2)
    b8 = max(b2)
    b9 = mean(b2)
    b10 = sum(b2)
    print(f'Minimum analysis time: {b7:.4f} seconds')
    print(f'Average analysis time: {b9:.4f} seconds')
    print(f'Maximum analysis time: {b8:.4f} seconds')
    print(f'Total analysis time: {b10:.4f} seconds')
if b11 = = "__main__":
    b12 = 'Normal_Example'
    b13 = 'Abnormal_Example'
    fonk1(b12, b13)