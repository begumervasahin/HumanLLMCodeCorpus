import currency,test
from test import num_threads
from currency import CurrencyThread
from math import log
from BellmanFord import BellmanFord
def fonk1(rates,b1 = currency.CURRENCIES):
    b2 = dict()
    for  i in b1:
        b2[i] = dict()
    for j in rates:
        u,b3 = j["id"][0:3],j["id"][3:]
        print(u + " " +  b3 + " " +  j["Rate"])
        b4 = log(round(float(j["Rate"]) ** -1,4))
        b2[u][b3] = b4
    return b2
if b5 = = "__main__":
    b6 = num_threads()
    b7 = currency.make_threads(b6)
    CurrencyThread.run_all_threads(b7)
    b8 = []
    b9 = currency.CURRENCIES
    for  i in  b7:
        for j in i.data:
            b8.append(j)
    b2 = fonk1(b8)
    for u in  b2:
        print(b2[u])
    b10 = BellmanFord(b9,fonk1(b8),currency.CURRENCIES[0])