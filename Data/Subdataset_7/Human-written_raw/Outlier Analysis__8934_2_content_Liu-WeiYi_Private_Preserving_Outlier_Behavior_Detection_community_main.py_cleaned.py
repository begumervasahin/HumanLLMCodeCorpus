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
    b1 = glob.glob(b13+'/*.gml')
    b2 = glob.glob(b14+'/*.gml')
    b3 = []
    for file in b1:
        b4 = time.time()
        print('current file:\t', file)
        b5 = nx.read_gml(file)
        score_set, b6 = ASG.Detection_Outliers(b5)
        b7 = time.time()-b4
        b3.append(b7)
    b8 = min(b3)
    b9 = max(b3)
    b10 = mean(b3)
    b11 = sum(b3)
    print('b8:   ',b8)
    print('b10:   ',b10)
    print('b9:   ',b9)
    print('b11:   ',b11)
if b12 = = "__main__":
    b13 = 'Normal_Example'
    b14 = 'Abnormal_Example'
    b15 = "Nodes"
    fonk1(b13, b14, b15)