import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
b1 = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fonk1(b1, b2 = 0, adjmatrix=False):
    print('Fetching real-time rates...')
    b3 = CurrencyRates()
    b4 = {}
    for currency in b1:
        print(f'Fetching rates for {currency}...')
        b4[currency] = {}
        b5 = [code for code in b1 if code != currency]
        for other_currency in b5:
            try:
                b6 = b3.get_rate(currency, other_currency)
                b7 = np.log(b6)
                b4[currency][other_currency] = {'weights': b7}
            except Exception as e:
                print(f"Error fetching b6 for {currency} to {other_currency}: {e}")
                b4[currency][other_currency] = {'weights': None}
        time.sleep(b2)
    b8 = nx.from_dict_of_dicts(b4)
    if adjmatrix:
        return nx.to_numpy_matrix(b8)
    return b8
if b9 = = '__main__':
    b8 = fonk1(b1, b2=0.5)
    plt.figure(b10 = (10, 8))
    b11 = nx.spring_layout(b8)
    nx.draw_networkx(b8, b11, b12 = True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('currency_graph.png')
    plt.show()