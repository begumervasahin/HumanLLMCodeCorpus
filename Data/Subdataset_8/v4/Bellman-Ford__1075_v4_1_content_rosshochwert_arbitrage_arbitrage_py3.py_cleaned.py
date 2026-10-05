import json
import math
import re
from urllib.request import urlopen
def download_exchange_rates():
    exchange_rates = {}
    url = "http:
    with urlopen(url) as response:
        data = json.loads(response.read())
    pattern = re.compile("([A-Z]{3})_([A-Z]{3})")
    for key, value in data.items():
        matches = pattern.match(key)
        if matches:
            from_rate = matches.group(1)
            to_rate = matches.group(2)
            if from_rate != to_rate:
                if from_rate not in exchange_rates:
                    exchange_rates[from_rate] = {}
                exchange_rates[from_rate][to_rate] = -math.log(float(value))
    return exchange_rates
def initialize_distances_and_predecessors(graph, source):
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0
    return distances, predecessors
def relax_edge(node, neighbor, graph, distances, predecessors):
    if distances[neighbor] > distances[node] + graph[node][neighbor]:
        distances[neighbor] = distances[node] + graph[node][neighbor]
        predecessors[neighbor] = node
def retrace_negative_loop(predecessors, start):
    arbitrage_loop = [start]
    next_node = start
    while True:
        next_node = predecessors[next_node]
        if next_node not in arbitrage_loop:
            arbitrage_loop.append(next_node)
        else:
            arbitrage_loop.append(next_node)
            arbitrage_loop = arbitrage_loop[arbitrage_loop.index(next_node):]
            return arbitrage_loop
def bellman_ford(graph, source):
    distances, predecessors = initialize_distances_and_predecessors(graph, source)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                relax_edge(node, neighbor, graph, distances, predecessors)
    for node in graph:
        for neighbor in graph[node]:
            if distances[neighbor] < distances[node] + graph[node][neighbor]:
                return retrace_negative_loop(predecessors, source)
    return None
def find_arbitrage_opportunities():
    paths = []
    exchange_rates = download_exchange_rates()
    for currency_pair in exchange_rates:
        path = bellman_ford(exchange_rates, currency_pair)
        if path and path not in paths:
            paths.append(path)
    for path in paths:
        if not path:
            print("No arbitrage opportunity found.")
        else:
            initial_money = 100
            print(f"Starting with {initial_money} in {path[0]}")
            for i, _ in enumerate(path):
                if i + 1 < len(path):
                    start = path[i]
                    end = path[i + 1]
                    rate = math.exp(-exchange_rates[start][end])
                    initial_money *= rate
                    print(f"{start} to {end} at {rate} = {initial_money}")
if __name__ == "__main__":
    find_arbitrage_opportunities()