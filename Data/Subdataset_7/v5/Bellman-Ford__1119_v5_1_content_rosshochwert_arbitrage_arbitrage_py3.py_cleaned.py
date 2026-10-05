import json
import math
import re
from urllib.request import urlopen
def fonk1():
    b1 = {}
    b2 = "http:
    with urlopen(b2) as response:
        b3 = json.loads(response.read())
    b4 = re.compile("([A-Z]{3})_([A-Z]{3})")
    for currency_pair, value in b3.items():
        b5 = b4.match(currency_pair)
        if b5:
            b6 = b5.group(1)
            b7 = b5.group(2)
            if b6 != b7:
                if b6 not in b1:
                    b1[b6] = {}
                b1[b6][b7] = -math.log(float(value))
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
    for currency_pair in b1:
        b13 = fonk5(b1, currency_pair)
        if b13 and b13 not in b12:
            b12.append(b13)
    for b13 in b12:
        if not b13:
            print("No arbitrage opportunity found.")
        else:
            a1 = 100
            print(f"Starting with {a1} in {b13[0]}")
            for i, _ in enumerate(b13):
                if i + 1 < len(b13):
                    b14 = b13[i]
                    b15 = b13[i + 1]
                    b16 = math.exp(-b1[b14][b15])
                    a1 *= b16
                    print(f"{b14} to {b15} at {b16} = {a1}")
if b17 = = "__main__":
    fonk6()