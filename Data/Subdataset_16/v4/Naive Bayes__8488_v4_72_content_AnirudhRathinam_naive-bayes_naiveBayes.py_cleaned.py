import numpy as np
def fonk1(filename):
    b2, data, b1 = [], [], []
    a1 = 0
    with open(filename, 'r') as file:
        b2 = file.readline().split()[:-1]
        b3 = len(b2)
        for line in file:
            a1 += 1
            b1.append(line.split()[b3])
            data.append(line.split())
    return b2, data, b1, b3, a1
def fonk2(data, b1, b3, a1):
    b4 = b1.count('0') / len(b1)
    b5 = b1.count('1') / len(b1)
    prob_0, b6 = [], []
    for i in range(b3):
        b7 = [row[i] for row in data]
        b8 = c_0_t_1_count = c_1_t_0_count = c_1_t_1_count = t_0_count = t_1_count = 0
        for j in range(a1):
            if b7[j] == '0':
                t_0_count += 1
                if b1[j] == '0':
                    b8 += 1
                else:
                    c_0_t_1_count += 1
            elif b7[j] == '1':
                t_1_count += 1
                if b1[j] == '1':
                    c_1_t_1_count += 1
                else:
                    c_1_t_0_count += 1
        prob_0.append(b8 / t_0_count)
        prob_0.append(c_0_t_1_count / t_0_count)
        b6.append(c_1_t_0_count / t_1_count)
        b6.append(c_1_t_1_count / t_1_count)
    return prob_0, b6, b4, b5
def fonk3(prob_0, b6, b4, b5, att_list, b3):
    print(f'P(b9 = 0): {b4}')
    for i in range(b3):
        print(f'P({att_list[i]} = 0 | b9 = 0): {prob_0[i*2]:.2f}  P({att_list[i]} = 1 | b9 = 0): {prob_0[i*2+1]:.2f}', end=' ')
    print('\n\n')
    print(f'P(b9 = 1): {b5}')
    for i in range(b3):
        print(f'P({att_list[i]} = 0 | b9 = 1): {b6[i*2]:.2f}  P({att_list[i]} = 1 | b9 = 1): {b6[i*2+1]:.2f}', end=' ')
    print('\n\n')
def fonk4(row, prob_0, b6, b4, b5):
    p0, b10 = b4, b5
    for i in range(len(row) - 1):
        if row[i] == '0':
            p0 *= prob_0[i * 2]
            b10 *= b6[i * 2]
        else:
            p0 *= prob_0[i * 2 + 1]
            b10 *= b6[i * 2 + 1]
    return '1' if b10 > p0 else '0'
def fonk5(data, b1, prob_0, b6, b4, b5, a1):
    a2 = 0
    for i in range(a1):
        b11 = fonk4(data[i], prob_0, b6, b4, b5)
        if b11 = = b1[i]:
            a2 += 1
    return (a2 / a1) * 100
def fonk6():
    b12 = input('\nPlease input name of training dataset (with file extension): ')
    b13 = input('\nPlease input name of test dataset (with file extension): ')
    att_list, data, b1, b3, a1 = fonk1(b12)
    prob_0, b6, b4, b5 = fonk2(data, b1, b3, a1)
    fonk3(prob_0, b6, b4, b5, att_list, b3)
    b14 = fonk5(data, b1, prob_0, b6, b4, b5, a1)
    print(f'\n\nAccuracy on training set ({a1} instances) is: {b14:.2f}%')
    att_list, data, b1, b3, a1 = fonk1(b13)
    b15 = fonk5(data, b1, prob_0, b6, b4, b5, a1)
    print(f'\n\nAccuracy on test set ({a1} instances) is: {b15:.2f}%')
if b16 = = '__main__':
    fonk6()