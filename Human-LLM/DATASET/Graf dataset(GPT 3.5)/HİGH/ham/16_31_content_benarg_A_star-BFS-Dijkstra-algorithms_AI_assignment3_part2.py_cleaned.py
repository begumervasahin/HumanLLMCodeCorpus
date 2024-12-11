31. Repository: benarg/A_star-BFS-Dijkstra-algorithms
   File: AI_assignment3_part2.py
   URL: https:
   Code Content:
from PIL import Image, ImageDraw
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
        def fonk2(self, b4, b5):
            self.b4 = b4
            self.b5 = b5
            self.b6 = None
            self.b7 = None
            self.b8 = None
            self.b9 = None
            self.b10 = []
def fonk3(filename):
    with b27(filename, 'r') as file:
        b11 = file.read()
        file.close()
    b11 = b11.split('\n')
    b11 = b11[:-1]
    b12 = []
    for i, e1 in enumerate(b11):
        b13 = []
        a1 = 0
        for b14 in e1:
            b13.append(class2(class1(a1, len(b11) - i - 1, b14), fonk9(b14)))
            if b14 = = 'A':
                b15 = (a1, len(b11) - i - 1)
            elif b14 = = 'B':
                b16 = (a1, len(b11) - i - 1)
            a1 += 1
        b12.append(b13)
    b12.reverse()
    return b15, b16, b12
def fonk4(s1, s2):
    return(abs(s2.b1 - s1.b1) + abs(s2.b1 - s1.b1))
def fonk5(s1, sf):
    if s1.b1 = = sf.b1 and s1.b2 == sf.b2:
        return True
    else:
        return False
def fonk6(s, b12):
    b17 = []
    if s.b1 > 0:
        b17.append(b12[s.b2][s.b1-1])
    if s.b1 < (len(b12[s.b2]) - 1):
        b17.append(b12[s.b2][s.b1+1])
    if s.b2 > 0:
        b17.append(b12[s.b2-1][s.b1])
    if s.b2 < (len(b12) - 1):
        b17.append(b12[s.b2+1][s.b1])
    return b17
def fonk7(C, P, sf):
    C.b9 = P
    C.b6 = P.b6 + C.b5
    b7 = fonk4(C.b4, sf)
    C.b7 = b7
    C.b8 = b7 + C.b6
def fonk8(P):
    for b23 in P.b10:
        if P.b6 + b23.b5 < b23.b6:
            b23.b9 = P
            b23.b6 = P.b6 + b23.b5
            b23.b8 = b23.b6 + b23.b7
            fonk8(b23)
def fonk9(b3):
    if b3 = = 'w':
        return 100
    elif b3 = = 'm':
        return 50
    elif b3 = = 'b8':
        return 10
    elif b3 = = 'b6':
        return 5
    elif b3 = = 'r':
        return 1
    else:
        return 1
def fonk10(n):
    if n.b4.b3 = = 'w':
        return (73,216,245)
    elif n.b4.b3 = = 'm':
        return (99,99,99)
    elif n.b4.b3 = = 'b8':
        return (3,82,0)
    elif n.b4.b3 = = 'b6':
        return (50,200,50)
    elif n.b4.b3 = = 'r':
        return (114,80,41)
    elif n.b4.b3 = = 'A':
        return (90,180,90)
    elif n.b4.b3 = = 'B':
        return (255,90,90)
def fonk11(b28, b29, b12, name):
    b18 = b29
    b19 = []
    b19.append(b29)
    while b18 != b28:
        b18 = b18.b9
        b19.append(b18)
    b12.reverse()
    fonk12(b12, b19, name)
    b20 = ''
    for b18 in b19[1:-1]:
        b18.b4.b3 = 'O'
    for b13 in b12:
        for e in b13:
            b20 += e.b4.b3
        b20 += '\n'
    print(b20)
def fonk12(b12, b19, name):
    b21 = Image.new( 'RGB', (len(b12[0])*20,len(b12)*20), "white")
    b22 = ImageDraw.Draw(b21)
    for b2 in range(0,len(b12)):
        for b1 in range(0,len(b12[0])):
            b23 = fonk10(b12[b2][b1])
            b22.rectangle([(b1*20,b2*20),(b1*20+20,b2*20+20)], b24 = b23, outline=(0,0,0))
            if b12[b2][b1] in b19:
                b23 = (107,97,255)
                b22.rectangle([(b1*20+6,b2*20+6),(b1*20+14,b2*20+14)], b24 = b23, outline=(0,0,0))
    b25 = "assignment3_images/part2_" + name + ".png"
    b21.save(b25,"PNG")
def fonk13(b15, b16, b12, name):
    b26 = []
    b27 = []
    b28 = b12[b15[1]][b15[0]]
    b29 = b12[b16[1]][b16[0]]
    b28.b6 = 0
    b7 = fonk4(b28.b4, b29.b4)
    b28.b7 = b7
    b28.b8 = b7
    b27.append(b28)
    b30 = True
    while  b30:
        if b27 = = []:
            return 'FAIL'
        b18 = b27.pop()
        b26.append(b18)
        if fonk5(b18.b4, b29.b4):
            fonk11(b28, b29, b12, name)
            return 'SUCCEED'
        b17 = fonk6(b18.b4, b12)
        for s in b17:
            b18.b10.append(s)
            if s not in b27 and s not in b26:
                fonk7(s, b18, b29.b4)
                b27.append(s)
                b27.sort(b31 = lambda e: e.b8, reverse=True)
            elif b18.b6 + s.b5 < s.b6:
                fonk7(s, b18, b29.b4)
                if s in b26:
                    fonk8(s)
b15,b16, b12 = fonk3('boards/b12-2-1.txt')
b12 = fonk13(b15,b16,b12, 'b12-2-1')
b15,b16, b12 = fonk3('boards/b12-2-2.txt')
b12 = fonk13(b15,b16,b12, 'b12-2-2')
b15,b16, b12 = fonk3('boards/b12-2-3.txt')
b12 = fonk13(b15,b16,b12, 'b12-2-3')
b15,b16, b12 = fonk3('boards/b12-2-4.txt')
b12 = fonk13(b15,b16,b12, 'b12-2-4')
   README Content:
ImplÃ©mentation des algorithmes A*, Breadth First Search et Dijkstra pour trouver le plus court chemin.
