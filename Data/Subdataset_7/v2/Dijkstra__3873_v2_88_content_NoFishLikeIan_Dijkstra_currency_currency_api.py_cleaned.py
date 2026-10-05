import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
b1 = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fonk1(list_codes, b2 = 0, adjmatrix=False):
    print('Lazy-search for real-time rates')
    b3 = CurrencyRates()
    b4 = {}
    for currency in list_codes:
        print(f'Checking for {currency}')
        b4[currency] = {}
        b5 = [i for i in list_codes if i not in list(b4.keys())]
        for other_currency in b5:
            b6 = np.log(b3.get_rate(currency, other_currency))
            b4[currency][other_currency] = {'weights': b6}
        time.sleep(0.5)
    b7 = nx.from_dict_of_dicts(b4)
    return b7
if b8 = = '__main__':
    import matplotlib.pyplot as plt
    import pdb
    b7 = fonk1(b1)
    plt.plot()
    nx.draw_networkx(b7, b9 = nx.spring_layout(b7))
    plt.savefig('currency_graph.png')
    plt.close()
    pdb.set_trace()