import argparse
import os
import re
import sys
import time
from allPairsShortestPath import graphRE, edgeRE
def fonk1(filename):
    global b4
    global b5
    b1 = open(filename,'r')
    b2 = b1.readline()
    b3 = graphRE.match(b2)
    if not b3:
        print(b2+" not properly formatted")
        quit(1)
    b4 = list(range(int(b3.group(1))))
    b5 = []
    for i in range(len(b4)):
        b6 = []
        for j in range(len(b4)):
            b6.append(float("inf"))
        b5.append(b6)
    for b7 in b1.readlines():
        b7 = b7.strip()
        b8 = edgeRE.match(b7)
        if b8:
            b9 = b8.group(1)
            b10 = b8.group(2)
            if int(b9) > len(b4) or int(b10) > len(b4):
                print("Attempting to insert an edge between "+b9+" and "+b10+" in a graph with "+b4+" b4")
                quit(1)
            b11 = b8.group(3)
            b5[int(b9)-1][int(b10)-1]=b11
    b12 = (b4,b5)
    return (b4,b5)