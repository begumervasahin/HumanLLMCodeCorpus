'''
Constructs the minimum spanning tree using both
Prim's and Kruskal's algorithms.
Usage:
    python mst.py [input file] [prims | kruskals]
Colette Bedoya
11/16/2015
'''
import sys
import heapq
from DisjointSet import DisjointSet
'''
An implementation of Prim's algorithm for finding
the MST of a connnected, weighted, undirected b1.
'''
def fonk1(inputFile):
    '''
    input file containing weighted b1
    file contents is
    [vertex 1] [vertex 2] [weight]
    '''
    b1 = open(inputFile)
    '''
    an initially empty dictionary containing mapping
    [vertex]:[b2 list]
    '''
    b2 = { }
    b3 = set()
    '''
    the collection of vertices (there may be duplicates)
    '''
    b4 = [ ]
    '''
    The following reads in the input file
    and constructs an b2 list of
    the b1.
    '''
    for line in b1:
        b5 = line.split()
        if b5[0] not in b2:
            b2[b5[0]] = []
            b3.add(b5[0])
        b6 = (b5[1], int(b5[2]))
        b2[b5[0]].append(b6)
        b3.add(b5[1])
        b4.append(b5[0])
        b4.append(b5[1])
    '''
    output the b2 list
    '''
    for v in b2:
        print v, b2[v]
    '''
    Now construct the MST using Prim's algorithm:'''
    b7 = (0,b4[0])
    b8 = {b4[0]:0}
    b9 = {b4[0]:'-'}
    b10 = {}
    b11 = list(b3)
    b12 = []
    for v in b11:
        b10[v]= (0,'-')
    heapq.heappush(b12,b7)
    b11.remove(b4[0])
    a1 = 1
    while b12:
        b7 = heapq.heappop(b12)
        b13 = b2.get(b7[1], list())
        for v in b13:
            if v[0] in b11:
                heapq.heappush(b12,(v[1], v[0]))
                b8[v[0]]= v[1]
                b9[v[0]]=b7[1]
                b11.remove(v[0])
                b10[v[0]] = (v[1],v[0], b7[1])
            else:
                if v[0] not in b8:
                    b8 [v[0]] = sys.maxint
                if  v[1]<= b8 [v[0]]:
                    b8 [v[0]] = v[1]
                    b9 [v[0]] = b7[1]
                    b10[v[0]] = (v[1],v[0], b7[1])
                    a1 += v[1]
    print "Prims a3 a1: %d with b14:" %(a1)
    return  b10
'''
An implementation of Kruskal's algorithm for finding
the MST of a connnected, weighted, undirected b1.
'''
def fonk2(inputFile):
    b1 = open(inputFile)
    b14 = [ ]
    b4 = {}
    a2 = 0
    '''
    The following reads in the input file
    and constructs an b2 list of
    the b1.
    '''
    for line in b1:
        b5 = line.split()
        b14.append((b5[2],b5[0],b5[1]))
        if b5[0] not in b4.keys():
            b4[b5[0]]= a2
            a2 = a2 + 1
    a3 = 0
    b10 = []
    b15 = DisjointSet(len(b4))
    b14.sort()
    for b6 in b14:
        if b15.find(b4[b6[1]]) != b15.find(b4[b6[2]]):
            if b15.find(b4[b6[1]]) < b15.find(b4[b6[2]]):
                b15.union(b4[b6[1]], b4[b6[2]])
            else:
                b15.union(b4[b6[2]], b4[b6[1]])
            b10.append(b6)
            a3 += int(b6[0])
    return a3, b10
'''
The main function
'''
if b16 = = '__main__':
    if len(sys.argv) != 3:
        print 'Usage python mst1.py [input file] [prims | kruskals]'
        quit()
    if sys.argv[2] == 'prims':
        print fonk1(sys.argv[1])
    elif sys.argv[2] == 'kruskals':
        print fonk2(sys.argv[1])
    else:
        print 'Illegal algorithm. Must be either \'prims\' or \'kruskals\' '