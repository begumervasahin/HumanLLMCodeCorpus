82. Repository: Xalvom/python-bfs-dfs
   File: bfs.py
   URL: https:
   Code Content:
peta1 =  {'A':set(['B']),
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
awal = input("Input Awal: ")
akhir = input("Input Tujuan: ")
print("***********************")
print()
def bfs(graf, mulai, tujuan):
    queue = [[mulai]]
    visited = set()
    while queue:
        jalur = queue.pop(0)
        state = jalur[-1]
        if state == tujuan:
            return jalur
        elif state not in visited:
            for cabang in graf.get(state, []):
                jalur_baru = list(jalur)
                jalur_baru.append(cabang)
                queue.append(jalur_baru)
            visited.add(state)
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")
print(bfs(peta1,awal,akhir))
print()
print("Link Github: https:
   README Content:
BFS and DFS with pyhton
