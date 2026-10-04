import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
currency_codes = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fetch_currency_rates(currencies, delay=0):
    print('Fetching real-time exchange rates...')
    c = CurrencyRates()
    rates = {}
    for currency in currencies:
        print(f'Processing rates for {currency}...')
        rates[currency] = {}
        for other_currency in currencies:
            if currency == other_currency:
                continue
            try:
                rate = c.get_rate(currency, other_currency)
                rates[currency][other_currency] = np.log(rate)
            except Exception as e:
                print(f"Error fetching rate for {currency} to {other_currency}: {e}")
                rates[currency][other_currency] = None
        time.sleep(delay)
    return rates
def create_currency_graph(rates):
    print('Creating graph from exchange rates...')
    G = nx.from_dict_of_dicts(rates)
    return G
def plot_graph(G):
    print('Plotting and saving graph...')
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('currency_graph.png')
    plt.show()
if __name__ == '__main__':
    currency_rates = fetch_currency_rates(currency_codes, delay=0.5)
    currency_graph = create_currency_graph(currency_rates)
    plot_graph(currency_graph)