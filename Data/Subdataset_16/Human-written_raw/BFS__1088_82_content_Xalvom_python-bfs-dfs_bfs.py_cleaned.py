82. Repository: Xalvom/python-bfs-dfs
   File: bfs.py
   URL: https:
   Code Content:
b1 = {'A':set(['B']),
         'B':set(['A','C']),
         'C':set(['B','D','H','I']),
         'D':set(['C','E','F','H','M']),
         'E':set(['D']),
         'F':set(['D','G','M']),
         'G':set(['F','H']),
         'H':set(['C','D','G','L']),
         'I':set(['C','J','K']),
         'J':set(['I']),
         'K':set(['I','L']),
         'L':set(['H','K']),
	 'M':set(['D','F'])}
print()
print("*********BFS***********")
b2 = input("Input Awal: ")
b3 = input("Input Tujuan: ")
print("***********************")
print()
def fonk1(graf, mulai, tujuan):
    b4 = [[mulai]]
    b5 = set()
    while b4:
        b6 = b4.pop(0)
        b7 = b6[-1]
        if b7 = = tujuan:
            return b6
        elif b7 not in b5:
            for cabang in graf.get(b7, []):
                b8 = list(b6)
                b8.append(cabang)
                b4.append(b8)
            b5.add(b7)
        b9 = len(b4)
        if b9 = = 0:
            print("Tidak ditemukan")
print(fonk1(b1,b2,b3))
print()
print("Link Github: https:
   README Content:
BFS and DFS with pyhton
