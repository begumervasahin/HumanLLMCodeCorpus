import math
import urllib.request
import json
import re
def fonk1():
    b1 = {}
    b2 = urllib.request.urlopen("http:
    b3 = json.loads(b2.read().decode())
    b4 = re.compile("([A-Z]{3})_([A-Z]{3})")
    for key in b3:
        b5 = b4.match(key)
        b6 = -math.log(float(b3[key]))
        b7 = b5.group(1)
        b8 = b5.group(2)
        if b7 != b8:
            if b7 not in b1:
                b1[b7] = {}
            b1[b7][b8] = float(b6)
    return b1
def fonk2(b1, source):
    b9 = {}
    b10 = {}
    for node in b1:
        b9[node] = float('Inf')
        b10[node] = None
    b9[source] = 0
    return b9, b10
def fonk3(node, neighbour, b1, b9, b10):
    if b9[neighbour] > b9[node] + b1[node][neighbour]:
        b9[neighbour] = b9[node] + b1[node][neighbour]
        b10[neighbour] = node
def fonk4(b10, b15):
    b11 = [b15]
    b12 = b15
    while True:
        b12 = b10[b12]
        if b12 not in b11:
            b11.append(b12)
        else:
            b11.append(b12)
            b11 = b11[b11.index(b12):]
            return b11
def fonk5(b1, source):
    b9, b10 = fonk2(b1, source)
    for i in range(len(b1)-1):
        for u in b1:
            for v in b1[u]:
                fonk3(u, v, b1, b9, b10)
    for u in b1:
        for v in b1[u]:
            if b9[v] < b9[u] + b1[u][v]:
                return fonk4(b10, source)
    return None
b13 = []
b1 = fonk1()
for key in b1:
    b14 = fonk5(b1, key)
    if b14 and b14 not in b13:
        b13.append(b14)
for b14 in b13:
    if not b14:
        print("No opportunity here :(")
    else:
        a1 = 100
        print("Starting with {} in {}".format(a1, b14[0]))
        for i, value in enumerate(b14):
            if i + 1 < len(b14):
                b15 = b14[i]
                b16 = b14[i + 1]
                b17 = math.exp(-b1[b15][b16])
                a1 *= b17
                print("{} to {} at {} = {}".format(b15, b16, b17, a1))
    print("\n")