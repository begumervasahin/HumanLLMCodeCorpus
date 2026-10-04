from collections import defaultdict
from heapq import *
def fonk1(b6, f, t):
    b1 = defaultdict(list)
    for l,r,c in b6:
        b1[l].append((c,r))
    q, b2 = [(0,f,())], set()
    while q:
        (cost,b4,b3) = heappop(q)
        if b4 not in b2:
            b2.add(b4)
            b3 = (b4, b3)
            if b4 = = t: return (cost, b3)
            for c, v2 in b1.get(b4, ()):
                if v2 not in b2:
                    heappush(q, (cost+c, v2, b3))
    return float("inf")
if b5 = = "__main__":
    b6 = [
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
    print ("=== b7 = ==")
    print ("A -> H:")
    print (fonk1(b6, "A", "H"))
    print (fonk1(b6,"A","D"))
    print (fonk1(b6,"D","F"))
    print (fonk1(b6,"F","G"))
    print (fonk1(b6,"G","H"))
    print ("F -> G:")
    print (fonk1(b6, "F", "G"))