import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
currency_codes = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def currency_nxgraph(currency_codes, sleeping=0, adjmatrix=False):
    print('Fetching real-time rates...')
    c = CurrencyRates()
    graph_data = {}
    for currency in currency_codes:
        print(f'Fetching rates for {currency}...')
        graph_data[currency] = {}
        remaining_codes = [code for code in currency_codes if code != currency]
        for other_currency in remaining_codes:
            try:
                rate = c.get_rate(currency, other_currency)
                log_rate = np.log(rate)
                graph_data[currency][other_currency] = {'weights': log_rate}
            except Exception as e:
                print(f"Error fetching rate for {currency} to {other_currency}: {e}")
                graph_data[currency][other_currency] = {'weights': None}
        time.sleep(sleeping)
    G = nx.from_dict_of_dicts(graph_data)
    if adjmatrix:
        return nx.to_numpy_matrix(G)
    return G
if __name__ == '__main__':
    G = currency_nxgraph(currency_codes, sleeping=0.5)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('currency_graph.png')
    plt.show()