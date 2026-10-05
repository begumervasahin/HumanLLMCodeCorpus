import argparse
import os
import re
import sys
import time
import timeit
parser=argparse.ArgumentParser(description='Calculate the shortest path between all pairs of vertices in a graph')
parser.add_argument('--algorithm',default='a',\
    help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
parser.add_argument('-v','--verbose',action='store_true')
parser.add_argument('--profile',action='store_true')
parser.add_argument('filename',metavar='<filename>',help='Input file containing graph')
graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")
vertices=[]
edges=[]
def BellmanFord(G):
    pathPairs=[]
    for source in range(0, len(G[0])):
        d = [float("inf")] * len(G[0])
        d[source] = 0.0
        for iteration in range(0, len(G[0])-1):
            for current in range(0, len(G[0])):
                for otherVertex in range(0, len(G[1])):
                    if d[otherVertex] > float(d[current]) + float(G[1][current][otherVertex]):
                        d[otherVertex] = float(d[current]) + float(G[1][current][otherVertex])
        for current in range(0, len(G[0])):
            for otherVertex in range(0, len(G[1])):
                if d[otherVertex] > float(d[current]) + float(G[1][current][otherVertex]):
                    return (pathPairs,False)
        pathPairs.append(d)
    return (pathPairs,True)
def FloydWarshall(G):
    pathPairs=[]
    CopyG = G
    for x in range(0,len(G[0])):
        CopyG[1][x][x] = 0
    for i in range(0, len(G[0])):
        for j in range(0, len(G[0])):
            for iteration in range(0, len(G[0])):
                CopyG[1][j][iteration] = min(float(CopyG[1][j][iteration]), float(CopyG[1][j][i]) + float(CopyG[1][i][iteration]))
    pathPairs = CopyG[1]
    return pathPairs
def readFile(filename):
    global vertices
    global edges
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)-1][int(sink)-1]=weight
    G = (vertices,edges)
    return (vertices,edges)
def matrixEquality(a,b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i,row in enumerate(a):
        for j,value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def main(filename,algorithm):
    G=readFile(filename)
    pathPairs = []
    noCycle = True
    if algorithm == 'b' or algorithm == 'B':
        startTimer = timeit.default_timer()
        pathPairs = BellmanFord(G)
        stopTimer = timeit.default_timer()
        print(stopTimer - startTimer)
        noCycle = pathPairs[1]
        pathPairs = pathPairs[0]
    if algorithm == 'f' or algorithm == 'F':
        startTimer = timeit.default_timer()
        pathPairs = FloydWarshall(G)
        stopTimer = timeit.default_timer()
        print(stopTimer - startTimer)
    if algorithm == 'a':
        print('running both')
        pathPairsBellman = BellmanFord(G)
        pathPairsFloyd = FloydWarshall(G)
        pathPairs = pathPairsBellman[0]
        pathPairs = pathPairsFloyd
        noCycle = pathPairsBellman[1]
        if not matrixEquality(pathPairsBellman,pathPairsFloyd) or noCycle == False:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0]+'_shortestPaths.txt','w') as f:
        if noCycle == False:
            f.write("Negative Cycle Detected \n")
        for row in pathPairs:
            for weight in row:
                f.write(str(weight)+' ')
            f.write('\n')
if __name__ == '__main__':
    args=parser.parse_args()
    main(args.filename,args.algorithm)