def fonk1(array, a2, j):
    array[a2], array[j] = array[j],array[a2]
def fonk2(array):
    a1 = 0
    b1 = len(array)-1
    fonk3(array, a1, b1)
def fonk3(array, a1, b1):
    if a1 < b1 :
        b2 = fonk4(array, a1, b1)
        fonk3(array, a1, b2)
        fonk3(array, b2+1, b1)
def fonk4(array, a1, b1):
    b3 = (a1 + b1)
    b4 = array[b3][2]
    fonk1(array, a1, b3)
    b5 = a1
    for k in range(a1+1, b1+1):
        if array[k][2] < b4:
            b5 += 1
            fonk1(array, k, b5)
    fonk1(array, a1, b5)
    return b5
""""
def fonk5(b6):
    if b17[b6] == b6:
        return b6
    else:
        b17[b6] = fonk5(b17[b6])
        return b17[b6]
def fonk6(b6, b7):
    b6 = fonk5(b6)
    b7 = fonk5(b7)
    if b18[b6] < b18[b7]:
        b17[b6] = b7
    else:
        b17[b7] = b6
        if b18[b6] == b18[b7]:
            b18[b6] += 1
b8 = []
b9 = 'inputgraphfile.txt'
b10 = open(b9)
b10 = b10.read()
b11 = b10.splitlines()
for a2 in range(len(b11)):
    b12 = b11[a2].split(' ')
    b13 = int(b12[0])
    b14 = int(b12[1])
    b15 = int(b12[2])
    b8.append([b13,b14,b15])
    if b13>=b14:
        b16 = b13
    else:
        b16 = b14
b16+=1
b17 = []
for j in range(b16):
    b17.append(j)
b18 = [0] * b16
b19 = []
fonk2(b8)
a2 = 0
for edge in b8:
    b13, b14, b20 = b8[a2]
    a2 = a2 + 1
    if fonk5(b13) != fonk5(b14):
        b19.append([b13, b14, b20])
        fonk6(b13, b14)
b10 = open('output_kruskal.txt', 'b15')
for b13,b14,b15 in b19:
    b10.write(str(b13) + " ")
    b10.write(str(b14) + " ")
    b10.write(str(b15) + " "+ "\n")
b10.close()