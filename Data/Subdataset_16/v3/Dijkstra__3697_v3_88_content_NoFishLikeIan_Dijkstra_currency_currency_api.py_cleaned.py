import time
import numpy as np
import networkx as nx
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
b1 = ['EUR', 'USD', 'GBP', 'JPY', 'CNY', 'INR', 'AUD']
def fonk1(currencies, b2 = 0):
    print('Fetching real-time exchange b4...')
    b3 = CurrencyRates()
    b4 = {}
    for b5 in currencies:
        print(f'Processing b4 for {b5}...')
        b4[b5] = {}
        for target_currency in currencies:
            if b5 = = target_currency:
                continue
            try:
                b6 = b3.get_rate(b5, target_currency)
                b4[b5][target_currency] = np.log(b6)
            except Exception as e:
                print(f"Error fetching b6 from {b5} to {target_currency}: {e}")
                b4[b5][target_currency] = None
        time.sleep(b2)
    return b4
def fonk2(b12):
    print('Creating b7 from exchange b6 data...')
    b7 = nx.from_dict_of_dicts(b12)
    return b7
def fonk3(b7):
    print('Plotting and saving b7...')
    plt.figure(b8 = (10, 8))
    b9 = nx.spring_layout(b7)
    nx.draw_networkx(b7, b10 = b9, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('b13.png')
    plt.show()
if b11 = = '__main__':
    b12 = fonk1(b1, b2=0.5)
    b13 = fonk2(b12)
    fonk3(b13)