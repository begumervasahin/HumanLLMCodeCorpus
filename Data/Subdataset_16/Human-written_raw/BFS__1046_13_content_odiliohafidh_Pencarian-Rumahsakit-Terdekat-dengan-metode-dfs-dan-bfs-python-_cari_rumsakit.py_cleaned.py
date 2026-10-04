13. Repository: odiliohafidh/Pencarian-Rumahsakit-Terdekat-dengan-metode-dfs-dan-bfs-python-
   File: cari_rumsakit.py
   URL: https:
   Code Content:
b1 = {'A':set(['RS1','C','E']),
         'B':set(['E','D']),
         'C':set(['A','B','RS2']),
         'D':set(['B','F','K','RS3']),
         'E':set(['A','B']),
         'F':set(['D','G']),
         'G':set(['H','F','I']),
         'H':set(['G']),
         'I':set(['G','J']),
         'J':set(['I']),
         'K':set(['D','L','M']),
         'L':set(['RS2','K']),
         'M':set(['K']),
         'RS1':set(['A']),
         'RS2':set(['C','L']),
         'RS3':set(['D'])}
def fonk1(graf, mulai):
    b2 = [[mulai]]
    b3 = 'RS1'
    b4 = 'RS2'
    b5 = 'RS3'
    b6 = set()
    while b2:
        b7 = b2.pop(0)
        b8 = b7[-1]
        if b8 = = b3:
            return b7
        elif b8 = = b4:
            return b7
        elif b8 = = b5:
            return b7
        elif b8 not in b6:
            for cabang in graf.get(b8, []):
                b9 = list(b7)
                b9.append(cabang)
                b2.append(b9)
            b6.add(b8)
        b10 = len(b2)
        if b10 = = 0:
            print("Tidak ditemukan")
def fonk2(graf, mulai):
    b11 = [[mulai]]
    b3 = 'RS1'
    b4 = 'RS2'
    b5 = 'RS3'
    b6 = set()
    while b11:
        b7 = b11.pop(-1)
        b8 = b7[-1]
        if b8 = = b3:
            return b7
        elif b8 = = b4:
            return b7
        elif b8 = = b5:
            return b7
        elif b8 not in b6:
            for cabang in graf.get(b8, []):
                b9 = list(b7)
                b9.append(cabang)
                b11.append(b9)
            b6.add(b8)
        b10 = len(b11)
        if b10 = = 0:
            print("Tidak ditemukan")
   README Content:
Pencarian Rumah Sakit Terdekat dengan metode DFS dan BFS (Python)
===========================
pencarian rumah sakit terdekat dengan hanya menginputkan posisi awal
![graph](https:
di develop dan modifikasi oleh
 - Reo Cavallera A11.2014.08577
 - Odilio Arys H A A11.2014.08385
 - Proyek  AI A11.4606 2017
