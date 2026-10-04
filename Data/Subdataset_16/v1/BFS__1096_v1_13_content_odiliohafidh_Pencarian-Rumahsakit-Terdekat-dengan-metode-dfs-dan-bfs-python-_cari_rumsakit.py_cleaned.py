
b1 = {
    'A': set(['RS1', 'C', 'E']),
    'B': set(['E', 'D']),
    'C': set(['A', 'B', 'RS2']),
    'D': set(['B', 'F', 'K', 'RS3']),
    'E': set(['A', 'B']),
    'F': set(['D', 'G']),
    'G': set(['H', 'F', 'I']),
    'H': set(['G']),
    'I': set(['G', 'J']),
    'J': set(['I']),
    'K': set(['D', 'L', 'M']),
    'L': set(['RS2', 'K']),
    'M': set(['K']),
    'RS1': set(['A']),
    'RS2': set(['C', 'L']),
    'RS3': set(['D'])
}
def fonk1(graf, b12):
    b2 = [[b12]]
    b3 = 'RS1'
    b4 = 'RS2'
    b5 = 'RS3'
    b6 = set()
    while b2:
        b7 = b2.pop(0)
        b8 = b7[-1]
        if b8 = = b3 or b8 == b4 or b8 == b5:
            return b7
        elif b8 not in b6:
            for cabang in graf.get(b8, []):
                b9 = list(b7)
                b9.append(cabang)
                b2.append(b9)
            b6.add(b8)
    print("Tidak ditemukan")
    return None
def fonk2(graf, b12):
    b10 = [[b12]]
    b3 = 'RS1'
    b4 = 'RS2'
    b5 = 'RS3'
    b6 = set()
    while b10:
        b7 = b10.pop()
        b8 = b7[-1]
        if b8 = = b3 or b8 == b4 or b8 == b5:
            return b7
        elif b8 not in b6:
            for cabang in graf.get(b8, []):
                b9 = list(b7)
                b9.append(cabang)
                b10.append(b9)
            b6.add(b8)
    print("Tidak ditemukan")
    return None
if b11 = = "__main__":
    b12 = input("Masukkan posisi awal: ").strip()
    print("BFS mencari rumah sakit terdekat dari:", b12)
    b13 = fonk1(b1, b12)
    if b13:
        print("Jalur BFS:", " -> ".join(b13))
    print("\nDFS mencari rumah sakit terdekat dari:", b12)
    b14 = fonk2(b1, b12)
    if b14:
        print("Jalur DFS:", " -> ".join(b14))