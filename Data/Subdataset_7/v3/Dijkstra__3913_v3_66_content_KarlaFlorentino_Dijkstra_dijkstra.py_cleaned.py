import sys
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = []
    for line in b1:
        b3 = [int(cell) for cell in line.strip().split()]
        b2.append(b3)
    return b2
def fonk2(b2):
    b4 = []
    for i in range(len(b2)):
        b4.append([(j, b2[i][j]) for j in range(len(b2)) if b2[i][j] != 1024])
    return b4
def fonk3(b4, b14, end):
    b5 = [0] * len(b4)
    b6 = []
    b7 = [0] * len(b4)
    b8 = int(b14)
    a1 = 0
    b9 = ""
    a2 = 0
    b10 = ""
    b11 = ""
    b6.append(f'- {b14} 0')
    b5[int(b14)] = 1
    while b5[int(end)] != 1:
        b10 = b4[b8][0][0]
        b11 = int(b4[b8][0][1]) + a1
        for i in range(1, len(b4[b8])):
            if b5[int(b10)] != 1:
                if int(b10) == int(end):
                    b9 = b8
                else:
                    b12 = b4[b8][i][0]
                    if b5[int(b12)] != 1:
                        b13 = int(b4[b8][i][1]) + a1
                        if b13 < b11:
                            b10 = b12
                            b11 = b13
                            b9 = b8
            elif b9 = = int(b14) or b5[int(b10)] == 1:
                b10 = b4[b8][i][0]
                b11 = int(b4[b8][i][1]) + a1
        if b9 = = "":
            b9 = b8
        a2 = int(b6[b7[int(b9)]][0].split(" ")[2])
        if len(b6) > 2 and b9 != int(b14) and int(b10) != int(end):
            for i in range(len(b4[int(b9)])):
                b12 = b4[int(b9)][i][0]
                if b5[int(b12)] != 1:
                    b13 = int(b4[int(b9)][i][1]) + a2
                    if b13 < b11:
                        b10 = b4[int(b9)][i][0]
                        b11 = b13
        b6.append(f'{b9} {b10} {b11}')
        b5[int(b10)] = 1
        b7[int(b10)] = len(b6) - 1
        b8 = int(b10)
        a1 = int(b11)
    return b6
def fonk4(b6, b14, end):
    if b14 = = end:
        print(b14)
    else:
        b15 = ""
        b15 += b6[-1][0].split(" ")[1] + " "
        b16 = b6[-1][0].split(" ")[0]
        while int(b16) != int(b14):
            for i in range(1, len(b6) - 1):
                if b6[i][0].split(" ")[1] == b16:
                    b15 += b6[i][0].split(" ")[1] + " "
                    b16 = b6[i][0].split(" ")[0]
        b15 += b6[0][0].split(" ")[1]
        print(b15[::-1])
if b17 = = "__main__":
    file_path, start_node, b18 = sys.argv[1:]
    b4 = fonk2(fonk1(file_path))
    b6 = fonk3(b4, start_node, b18)
    fonk4(b6, start_node, b18)