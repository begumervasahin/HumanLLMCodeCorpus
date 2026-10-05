import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
CURRENCY_CODES = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def currency_nxgraph(list_codes, sleeping=0.5, adjmatrix=False):
    print('Lazy-search for real-time rates')
    currency_rates = CurrencyRates()
    exchange_rates = {}
    for currency in list_codes:
        print(f'Checking for {currency}')
        exchange_rates[currency] = {}
        for other_currency in list_codes:
            if currency != other_currency:
                rate = np.log(currency_rates.get_rate(currency, other_currency))
                exchange_rates[currency][other_currency] = {'weight': rate}
                time.sleep(sleeping)
    G = nx.from_dict_of_dicts(exchange_rates)
    return G
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    graph = currency_nxgraph(CURRENCY_CODES)
    plt.plot()
    nx.draw_networkx(graph, pos=nx.spring_layout(graph))
    plt.savefig('currency_graph.png')
    plt.close()