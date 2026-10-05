b1 = {'A':set(['B']),
        'B':set(['C','A']),
        'C':set(['H','B','I','D']),
        'D':set(['C','E','H','F']),
        'E':set(['D']),
        'F':set(['D','G']),
        'G':set(['F','H']),
        'H':set(['L','C','G','D']),
        'I':set(['C','J','K']),
        'J':set(['I']),
        'K':set(['L','I']),
        'L':set(['K','H'])}
def fonk1(graph, b4, goal):
    b2 = []
    b3 = [[b4]]
    if b4 = = goal:
        return "Awal adalah Tujuan"
    while b3:
        b5 = b3.pop(0)
        b6 = b5[-1]
        if b6 not in b2:
            b7 = graph[b6]
            for b9 in b7:
                b8 = list(b5)
                b8.append(b9)
                b3.append(b8)
                if b9 = = goal:
                    return b8
            b2.append(b6)
    return "Mohon maaf b6 yang kalian pilih tidak ada"
b10 = input("Masukan b10: ")
b11 = input("Masukan Akhir: ")
print(fonk1(b1, b10, b11))