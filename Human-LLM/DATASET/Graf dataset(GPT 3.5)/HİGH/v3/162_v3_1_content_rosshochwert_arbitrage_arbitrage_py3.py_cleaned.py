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
    for key, value in b3.items():
        b5 = b4.match(key)
        if b5:
            from_currency, b6 = b5.group(1), b5.group(2)
            if from_currency != b6:
                b1.setdefault(from_currency, {})
                b1[from_currency][b6] = -math.log(float(value))
    return b1
def fonk2(graph, source):
    b7 = {node: float('inf') for node in graph}
    b8 = {node: None for node in graph}
    b7[source] = 0
    return b7, b8
def fonk3(node, neighbor, graph, b7, b8):
    if b7[neighbor] > b7[node] + graph[node][neighbor]:
        b7[neighbor] = b7[node] + graph[node][neighbor]
        b8[neighbor] = node
def fonk4(b8, start):
    b9 = [start]
    b10 = start
    while True:
        b10 = b8[b10]
        if b10 not in b9:
            b9.append(b10)
        else:
            b9.append(b10)
            b9 = b9[b9.index(b10):]
            return b9
def fonk5(graph, source):
    b7, b8 = fonk2(graph, source)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                fonk3(node, neighbor, graph, b7, b8)
    for node in graph:
        for neighbor in graph[node]:
            if b7[neighbor] < b7[node] + graph[node][neighbor]:
                return fonk4(b8, source)
    return None
def fonk6():
    b11 = []
    b1 = fonk1()
    for currency_pair in b1:
        b12 = fonk5(b1, currency_pair)
        if b12 and b12 not in b11:
            b11.append(b12)
    for b12 in b11:
        if not b12:
            print("No arbitrage opportunity found.")
        else:
            a1 = 100
            print(f"Starting with {a1} in {b12[0]}")
            for i in range(len(b12) - 1):
                start, b13 = b12[i], b12[i + 1]
                b14 = math.exp(-b1[start][b13])
                a1 *= b14
                print(f"{start} to {b13} at {b14} = {a1}")
if b15 = = "__main__":
    fonk6()