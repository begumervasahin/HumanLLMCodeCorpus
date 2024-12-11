51. Repository: rrraharja/Kecerdasan-Buatan-AI
   File: Project DFS.py
   URL: https:
   Code Content:
b1 = {'ALASKA':set(['CALIFORNIA']),
         'CALIFORNIA':set(['CAROLINA','ALASKA']),
         'CAROLINA':set(['CALIFORNIA','INDIANA','HAWAII','DAREWALE']),
         'DAREWALE':set(['CAROLINA','EDINBURH','HAWAII','FLORIDA']),
         'EDINBURGH':set(['DAREWALE']),
         'FLORIDA':set(['DAREWALE','GEORGIA']),
         'GEORGIA':set(['FLORIDA','HAWAII']),
         'HAWAII':set(['DARAWALE','CAROLINA','GEORGIA','LOUSIANA']),
         'INDIANA':set(['CAROLINA','IDAKO','KENTUCKY']),
         'IDAKO':set(['INDIANA']),
         'KENTUCKY':set(['LOUSIANA','INDIANA']),
         'LOUSIANA':set(['KENTUCKY','HAWAII'])}
def fonk1(graf, start, finish):
    b2 = [[start]]
    b3 = set()
    while b2:
        b4 = len(b2)-1
        b5 = b2.pop(b4)
        b6 = b5[-1]
        if b6 = = finish:
            return b5
        elif b6 not in b3:
            for branch in graf.get(b6, []):
                b7 = list(b5)
                b7.append(branch)
                b2.append(b7)
            b3.add(b6)
        b8 = len(b2)
        if b8 = = 0:
            print("NOT FOUND 404")
print(fonk1(b1,'ALASKA','INDIANA'))
   README Content:
BFS dan DFS
