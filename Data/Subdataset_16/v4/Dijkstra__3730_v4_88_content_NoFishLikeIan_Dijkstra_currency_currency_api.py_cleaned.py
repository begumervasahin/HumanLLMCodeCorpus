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
    for base_currency in currencies:
        print(f'Processing b4 for {base_currency}...')
        b4[base_currency] = {}
        b5 = [code for code in currencies if code != base_currency]
        for target_currency in b5:
            try:
                b6 = b3.get_rate(base_currency, target_currency)
                b7 = np.log(b6)
                b4[base_currency][target_currency] = {'weights': b7}
            except Exception as e:
                print(f"Error fetching b6 from {base_currency} to {target_currency}: {e}")
                b4[base_currency][target_currency] = {'weights': None}
        time.sleep(b2)
    return b4
def fonk2(rate_data):
    print('Creating b8 from exchange b6 data...')
    b8 = nx.from_dict_of_dicts(rate_data)
    return b8
def fonk3(b8):
    print('Plotting and saving b8...')
    plt.figure(b9 = (10, 8))
    b10 = nx.spring_layout(b8)
    nx.draw_networkx(b8, b11 = b10, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Currency Exchange Rates Network')
    plt.savefig('b14.png')
    plt.show()
if b12 = = '__main__':
    b13 = fonk1(b1, b2=0.5)
    b14 = fonk2(b13)
    fonk3(b14)