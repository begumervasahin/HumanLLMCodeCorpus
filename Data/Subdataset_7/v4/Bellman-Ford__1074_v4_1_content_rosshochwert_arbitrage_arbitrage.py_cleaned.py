import math
import urllib.request
import json
import re
def fonk1():
    b1 = {}
    b2 = "http:
    with urllib.request.urlopen(b2) as response:
        b3 = json.loads(response.read().decode())
    b4 = re.compile("([A-Z]{3})_([A-Z]{3})")
    for key, value in b3.items():
        b5 = b4.match(key)
        if b5:
            b6 = b5.group(1)
            b7 = b5.group(2)
            if b6 != b7:
                if b6 not in b1:
                    b1[b6] = {}
                b1[b6][b7] = -math.log(float(value))
    return b1
def fonk2(b1, source):
    b8 = {}
    b9 = {}
    for node in b1:
        b8[node] = float('inf')
        b9[node] = None
    b8[source] = 0
    return b8, b9
def fonk3(node, neighbour, b1, b8, b9):
    if b8[neighbour] > b8[node] + b1[node][neighbour]:
        b8[neighbour] = b8[node] + b1[node][neighbour]
        b9[neighbour] = node
def fonk4(b9, b14):
    b10 = [b14]
    b11 = b14
    while True:
        b11 = b9[b11]
        if b11 not in b10:
            b10.append(b11)
        else:
            b10.append(b11)
            b10 = b10[b10.index(b11):]
            return b10
def fonk5(b1, source):
    b8, b9 = fonk2(b1, source)
    for _ in range(len(b1) - 1):
        for node in b1:
            for neighbour in b1[node]:
                fonk3(node, neighbour, b1, b8, b9)
    for node in b1:
        for neighbour in b1[node]:
            if b8[neighbour] < b8[node] + b1[node][neighbour]:
                return fonk4(b9, source)
    return None
b12 = []
b1 = fonk1()
for key in b1:
    b13 = fonk5(b1, key)
    if b13 and b13 not in b12:
        b12.append(b13)
for b13 in b12:
    if not b13:
        print("No arbitrage opportunity found.")
    else:
        a1 = 100
        print("Starting with {} in {}".format(a1, b13[0]))
        for i, value in enumerate(b13):
            if i + 1 < len(b13):
                b14 = b13[i]
                b15 = b13[i + 1]
                b16 = math.exp(-b1[b14][b15])
                a1 *= b16
                print("{} to {} at {} = {}".format(b14, b15, b16, a1))
    print("\n")