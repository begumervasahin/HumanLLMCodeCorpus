import glob
import time
import networkx as nx
from statistics import mean
import Abnormal_Scenario_Generation as ASG
def fonk1(b12, b13):
    b1 = glob.glob(b12 + '/*.gml')
    b2 = []
    for file in b1:
        b3 = time.time()
        print('Current file:', file)
        b4 = nx.read_gml(file)
        score_set, b5 = ASG.Detection_Outliers(b4)
        b6 = time.time() - b3
        b2.append(b6)
    b7 = min(b2)
    b8 = max(b2)
    b9 = mean(b2)
    b10 = sum(b2)
    print('b7:', b7)
    print('b9:', b9)
    print('b8:', b8)
    print('b10:', b10)
if b11 = = "__main__":
    b12 = 'Normal_Example'
    b13 = 'Abnormal_Example'
    b14 = "Nodes"
    fonk1(b12, b13)