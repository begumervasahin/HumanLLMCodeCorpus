def fonk1(b2):
    a1 = 1000
    b1 = None
    for key in b2:
        if b2[key] < a1:
            a1 = b2[key]
            b1 = key
    del b2[b1]
    return b1
def fonk2(b8, start):
    b2 = {}
    b3 = {}
    b4 = {}
    for v in b8:
        b3[v] = 1000
        b4[v] = -1
    b3[start] = 0
    for v in b8:
       b2[v] = b3[v]
    while b2:
        b5 = fonk1(b2)
        for v in b8[b5].keys():
            b6 = b8[b5][v]
            b7 = b3[b5] + b6
            if (b7 < b3[v]):
                b2[v] = b7
                b3[v] = b7
                b4[v] = b5
    return b3, b4
b8 = {
    0 : {1:6, 2:1, 3:4},
    1 : {4:3},
    2 : {1:-3, 3:2},
    3 : {4:-1},
    4 : {2:5},
}
b3, b4 = fonk2(b8, 0)
print ("Shortest distance from start node 0 to all other nodes is:")
for v in b3:
    print (v,'=',b3[v])
print ("Paths from start noe to all other nodes (predecessors of nodes):")
for v in b4:
    print (v,'=',b4[v])