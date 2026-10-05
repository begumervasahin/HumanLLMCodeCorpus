def fonk1(file_name):
    b1 = []
    b2 = []
    b3 = []
    with open(file_name, 'r') as file:
        b4 = file.readline().split()[:-1]
        b1 = b4
        for line in file:
            b5 = line.split()
            b3.append(b5[-1])
            b2.append(b5[:-1])
    return b1, b2, b3
def fonk2(b2, class_labels, attribute_names):
    b6 = len(b2)
    b7 = len(attribute_names)
    b8 = []
    b9 = []
    for i in range(b7):
        b10 = [int(b5[i]) for b5 in b2]
        b11 = b10.count(0)
        b12 = b6 - b11
        b13 = b11
        b14 = b12
        b8.append(b11 / b6)
        b8.append(b12 / b6)
        b9.append(b13 / b6)
        b9.append(b14 / b6)
    return b8, b9
def fonk3(b2, class_labels, b8, b9, c0, c1):
    a1 = 0
    for instance, true_label in zip(b2, class_labels):
        b15 = fonk4(instance, b8, b9, c0, c1)
        if b15 = = true_label:
            a1 += 1
    return a1 / len(b2) * 100
def fonk4(instance, b8, b9, c0, c1):
    b16 = c0
    b17 = c1
    for b18, prob_0_attr, prob_1_attr in zip(instance, b8, b9):
        if b18 = = '0':
            b16 *= prob_0_attr
            b17 *= prob_1_attr
        else:
            b16 *= (1 - prob_0_attr)
            b17 *= (1 - prob_1_attr)
    return '1' if b17 > b16 else '0'
b19 = input('\nPlease input the name of the training dataset (with file extension): ')
b20 = input('\nPlease input the name of the test dataset (with file extension): ')
att_list_train, data_train, b21 = fonk1(b19)
att_list_test, data_test, b22 = fonk1(b20)
prob_0_train, b23 = fonk2(data_train, b21, att_list_train)
b24 = b21.count('0') / len(b21)
b25 = b21.count('1') / len(b21)
print('Class probabilities:')
print('P(b26 = 0):', b24)
print('P(b26 = 1):', b25)
print('\nConditional probabilities:')
for i, att_name in enumerate(att_list_train):
    print('P({} = 0|b26 = 0): {:.2f}'.format(att_name, prob_0_train[2 * i]), end=' ')
    print('P({} = 1|b26 = 0): {:.2f}'.format(att_name, prob_0_train[2 * i + 1]), end=' ')
    print('P({} = 0|b26 = 1): {:.2f}'.format(att_name, b23[2 * i]), end=' ')
    print('P({} = 1|b26 = 1): {:.2f}'.format(att_name, b23[2 * i + 1]))
b27 = fonk3(data_train, b21, prob_0_train, b23, b24, b25)
print('\nAccuracy on the training set is: {:.2f}%'.format(b27))
b28 = fonk3(data_test, b22, prob_0_train, b23, b24, b25)
print('Accuracy on the test set is: {:.2f}%'.format(b28))