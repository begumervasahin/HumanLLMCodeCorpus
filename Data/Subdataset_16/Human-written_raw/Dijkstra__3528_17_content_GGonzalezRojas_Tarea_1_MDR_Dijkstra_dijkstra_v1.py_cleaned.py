from collections import defaultdict
from heapq import heappop, heappush
def fonk1(b7, inicio, final):
    b1 = defaultdict(list)
    for nodo, nodo_sgte, peso in b7:
        b1[nodo].append((peso,nodo_sgte))
    b2 = [(0,inicio,())]
    b3 = set()
    while b2:
        (costo, b5, b4) = heappop(b2)
        if b5 not in b3:
            b3.add(b5)
            b4 = (b5, b4)
            if b5 = = final: return (costo,b4)
            for peso, parado_sgte in b1.get(b5,()):
                if parado_sgte not in b3:
                    heappush(b2,(costo + peso, parado_sgte, b4))
    return float("infinito")
if b6 = = "__main__":
    b7 = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11),
        ("G", "H", 5)
    ]
print(fonk1(b7,"A","H"))