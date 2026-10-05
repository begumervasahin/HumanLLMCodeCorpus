import sys
def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = []
    for line in b1:
        b3 = [cell.strip() for cell in line.split()]
        b2.append(b3)
    return b2
def fonk2(b2):
    b4 = []
    for i in range(len(b2)):
        b5 = []
        for j in range(len(b2[i])):
            if b2[i][j] != "1024":
                b5.append(f"{j} {b2[i][j]}")
        b4.append(b5)
    return b4
def fonk3(b4, b9, b10):
    b6 = [0] * len(b4)
    b7 = []
    b8 = [0] * len(b4)
    b9 = int(b9)
    b10 = int(b10)
    b6[b9] = 1
    b11 = b9
    a1 = 0
    b7.append(f'- {b9} 0')
    while b6[b10] != 1:
        b12 = b4[b11][0].split()[0]
        b13 = int(b4[b11][0].split()[1]) + a1
        for i in range(1, len(b4[b11])):
            b15, b14 = map(int, b4[b11][i].split())
            if not b6[b15]:
                if b15 = = b10:
                    b16 = b11
                elif b14 + a1 < b13:
                    b12 = b15
                    b13 = b14 + a1
                    b16 = b11
            elif b16 = = b9 or b6[b12]:
                b12 = b15
                b13 = b14 + a1
        if not b16:
            b16 = b11
        b17 = int(b7[b8[b16]][0].split()[2])
        if len(b7) > 2 and b16 != b9 and b12 != b10:
            for i in range(len(b4[b16])):
                b15, b14 = map(int, b4[b16][i].split())
                if not b6[b15]:
                    b18 = b14 + b17
                    if b18 < b13:
                        b12 = b15
                        b13 = b18
        b7.append(f'{b16} {b12} {b13}')
        b6[b12] = 1
        b8[b12] = len(b7) - 1
        b11 = b12
        a1 = b13
    return b7
def fonk4(b7, b9, b10):
    if b9 = = b10:
        print(b9)
    else:
        b19 = ''
        b19 += b7[-1][0].split()[1] + ' '
        b20 = b7[-1][0].split()[0]
        while int(b20) != int(b9):
            for i in range(1, len(b7) - 1):
                if b7[i][0].split()[1] == b20:
                    b19 += b7[i][0].split()[1] + ' '
                    b20 = b7[i][0].split()[0]
        b19 += b7[0][0].split()[1]
        print(b19[::-1])
if b21 = = '__main__':
    file_path, start_node, b22 = sys.argv[1:]
    b4 = fonk2(fonk1(file_path))
    b7 = fonk3(b4, start_node, b22)
    fonk4(b7, start_node, b22)