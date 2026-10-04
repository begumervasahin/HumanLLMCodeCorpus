import random
def fonk1(b16):
        b1 = []
        for i in range(b16):
                b1.append([])
        for i in range(2, b16):
                b2 = random.randint(1, i-1)
                for j in range(b2):
                    b3 = random.randint(0, b16-1)
                    b4 = random.randint(10, 100)
                    b1[i].append((b3, b4))
                    b1[b3].append((i, b4))
        b5 = []
        for i in range(b16):
                b6 = []
                for j in range(b16):
                        b6.append(0)
                b5.append(b6)
        for i in range(b16):
                for j in range(len(b1[i])):
                        b7 = b1[i][j][0]
                        b8 = b1[i][j][1]
                        b5[i][b7] = b8
        return(b5)
def fonk2(G):
        b9 = random.randint(0,len(G)-1)
        a1 = 0
        b10 = []
        b11 = []
        for i in range(0,len(G)):
                b11.append(0)
        b11[b9] = 1
        b10.append(b9)
        while (len(b10) != 0):
                b2 = b10.pop(0)
                for y in range(0, len(b11)):
                        if ((G[b2][y] > 0) and (b11[y] == 0)):
                                b11[y] = 1
                                b10.append(y)
                                a1 += G[b2][y]
        return(a1)
def fonk3(G):
        a1 = 0
        b12 = random.randint(0,len(G)-1)
        b13 = [[],[],[]]
        for b2 in range(0,3):
                for y in range(0,len(G)):
                        b13[b2].append("empty")
        b13[0][b12] = "N"
        for i in range(1,len(G)):
                b13[0][i] = "Y"
                b13[2][i] = 1000
        for i in range(0,len(G)):
                if (G[0][i] > 0):
                        b13[1][i] = b12
                        b13[2][i] = G[b12][i]
        b14 = [0]
        b15 = []
        while (len(b14) < len(G)):
                a2 = 1000
                for i in range(0,len(G)):
                        if ((b13[0][i] == "Y") and (b13[2][i] < a2)):
                                a2 = b13[2][i]
                                b2 = i
                b14.append(b2)
                b15.append((b2,b13[1][b2]))
                a1 += b13[2][b2]
                b13[0][b2] = "N"
                for y in range(0,len(G)):
                        if (G[b2][y] > 0):
                                if ((b13[0][y] == "Y") and (G[b2][y] < b13[2][y])):
                                        b13[1][y] =  b2
                                        b13[2][y] = G[b2][y]
        return(a1)
def fonk4():
        b16 = [20, 30, 40, 50, 60]
        a3 = 1000
        for b2 in range(len(b16)):
                a4 = 0
                for y in range(0,a3):
                        b17 = fonk1(b16[b2])
                        b18 = fonk2(b17)
                        b19 = fonk3(b17)
                        b20 = ((b18/b19) - 1) * 100
                        a4 += b20
                b21 = a4/a3
                print("Average of b20 for b16 = " + str(b16[b2]) + ": " + str(b21))
fonk4()