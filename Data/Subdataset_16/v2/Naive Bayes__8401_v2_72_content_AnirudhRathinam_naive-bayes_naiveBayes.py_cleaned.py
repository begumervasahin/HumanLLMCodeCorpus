import numpy as np
def fonk1(filename):
    b1 = []
    b2 = []
    b3 = []
    with open(filename, 'r') as file:
        b4 = file.readline().strip().split()
        b1 = b4[:-1]
        for line in file:
            b5 = line.split()
            b2.append(b5[:-1])
            b3.append(b5[-1])
    return b1, b2, b3
def fonk2(b2, b3, b18):
    b6 = []
    b7 = []
    b8 = b3.count('0') / len(b3)
    b9 = b3.count('1') / len(b3)
    for i in range(b18):
        b10 = count_c0_t1 = count_c1_t0 = count_c1_t1 = 0
        b11 = count_t1 = 0
        for j in range(len(b2)):
            if b2[j][i] == '0':
                b11 += 1
                if b3[j] == '0':
                    b10 += 1
                else:
                    count_c0_t1 += 1
            else:
                count_t1 += 1
                if b3[j] == '1':
                    count_c1_t1 += 1
                else:
                    count_c1_t0 += 1
        b6.extend([b10 / b11, count_c0_t1 / b11])
        b7.extend([count_c1_t0 / count_t1, count_c1_t1 / count_t1])
    return b8, b9, b6, b7
def fonk3(b8, b9, b6, b7, b1):
    print(f'P(b12 = 0): {b8}')
    for i, att in enumerate(b1):
        print(f'P({att} = 0|b12 = 0): {b6[2 * i]:.2f} P({att} = 1|b12 = 0): {b6[2 * i + 1]:.2f}', end=' ')
    print('\n')
    print(f'P(b12 = 1): {b9}')
    for i, att in enumerate(b1):
        print(f'P({att} = 0|b12 = 1): {b7[2 * i]:.2f} P({att} = 1|b12 = 1): {b7[2 * i + 1]:.2f}', end=' ')
def fonk4(row, b6, b7, b8, b9):
    b13 = b8
    b14 = b9
    for i in range(len(row)):
        if row[i] == '0':
            b13 *= b6[2 * i]
            b14 *= b7[2 * i]
        else:
            b13 *= b6[2 * i + 1]
            b14 *= b7[2 * i + 1]
    return '1' if b14 > b13 else '0'
def fonk5(b2, b3, b6, b7, b8, b9):
    a1 = 0
    for i in range(len(b2)):
        if fonk4(b2[i], b6, b7, b8, b9) == b3[i]:
            a1 += 1
    return (a1 / len(b2)) * 100
def fonk6():
    b15 = input('Please input the name of the training dataset (with file extension): ')
    b16 = input('Please input the name of the test dataset (with file extension): ')
    b1, train_data, b17 = fonk1(b15)
    b18 = len(b1)
    b8, b9, b6, b7 = fonk2(train_data, b17, b18)
    fonk3(b8, b9, b6, b7, b1)
    b19 = fonk5(train_data, b17, b6, b7, b8, b9)
    print(f'\n\nAccuracy on training set ({len(train_data)} instances): {b19:.2f}%')
    b1, test_data, b20 = fonk1(b16)
    b21 = fonk5(test_data, b20, b6, b7, b8, b9)
    print(f'\n\nAccuracy on test set ({len(test_data)} instances): {b21:.2f}%')
if b22 = = "__main__":
    fonk6()