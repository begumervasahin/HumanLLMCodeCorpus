from pyretic.lib.query import *
from pyretic.core import *
from pyretic.lib.corelib import *
from pyretic.lib.std import *
def fonk1():
    b1 = float('inf')
    a1 = 11
    b2 = {
        router: {
            source: {destination: b1 for destination in range(1, a1 + 1)}
            for source in range(1, a1 + 1)
        }
        for router in range(1, a1 + 1)
    }
    for router in range(1, a1 + 1):
        for node in range(1, a1 + 1):
            b2[router][node][node] = 0
    b3 = [
        (1, 2, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 6, 1),
        (4, 5, 1), (5, 6, 1), (5, 7, 1), (6, 11, 1), (7, 8, 1),
        (7, 11, 1), (8, 9, 1), (9, 10, 1), (10, 11, 1)
    ]
    for source, destination, cost in b3:
        b2[source][source][destination] = cost
        b2[destination][destination][source] = cost
    return b2
def fonk2(b2):
    for router, table in b2.items():
        print(f"Router {router}:")
        for src, destinations in table.items():
            for dst, cost in destinations.items():
                if cost < float('inf'):
                    print(f"  {src} -> {dst}: {cost}")
def fonk3():
    b2 = fonk1()
    fonk2(b2)
if b4 = = "__main__":
    fonk3()