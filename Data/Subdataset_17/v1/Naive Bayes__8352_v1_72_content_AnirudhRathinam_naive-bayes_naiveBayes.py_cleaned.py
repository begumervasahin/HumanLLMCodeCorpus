import numpy as np
def load_data(filename):
    att_list = []
    data = []
    class_list = []
    with open(filename, 'r') as file:
        attributes = file.readline().strip()
        for i in attributes.split()[:-1]:
            att_list.append(i)
        cols = len(att_list)
        for line in file:
            parts = line.split()
            data.append(parts[:cols])
            class_list.append(parts[cols])
    return att_list, data, class_list
def calculate_probabilities(data, class_list, cols):
    prob_0 = []
    prob_1 = []
    c0 = class_list.count('0') / len(class_list)
    c1 = class_list.count('1') / len(class_list)
    for i in range(cols):
        tmp_list = [row[i] for row in data]
        c_0_t_0_count = c_0_t_1_count = c_1_t_0_count = c_1_t_1_count = t_0_count = t_1_count = 0
        for j in range(len(data)):
            if tmp_list[j] == '0':
                t_0_count += 1
                if class_list[j] == '0':
                    c_0_t_0_count += 1
                else:
                    c_0_t_1_count += 1
            if tmp_list[j] == '1':
                t_1_count += 1
                if class_list[j] == '1':
                    c_1_t_1_count += 1
                else:
                    c_1_t_0_count += 1
        prob_0.append(c_0_t_0_count / t_0_count)
        prob_0.append(c_0_t_1_count / t_0_count)
        prob_1.append(c_1_t_0_count / t_1_count)
        prob_1.append(c_1_t_1_count / t_1_count)
    return c0, c1, prob_0, prob_1
def print_probabilities(c0, c1, prob_0, prob_1, att_list):
    print(f'P(C = 0): {c0}')
    for i in range(len(att_list)):
        print(f'P({att_list[i]} = 0|C = 0): {prob_0[2 * i]:.2f} P({att_list[i]} = 1|C = 0): {prob_0[2 * i + 1]:.2f}', end=' ')
    print('\n')
    print(f'P(C = 1): {c1}')
    for i in range(len(att_list)):
        print(f'P({att_list[i]} = 0|C = 1): {prob_1[2 * i]:.2f} P({att_list[i]} = 1|C = 1): {prob_1[2 * i + 1]:.2f}', end=' ')
def get_class(row, prob_0, prob_1, c0, c1):
    row = list(map(int, row))
    p0 = c0
    p1 = c1
    for i in range(len(row)):
        j = i * 2
        if row[i] == 0:
            p0 *= prob_0[j]
            p1 *= prob_1[j]
        else:
            p0 *= prob_0[j + 1]
            p1 *= prob_1[j + 1]
    return '1' if p1 > p0 else '0'
def calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1):
    a_count = 0
    for i in range(len(data)):
        if get_class(data[i], prob_0, prob_1, c0, c1) == class_list[i]:
            a_count += 1
    return (a_count / len(data)) * 100
def main():
    train = input('\nPlease input name of training dataset (with file extension): ')
    test = input('\nPlease input name of test dataset (with file extension): ')
    att_list, data, class_list = load_data(train)
    cols = len(att_list)
    rows = len(data)
    c0, c1, prob_0, prob_1 = calculate_probabilities(data, class_list, cols)
    print_probabilities(c0, c1, prob_0, prob_1, att_list)
    train_accuracy = calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1)
    print(f'\n\nAccuracy on training set ({rows} instances) is: {train_accuracy:.2f}%')
    att_list, data, class_list = load_data(test)
    rows = len(data)
    test_accuracy = calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1)
    print(f'\n\nAccuracy on test set ({rows} instances) is: {test_accuracy:.2f}%')
if __name__ == "__main__":
    main()