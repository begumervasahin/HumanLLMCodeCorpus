
from math import inf
def fonk1(b4 , n):
    b1 = []
    for b3 in range(n+1):
        b1.append([])
        for j in range(n+1):
            b1[b3].append([])
            for b2 in range(2):
                b1[b3][j].append(0)
                if b2 = = 0:
                    if b3 = = j:
                        b1[b3][j][0] = 0
                    elif b4.get((b3,j)) != None:
                        b1[b3][j][0] = b4[(b3,j)]
                    else:
                        b1[b3][j][0] = inf
    a1 = inf
    for b2 in range(1,n+1):
        for b3 in range(1,n+1):
            for j in range(1,n+1):
                b1[b3][j][1] = min(b1[b3][j][0] , b1[b3][b2][0] + b1[b2][j][0])
                if b2 = = n:
                    if a1 > b1[b3][j][1]:
                        a1 = b1[b3][j][1]
                if b3 = = j:
                   if b1[b3][j][1]<0:
                       return 'NULL'
                b1[b3][j][1] , b1[b3][j][0] = b1[b3][j][0] ,b1[b3][j][1]
    return a1
b4 = {}
with open('g3.txt') as f:
    b5 = f.readline()
    num_of_vertices , b6 = list(map(int,b5.split()))
    b7 = f.readlines()
    for line in b7:
        b8 = list(map(int,line.split()))
        if b4.get((b8[0],b8[1])) == None:
            b4[(b8[0],b8[1])] = b8[2]
        else:
            if b4[(b8[0],b8[1])] > b8[2]:
                b4[(b8[0],b8[1])] = b8[2]
f.close()
print(fonk1(b4, num_of_vertices))