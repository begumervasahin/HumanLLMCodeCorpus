
b1 = {
    'A': set(['B']),
    'B': set(['A', 'C']),
    'C': set(['B', 'D', 'H', 'I']),
    'D': set(['C', 'E', 'F', 'H', 'M']),
    'E': set(['D']),
    'F': set(['D', 'G', 'M']),
    'G': set(['F', 'H']),
    'H': set(['C', 'D', 'G', 'L']),
    'I': set(['C', 'J', 'K']),
    'J': set(['I']),
    'K': set(['I', 'L']),
    'L': set(['H', 'K']),
    'M': set(['D', 'F'])
}
def fonk1(graf, mulai, tujuan):
    b2 = [[mulai]]
    b3 = set()
    while b2:
        b4 = b2.pop(0)
        b5 = b4[-1]
        if b5 = = tujuan:
            return b4
        elif b5 not in b3:
            for cabang in graf.get(b5, []):
                b6 = list(b4)
                b6.append(cabang)
                b2.append(b6)
            b3.add(b5)
    return "Tidak ditemukan"
if b7 = = "__main__":
    print("*********BFS***********")
    b8 = input("Input Awal: ")
    b9 = input("Input Tujuan: ")
    print("***********************")
    print()
    b10 = fonk1(b1, b8, b9)
    print(b10)