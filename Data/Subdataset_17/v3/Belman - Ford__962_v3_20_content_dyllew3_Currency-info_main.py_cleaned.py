from currency import CurrencyThread, make_threads, CURRENCIES
from test import num_threads
from math import log
from BellmanFord import BellmanFord
def set_edges(rates, currencies=CURRENCIES):
    edges = {currency: {} for currency in currencies}
    for rate in rates:
        u, v = rate["id"][:3], rate["id"][3:]
        print(f"{u} {v} {rate['Rate']}")
        weight = log(round(float(rate["Rate"]) ** -1, 4))
        edges[u][v] = weight
    return edges
def collect_currency_rates(threads):
    currency_rates = []
    for thread in threads:
        currency_rates.extend(thread.data)
    return currency_rates
def main():
    threads_len = num_threads()
    threads = make_threads(threads_len)
    CurrencyThread.run_all_threads(threads)
    currency_rates = collect_currency_rates(threads)
    vertices = CURRENCIES
    edges = set_edges(currency_rates)
    for u in edges:
        print(edges[u])
    bellman_ford = BellmanFord(vertices, edges, vertices[0])
if __name__ == "__main__":
    main()