import glob
import time
import networkx as nx
import matplotlib.pyplot as plt
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def fonk1(file_paths, detection_function):
    b1 = []
    for file_path in file_paths:
        b2 = time.time()
        print(f'Analyzing file: {file_path}')
        b3 = nx.read_gml(file_path)
        score_set, b4 = detection_function(b3)
        b1.append(time.time() - b2)
    return b1
def fonk2(b13, b14):
    b5 = glob.glob(f'{b13}/*.gml')
    b6 = glob.glob(f'{b14}/*.gml')
    b7 = fonk1(b5, ASG.Detection_Outliers)
    b8 = min(b7)
    b9 = max(b7)
    b10 = mean(b7)
    b11 = sum(b7)
    print(f'Minimum analysis time: {b8:.2f} seconds')
    print(f'Average analysis time: {b10:.2f} seconds')
    print(f'Maximum analysis time: {b9:.2f} seconds')
    print(f'Total analysis time: {b11:.2f} seconds')
if b12 = = "__main__":
    b13 = 'Normal_Example'
    b14 = 'Abnormal_Example'
    fonk2(b13, b14)