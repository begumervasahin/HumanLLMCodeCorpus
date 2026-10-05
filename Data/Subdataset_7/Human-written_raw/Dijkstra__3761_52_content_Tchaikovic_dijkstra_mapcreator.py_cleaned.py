import os
import csv
import numpy as np
def fonk1(coordinates_directory):
    b1 = []
    for filename in os.listdir(coordinates_directory):
        b2 = open(coordinates_directory+'/'+filename, 'r')
        b3 = csv.b3(b2, delimiter=',')
        b4 = []
        for b5 in b3:
            b5 = [x.strip(' ') for x in b5]
            b4 = b4+b5
            b1 = b1+b4
        b6 = filter(lambda a: a != '', b1)
    b7 = [[0 for x in range(len(b6))] for y in range(2)]
    for i in range(len(b6)):
        b7[0][i]= int(b6[i][1:].split("y")[0])
        b7[1][i] = int(b6[i][1:].split("y")[1])
    b8 = [["." for x in range(max(b7[0])+1)] for y in range(max(b7[1])+1)]
    for i in range(len(b7[0])):
        b8[b7[1][i]][b7[0][i]]="x"
    print b8
    b9 = open('b8.txt', 'w')
    for item in b8:
        b9.write("%s\n" % item)
    b10 = b8
    return b10
fonk1("CoordinateSystem")