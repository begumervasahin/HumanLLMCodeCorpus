import numpy as np
def fonk1(filename):
    b1 = []
    b2 = []
    b3 = []
    with open(filename, 'r') as file:
        b4 = file.readline().strip()
        for i in b4.split()[:-1]:
            b1.append(i)
        b5 = len(b1)
        for line in file:
            b6 = line.split()
            b2.append(b6[:b5])
            b3.append(b6[b5])
    return b1, b2, b3
def fonk2(b2, b3, b5):
    b7 = []
    b8 = []
    b9 = b3.count('0') / len(b3)
    b10 = b3.count('1') / len(b3)
    for i in range(b5):
        b11 = [b14[i] for b14 in b2]
        b12 = c_0_t_1_count = c_1_t_0_count = c_1_t_1_count = t_0_count = t_1_count = 0
        for b17 in range(len(b2)):
            if b11[b17] == '0':
                t_0_count += 1
                if b3[b17] == '0':
                    b12 += 1
                else:
                    c_0_t_1_count += 1
            if b11[b17] == '1':
                t_1_count += 1
                if b3[b17] == '1':
                    c_1_t_1_count += 1
                else:
                    c_1_t_0_count += 1
        b7.append(b12 / t_0_count)
        b7.append(c_0_t_1_count / t_0_count)
        b8.append(c_1_t_0_count / t_1_count)
        b8.append(c_1_t_1_count / t_1_count)
    return b9, b10, b7, b8
def fonk3(b9, b10, b7, b8, b1):
    print(f'P(b13 = 0): {b9}')
    for i in range(len(b1)):
        print(f'P({b1[i]} = 0|b13 = 0): {b7[2 * i]:.2f} P({b1[i]} = 1|b13 = 0): {b7[2 * i + 1]:.2f}', end=' ')
    print('\n')
    print(f'P(b13 = 1): {b10}')
    for i in range(len(b1)):
        print(f'P({b1[i]} = 0|b13 = 1): {b8[2 * i]:.2f} P({b1[i]} = 1|b13 = 1): {b8[2 * i + 1]:.2f}', end=' ')
def fonk4(b14, b7, b8, b9, b10):
    b14 = list(map(int, b14))
    b15 = b9
    b16 = b10
    for i in range(len(b14)):
        b17 = i * 2
        if b14[i] == 0:
            b15 *= b7[b17]
            b16 *= b8[b17]
        else:
            b15 *= b7[b17 + 1]
            b16 *= b8[b17 + 1]
    return '1' if b16 > b15 else '0'
def fonk5(b2, b3, b7, b8, b9, b10):
    a1 = 0
    for i in range(len(b2)):
        if fonk4(b2[i], b7, b8, b9, b10) == b3[i]:
            a1 += 1
    return (a1 / len(b2)) * 100
def fonk6():
    b18 = input('\nPlease input name of training dataset (with file extension): ')
    b19 = input('\nPlease input name of b19 dataset (with file extension): ')
    b1, b2, b3 = fonk1(b18)
    b5 = len(b1)
    b20 = len(b2)
    b9, b10, b7, b8 = fonk2(b2, b3, b5)
    fonk3(b9, b10, b7, b8, b1)
    b21 = fonk5(b2, b3, b7, b8, b9, b10)
    print(f'\n\nAccuracy on training set ({b20} instances) is: {b21:.2f}%')
    b1, b2, b3 = fonk1(b19)
    b20 = len(b2)
    b22 = fonk5(b2, b3, b7, b8, b9, b10)
    print(f'\n\nAccuracy on b19 set ({b20} instances) is: {b22:.2f}%')
if b23 = = "__main__":
    fonk6()