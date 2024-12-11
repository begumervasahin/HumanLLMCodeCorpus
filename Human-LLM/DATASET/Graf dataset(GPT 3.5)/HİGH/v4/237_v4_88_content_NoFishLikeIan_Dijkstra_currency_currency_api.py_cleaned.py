import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
b1 = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fonk1(list_codes, b2 = 0.5, adjmatrix=False):
    print('Lazy-search for real-time rates')
    b3 = CurrencyRates()
    b4 = {}
    for currency in list_codes:
        print(f'Checking for {currency}')
        b4[currency] = {}
        for other_currency in list_codes:
            if currency != other_currency:
                b5 = np.log(b3.get_rate(currency, other_currency))
                b4[currency][other_currency] = {'weight': b5}
                time.sleep(b2)
    b6 = nx.from_dict_of_dicts(b4)
    return b6
if b7 = = '__main__':
    import matplotlib.pyplot as plt
    b6 = fonk1(b1)
    plt.plot()
    nx.draw_networkx(b6, b8 = nx.spring_layout(b6))
    plt.savefig('currency_graph.png')
    plt.close()