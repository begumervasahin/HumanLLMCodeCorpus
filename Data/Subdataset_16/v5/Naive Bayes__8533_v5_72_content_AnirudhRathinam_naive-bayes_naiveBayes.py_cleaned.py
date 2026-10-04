import numpy as np
def fonk1(filename):
    b2, data, b1 = [], [], []
    with open(filename, 'r') as file:
        b2 = file.readline().strip().split()[:-1]
        b3 = len(b2)
        for line in file:
            b4 = line.strip().split()
            data.append(b4[:-1])
            b1.append(b4[-1])
    b5 = len(data)
    return b2, data, b1, b3, b5
def fonk2(data, b1, b3, b5):
    b6 = b1.count('0') / len(b1)
    b7 = b1.count('1') / len(b1)
    prob_0, b8 = [], []
    for i in range(b3):
        b9 = c_0_t_1_count = c_1_t_0_count = c_1_t_1_count = t_0_count = t_1_count = 0
        for j in range(b5):
            if data[j][i] == '0':
                t_0_count += 1
                if b1[j] == '0':
                    b9 += 1
                else:
                    c_0_t_1_count += 1
            elif data[j][i] == '1':
                t_1_count += 1
                if b1[j] == '1':
                    c_1_t_1_count += 1
                else:
                    c_1_t_0_count += 1
        prob_0.extend([b9 / t_0_count, c_0_t_1_count / t_0_count])
        b8.extend([c_1_t_0_count / t_1_count, c_1_t_1_count / t_1_count])
    return prob_0, b8, b6, b7
def fonk3(prob_0, b8, b6, b7, att_list, b3):
    print(f'P(b10 = 0): {b6}')
    for i in range(b3):
        print(f'P({att_list[i]} = 0 | b10 = 0): {prob_0[i*2]:.2f}  P({att_list[i]} = 1 | b10 = 0): {prob_0[i*2+1]:.2f}', end=' ')
    print('\n')
    print(f'P(b10 = 1): {b7}')
    for i in range(b3):
        print(f'P({att_list[i]} = 0 | b10 = 1): {b8[i*2]:.2f}  P({att_list[i]} = 1 | b10 = 1): {b8[i*2+1]:.2f}', end=' ')
    print('\n')
def fonk4(b4, prob_0, b8, b6, b7):
    p0, b11 = b6, b7
    for i in range(len(b4)):
        if b4[i] == '0':
            p0 *= prob_0[i * 2]
            b11 *= b8[i * 2]
        else:
            p0 *= prob_0[i * 2 + 1]
            b11 *= b8[i * 2 + 1]
    return '1' if b11 > p0 else '0'
def fonk5(data, b1, prob_0, b8, b6, b7, b5):
    a1 = 0
    for i in range(b5):
        b12 = fonk4(data[i], prob_0, b8, b6, b7)
        if b12 = = b1[i]:
            a1 += 1
    return (a1 / b5) * 100
def fonk6():
    b13 = input('Please input name of training dataset (with file extension): ')
    b14 = input('Please input name of test dataset (with file extension): ')
    att_list, train_data, train_class_list, b3, b15 = fonk1(b13)
    prob_0, b8, b6, b7 = fonk2(train_data, train_class_list, b3, b15)
    fonk3(prob_0, b8, b6, b7, att_list, b3)
    b16 = fonk5(train_data, train_class_list, prob_0, b8, b6, b7, b15)
    print(f'\nAccuracy on training set ({b15} instances): {b16:.2f}%')
    att_list, test_data, test_class_list, b3, b17 = fonk1(b14)
    b18 = fonk5(test_data, test_class_list, prob_0, b8, b6, b7, b17)
    print(f'\nAccuracy on test set ({b17} instances): {b18:.2f}%')
if b19 = = '__main__':
    fonk6()