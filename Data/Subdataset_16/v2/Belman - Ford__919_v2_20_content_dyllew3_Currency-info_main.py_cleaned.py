from currency import CurrencyThread, make_threads, CURRENCIES
from test import num_threads
from math import log
from BellmanFord import BellmanFord
def fonk1(rates, b1 = CURRENCIES):
    b2 = {currency: {} for currency in b1}
    for rate in rates:
        u, b3 = rate["id"][:3], rate["id"][3:]
        print(f"{u} {b3} {rate['Rate']}")
        b4 = log(round(float(rate["Rate"]) ** -1, 4))
        b2[u][b3] = b4
    return b2
def fonk2():
    b5 = num_threads()
    b6 = make_threads(b5)
    CurrencyThread.run_all_threads(b6)
    b7 = []
    for thread in b6:
        b7.extend(thread.data)
    b8 = CURRENCIES
    b2 = fonk1(b7)
    for u in b2:
        print(b2[u])
    b9 = BellmanFord(b8, b2, b8[0])
if b10 = = "__main__":
    fonk2()