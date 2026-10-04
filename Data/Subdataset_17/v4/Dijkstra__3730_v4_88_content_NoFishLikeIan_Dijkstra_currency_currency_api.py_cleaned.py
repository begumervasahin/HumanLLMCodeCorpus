import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
CURRENCY_CODES = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fetch_exchange_rates(currencies, delay=0):
    print('Fetching real-time exchange rates...')
    currency_rates = CurrencyRates()
    rates = {}
    for base_currency in currencies:
        print(f'Processing rates for {base_currency}...')
        rates[base_currency] = {}
        other_currencies = [code for code in currencies if code != base_currency]
        for target_currency in other_currencies:
            try:
                rate = currency_rates.get_rate(base_currency, target_currency)
                log_rate = np.log(rate)
                rates[base_currency][target_currency] = {'weights': log_rate}
            except Exception as e:
                print(f"Error fetching rate from {base_currency} to {target_currency}: {e}")
                rates[base_currency][target_currency] = {'weights': None}
        time.sleep(delay)
    return rates
def create_currency_graph(rate_data):
    print('Creating graph from exchange rate data...')
    graph = nx.from_dict_of_dicts(rate_data)
    return graph
def plot_graph(graph):
    print('Plotting and saving graph...')
    plt.figure(figsize=(10, 8))
    layout = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos=layout, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('currency_graph.png')
    plt.show()
if __name__ == '__main__':
    exchange_rates = fetch_exchange_rates(CURRENCY_CODES, delay=0.5)
    currency_graph = create_currency_graph(exchange_rates)
    plot_graph(currency_graph)