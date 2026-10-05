3. Repository: rizkyary/BFS_BASE
   File: BFS_BASE.py
   URL: https:
   Code Content:
base =  {'A':set(['B','C']),
         'B':set(['A','H','J',]),
         'C':set(['A','D','G']),
         'D':set(['C','E']),
         'E':set(['D','F']),
         'F':set(['E','G','K','L']),
         'G':set(['C','F']),
         'H':set(['B','I']),
         'I':set(['H','J','K']),
         'J':set(['B','I']),
         'K':set(['F','I','L']),
         'L':set(['F','K'])}
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
   README Content:
Mencari BFS dan DFS menggunakan software Python
BFS dan DFS
