import numpy as np
def load_data(filename):
    attributes, data, class_list = [], [], []
    rows = 0
    with open(filename, 'r') as file:
        attributes = file.readline().split()[:-1]
        cols = len(attributes)
        for line in file:
            rows += 1
            class_list.append(line.split()[cols])
            data.append(line.split())
    return attributes, data, class_list, cols, rows
def calculate_probabilities(data, class_list, cols, rows):
    c0 = class_list.count('0') / len(class_list)
    c1 = class_list.count('1') / len(class_list)
    prob_0, prob_1 = [], []
    for i in range(cols):
        tmp_list = [row[i] for row in data]
        c_0_t_0_count = c_0_t_1_count = c_1_t_0_count = c_1_t_1_count = t_0_count = t_1_count = 0
        for j in range(rows):
            if tmp_list[j] == '0':
                t_0_count += 1
                if class_list[j] == '0':
                    c_0_t_0_count += 1
                else:
                    c_0_t_1_count += 1
            elif tmp_list[j] == '1':
                t_1_count += 1
                if class_list[j] == '1':
                    c_1_t_1_count += 1
                else:
                    c_1_t_0_count += 1
        prob_0.append(c_0_t_0_count / t_0_count)
        prob_0.append(c_0_t_1_count / t_0_count)
        prob_1.append(c_1_t_0_count / t_1_count)
        prob_1.append(c_1_t_1_count / t_1_count)
    return prob_0, prob_1, c0, c1
def print_probabilities(prob_0, prob_1, c0, c1, att_list, cols):
    print(f'P(C = 0): {c0}')
    for i in range(cols):
        print(f'P({att_list[i]} = 0 | C = 0): {prob_0[i*2]:.2f}  P({att_list[i]} = 1 | C = 0): {prob_0[i*2+1]:.2f}', end=' ')
    print('\n\n')
    print(f'P(C = 1): {c1}')
    for i in range(cols):
        print(f'P({att_list[i]} = 0 | C = 1): {prob_1[i*2]:.2f}  P({att_list[i]} = 1 | C = 1): {prob_1[i*2+1]:.2f}', end=' ')
    print('\n\n')
def get_class(row, prob_0, prob_1, c0, c1):
    p0, p1 = c0, c1
    for i in range(len(row) - 1):
        if row[i] == '0':
            p0 *= prob_0[i * 2]
            p1 *= prob_1[i * 2]
        else:
            p0 *= prob_0[i * 2 + 1]
            p1 *= prob_1[i * 2 + 1]
    return '1' if p1 > p0 else '0'
def calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1, rows):
    correct_count = 0
    for i in range(rows):
        predicted_class = get_class(data[i], prob_0, prob_1, c0, c1)
        if predicted_class == class_list[i]:
            correct_count += 1
    return (correct_count / rows) * 100
def main():
    train_file = input('\nPlease input name of training dataset (with file extension): ')
    test_file = input('\nPlease input name of test dataset (with file extension): ')
    att_list, data, class_list, cols, rows = load_data(train_file)
    prob_0, prob_1, c0, c1 = calculate_probabilities(data, class_list, cols, rows)
    print_probabilities(prob_0, prob_1, c0, c1, att_list, cols)
    train_accuracy = calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1, rows)
    print(f'\n\nAccuracy on training set ({rows} instances) is: {train_accuracy:.2f}%')
    att_list, data, class_list, cols, rows = load_data(test_file)
    test_accuracy = calculate_accuracy(data, class_list, prob_0, prob_1, c0, c1, rows)
    print(f'\n\nAccuracy on test set ({rows} instances) is: {test_accuracy:.2f}%')
if __name__ == '__main__':
    main()