def fonk1(b12,b7,b4,b5):
    for b3 in range(b5):
        b1 = [b4]
        if(g[b4][b3]!=0):
            b1.append(b3)
            b7.append(b1)
    return
def fonk2(b12,b7,b8):
    a1 = 9999999
    for edge in b7:
        if(b12[edge[0]][edge[1]]!=0):
             if((b8[edge[0]]==1 and b8[edge[1]]==0) and b12[edge[0]][edge[1]]<a1):
               a1 = b12[edge[0]][edge[1]]
               b2 = edge[0]
               b3 = edge[1]
    b8[b3]=1
    return [b2,b3]
def fonk3(b12,b7,b10,b5):
    for edge in b7:
        if(edge[1]==b10):
            b7.remove(edge)
    fonk1(b12,b7,b10,b5)
    return
def fonk4(b12,b14):
    b4 = [b14]
    b5 = len(b12)
    b6 = []
    b7 = []
    fonk1(b12,b7,b14,b5)
    b8 = []
    for b2 in range(b5):
        b8.append(0)
    b8[b14]=1
    for b2 in range(b5-1):
        b9 = fonk2(b12,b7,b8)
        b6.append(b9)
        b10 = b9[1]
        b4.append(b10)
        fonk3(b12,b7,b10,b5)
    a2 = 0
    for b2 in b6:
        a2 = a2+b12[b2[0]][b2[1]]
    b11 = []
    for b2 in range(b5):
        b1 = []
        for b3 in range(b5):
            b1.append(0)
        b11.append(b1)
    for b2 in b6:
        b11[b2[0]][b2[1]]=b12[b2[0]][b2[1]]
    for b2 in b6:
        b11[b2[1]][b2[0]]=b12[b2[0]][b2[1]]
    print("The total cost is :",a2)
    print("The minimum spanning tree is ")
    for b2 in b11:
        print(b2)
    return b11
b5 = int(input("Enter the number of b4"))
b12 = []
for b2 in range(b5):
    b1 = []
    for b3 in range(b5):
        print("Enter the value for edge ",b2,b3)
        b13 = int(input())
        b1.append(b13)
    b12.append(b1)
b14 = int(input("Enter the b14 b4:"))
fonk4(b12,b14)