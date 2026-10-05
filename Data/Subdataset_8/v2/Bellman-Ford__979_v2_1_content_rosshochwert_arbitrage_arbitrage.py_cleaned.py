import math
import urllib.request
import json
import re
def download_exchange_rates():
    exchange_rates = {}
    url = "http:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    pattern = re.compile("([A-Z]{3})_([A-Z]{3})")
    for currency_pair, rate in data.items():
        matches = pattern.match(currency_pair)
        if matches:
            from_currency = matches.group(1)
            to_currency = matches.group(2)
            if from_currency != to_currency:
                if from_currency not in exchange_rates:
                    exchange_rates[from_currency] = {}
                exchange_rates[from_currency][to_currency] = -math.log(float(rate))
    return exchange_rates
def initialize_distances_and_paths(graph, source):
    distances = {}
    previous = {}
    for node in graph:
        distances[node] = float('inf')
        previous[node] = None
    distances[source] = 0
    return distances, previous
def relax_edge(node, neighbor, graph, distances, previous):
    if distances[neighbor] > distances[node] + graph[node][neighbor]:
        distances[neighbor] = distances[node] + graph[node][neighbor]
        previous[neighbor] = node
def retrace_negative_loop(previous, start):
    arbitrage_loop = [start]
    next_node = start
    while True:
        next_node = previous[next_node]
        if next_node not in arbitrage_loop:
            arbitrage_loop.append(next_node)
        else:
            arbitrage_loop.append(next_node)
            arbitrage_loop = arbitrage_loop[arbitrage_loop.index(next_node):]
            return arbitrage_loop
def bellman_ford(graph, source):
    distances, previous = initialize_distances_and_paths(graph, source)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                relax_edge(node, neighbor, graph, distances, previous)
    for node in graph:
        for neighbor in graph[node]:
            if distances[neighbor] < distances[node] + graph[node][neighbor]:
                return retrace_negative_loop(previous, source)
    return None
def find_arbitrage_opportunities():
    paths = []
    exchange_rates = download_exchange_rates()
    for currency in exchange_rates:
        path = bellman_ford(exchange_rates, currency)
        if path and path not in paths:
            paths.append(path)
    for path in paths:
        if not path:
            print("No arbitrage opportunity found.")
        else:
            initial_money = 100
            print("Starting with {} in {}".format(initial_money, path[0]))
            for i, currency in enumerate(path):
                if i + 1 < len(path):
                    start_currency = path[i]
                    end_currency = path[i + 1]
                    exchange_rate = math.exp(-exchange_rates[start_currency][end_currency])
                    initial_money *= exchange_rate
                    print("{} to {} at {} = {}".format(start_currency, end_currency, exchange_rate, initial_money))
        print("\n")
if __name__ == "__main__":
    find_arbitrage_opportunities()