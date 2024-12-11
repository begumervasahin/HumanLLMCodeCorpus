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
    for currency_pair, rate in b3.items():
        b5 = b4.match(currency_pair)
        if b5:
            b6 = b5.group(1)
            b7 = b5.group(2)
            if b6 != b7:
                if b6 not in b1:
                    b1[b6] = {}
                b1[b6][b7] = -math.log(float(rate))
    return b1
def fonk2(graph, source):
    b8 = {node: float('inf') for node in graph}
    b9 = {node: None for node in graph}
    b8[source] = 0
    return b8, b9
def fonk3(node, neighbor, graph, b8, b9):
    if b8[neighbor] > b8[node] + graph[node][neighbor]:
        b8[neighbor] = b8[node] + graph[node][neighbor]
        b9[neighbor] = node
def fonk4(b9, start):
    b10 = [start]
    b11 = start
    while True:
        b11 = b9[b11]
        if b11 not in b10:
            b10.append(b11)
        else:
            b10.append(b11)
            b10 = b10[b10.index(b11):]
            return b10
def fonk5(graph, source):
    b8, b9 = fonk2(graph, source)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                fonk3(node, neighbor, graph, b8, b9)
    for node in graph:
        for neighbor in graph[node]:
            if b8[neighbor] < b8[node] + graph[node][neighbor]:
                return fonk4(b9, source)
    return None
def fonk6():
    b12 = []
    b1 = fonk1()
    for currency in b1:
        b13 = fonk5(b1, currency)
        if b13 and b13 not in b12:
            b12.append(b13)
    for b13 in b12:
        if not b13:
            print("No arbitrage opportunity found.")
        else:
            a1 = 100
            print("Starting with {} in {}".format(a1, b13[0]))
            for i, currency in enumerate(b13):
                if i + 1 < len(b13):
                    b14 = b13[i]
                    b15 = b13[i + 1]
                    b16 = math.exp(-b1[b14][b15])
                    a1 *= b16
                    print("{} to {} at {} = {}".format(b14, b15, b16, a1))
        print("\n")
if b17 = = "__main__":
    fonk6()