def fonk1(graf, mulai, tujuan):
    b1 = [[mulai]]
    b2 = set()
    while b1:
        b3 = b1.pop(0)
        b4 = b3[-1]
        if b4 = = tujuan:
            return b3
        elif b4 not in b2:
            for cabang in graf.get(b4, []):
                b5 = list(b3)
                b5.append(cabang)
                b1.append(b5)
            b2.add(b4)
        if len(b1) == 0:
            print("Tidak ditemukan")
b6 = {
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
print("*********BFS***********")
b7 = input("Input Awal: ")
b8 = input("Input Tujuan: ")
print("***********************")
print()
b9 = fonk1(b6, b7, b8)
if b9:
    print("Jalur BFS:", b9)
else:
    print("Tidak ditemukan")
print()
print("Link Github: https: