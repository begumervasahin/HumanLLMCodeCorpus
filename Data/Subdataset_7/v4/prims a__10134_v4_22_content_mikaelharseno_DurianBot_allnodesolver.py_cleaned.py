import networkx as nx
import random
from heapq import heappop, heappush
from itertools import count
def fonk1(client):
    client.end()
    client.start()
    b1 = client.G
    b2 = nx.minimum_spanning_tree(b1)
    fonk2(b2, client)
    print("Number of bots needed to be rescued:")
    print(client.l)
    print("Number of final rescued bots:")
    print(client.bot_count[client.home])
    client.end()
def fonk2(b2, client):
    b3 = list(b2.degree)
    while (len(b3) > 1):
        a1 = 0
        b4 = len(b3)
        while a1 < b4:
            if b3[a1][1] == 1 and b3[a1][0] != client.h:
                break
            a1 += 1
        b5 = b3[a1][0]
        b6 = list(b2[b5].keys())[0]
        client.remote(b5, b6)
        b2.remove_node(b5)
        b3 = list(b2.degree)
