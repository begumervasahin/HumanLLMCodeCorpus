def fonk1():
    b1 = float('inf')
    a1 = 11
    b2 = {i: {j: {k: b1 for k in range(1, a1 + 1)} for j in range(1, a1 + 1)} for i in range(1, a1 + 1)}
    for i in range(1, a1 + 1):
        b2[i][i][i] = 0
    b3 = [
        (1, 2, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 6, 1),
        (4, 5, 1), (5, 6, 1), (5, 7, 1), (6, 11, 1), (7, 8, 1),
        (7, 11, 1), (8, 9, 1), (9, 10, 1), (10, 11, 1)
    ]
    for u, v, w in b3:
        b2[u][u][v] = w
        b2[v][v][u] = w
    return b2
def fonk2():
    b2 = fonk1()
    for rt in b2:
        print(f"Router {rt}:")
        for src in b2[rt]:
            for dst in b2[rt][src]:
                if b2[rt][src][dst] < float('inf'):
                    print(f"  {src} -> {dst}: {b2[rt][src][dst]}")
if b4 = = "__main__":
    fonk2()