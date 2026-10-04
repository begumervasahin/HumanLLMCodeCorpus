import glob
import time
import networkx as nx
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
def fonk2(b1):
    b5 = min(b1)
    b6 = max(b1)
    b7 = mean(b1)
    b8 = sum(b1)
    print(f'Minimum analysis time: {b5:.2f} seconds')
    print(f'Average analysis time: {b7:.2f} seconds')
    print(f'Maximum analysis time: {b6:.2f} seconds')
    print(f'Total analysis time: {b8:.2f} seconds')
def fonk3(b13, b14):
    b9 = glob.glob(f'{b13}/*.gml')
    b10 = glob.glob(f'{b14}/*.gml')
    b11 = fonk1(b9, ASG.Detection_Outliers)
    fonk2(b11)
if b12 = = "__main__":
    b13 = 'Normal_Example'
    b14 = 'Abnormal_Example'
    fonk3(b13, b14)