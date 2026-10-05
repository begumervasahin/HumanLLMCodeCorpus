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
        b5 = [(j, b2[i][j]) for j in range(len(b2[i])) if b2[i][j] != "1024"]
        b4.append(b5)
    return b4
def fonk3(b4, b17, b9):
    b6 = [0] * len(b4)
    b7 = []
    b8 = [0] * len(b4)
    b17, b9 = int(b17), int(b9)
    b6[b17] = 1
    b10 = b17
    a1 = 0
    b7.append(f'- {b17} 0')
    while b6[b9] != 1:
        b11 = b4[b10][0][0]
        b12 = int(b4[b10][0][1]) + a1
        for b13, distance in b4[b10][1:]:
            if not b6[b13]:
                if b13 = = b9:
                    b14 = b10
                elif distance + a1 < b12:
                    b11 = b13
                    b12 = distance + a1
                    b14 = b10
            elif b14 = = b17 or b6[b11]:
                b11 = b13
                b12 = distance + a1
        if not b14:
            b14 = b10
        b15 = int(b7[b8[b14]][0].split()[2])
        if len(b7) > 2 and b14 != b17 and b11 != b9:
            for b13, distance in b4[b14]:
                if not b6[b13]:
                    b16 = distance + b15
                    if b16 < b12:
                        b11 = b13
                        b12 = b16
        b7.append(f'{b14} {b11} {b12}')
        b6[b11] = 1
        b8[b11] = len(b7) - 1
        b10 = b11
        a1 = b12
    return b7
def fonk4(b7, b17, b9):
    if b17 = = b9:
        print(b17)
    else:
        b18 = ''
        b18 += b7[-1][0].split()[1] + ' '
        b19 = b7[-1][0].split()[0]
        while int(b19) != int(b17):
            for i in range(1, len(b7) - 1):
                if b7[i][0].split()[1] == b19:
                    b18 += b7[i][0].split()[1] + ' '
                    b19 = b7[i][0].split()[0]
        b18 += b7[0][0].split()[1]
        print(b18[::-1])
if b20 = = '__main__':
    file_path, start_node, b21 = sys.argv[1:]
    b4 = fonk2(fonk1(file_path))
    b7 = fonk3(b4, start_node, b21)
    fonk4(b7, start_node, b21)