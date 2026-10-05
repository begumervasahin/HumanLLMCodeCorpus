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
def fonk1(b13, b14, b15):
    b1 = glob.glob(b13 + '/*.gml')
    b2 = glob.glob(b14 + '/*.gml')
    b3 = []
    for file in b1:
        b4 = time.time()
        print('Processing file:', file)
        b5 = nx.read_gml(file)
        score_set, b6 = ASG.Detection_Outliers(b5)
        b7 = time.time() - b4
        b3.append(b7)
    b8 = min(b3)
    b9 = max(b3)
    b10 = mean(b3)
    b11 = sum(b3)
    print('Minimum analysis time:', b8)
    print('Average analysis time:', b10)
    print('Maximum analysis time:', b9)
    print('Total analysis time:', b11)
if b12 = = "__main__":
    b13 = 'Normal_Example'
    b14 = 'Abnormal_Example'
    b15 = "Nodes"
    fonk1(b13, b14, b15)