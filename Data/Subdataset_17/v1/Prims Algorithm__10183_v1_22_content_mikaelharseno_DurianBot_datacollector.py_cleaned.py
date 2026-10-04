import networkx as nx
from math import ceil
import random
import numpy as np
def solve(client):
    matrix = []
    for _ in range(90):
        client.start()
        graph = client.G
        locations = list(graph.nodes())
        numlocations = len(locations)
        print("numlocations is", str(numlocations))
        all_students = list(range(1, client.students + 1))
        numstudents = client.students
        print("num students is", str(numstudents))
        minNumTruth = ceil(numlocations / 2)
        numTruth = [0 for _ in range(numstudents)]
        numLies = [0 for _ in range(numstudents)]
        loc = list(range(numlocations))
        random.shuffle(loc)
        for randomloc in loc:
            temp_locations = client.scout(locations[randomloc], all_students)
            if temp_locations is None:
                continue
            studentreports = list(temp_locations.values())
            target = locations[randomloc]
            nextEdges = list(graph.edges(target, data='weight', default=0))
            minEdgeIndex = 0
            minEdge = float('inf')
            for i in range(len(nextEdges)):
                if nextEdges[i][2] < minEdge:
                    minEdge = nextEdges[i][2]
                    minEdgeIndex = i
            actualvalue = int(client.remote(target, nextEdges[minEdgeIndex][1]))
            for i in range(numstudents):
                studentreport = int(studentreports[i])
                if studentreport == actualvalue:
                    numTruth[i] += 1
                else:
                    numLies[i] -= 1
                worstcaseprob = (minNumTruth - numTruth[i]) / (numlocations - numTruth[i] - numLies[i])
                matrix.append([worstcaseprob, studentreport, actualvalue])
        client.end()
    np.savetxt("results.txt", np.array(matrix, np.float64))
    client.end()
