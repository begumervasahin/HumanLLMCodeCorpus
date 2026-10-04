import numpy as np
def load_data(filename):
    att_list = []
    data = []
    class_list = []
    with open(filename, 'r') as file:
        attributes = file.readline().strip().split()
        att_list = attributes[:-1]
        for line in file:
            parts = line.split()
            data.append(parts[:-1])
            class_list.append(parts[-1])
    return att_list, data, class_list
def calculate_probabilities(data, class_list, num_attributes):
    prob_0 = []
    prob_1 = []
    class_0_prob = class_list.count('0') / len(class_list)
    class_1_prob = class_list.count('1') / len(class_list)
    for i in range(num_attributes):
        count_c0_t0 = count_c0_t1 = count_c1_t0 = count_c1_t1 = 0
        count_t0 = count_t1 = 0
        for j in range(len(data)):
            if data[j][i] == '0':
                count_t0 += 1
                if class_list[j] == '0':
                    count_c0_t0 += 1
                else:
                    count_c0_t1 += 1
            else:
                count_t1 += 1
                if class_list[j] == '1':
                    count_c1_t1 += 1
                else:
                    count_c1_t0 += 1
        prob_0.extend([count_c0_t0 / count_t0, count_c0_t1 / count_t0])
        prob_1.extend([count_c1_t0 / count_t1, count_c1_t1 / count_t1])
    return class_0_prob, class_1_prob, prob_0, prob_1
def print_probabilities(class_0_prob, class_1_prob, prob_0, prob_1, att_list):
    print(f'P(C = 0): {class_0_prob:.2f}')
    for i, att in enumerate(att_list):
        print(f'P({att} = 0|C = 0): {prob_0[2 * i]:.2f} P({att} = 1|C = 0): {prob_0[2 * i + 1]:.2f}', end=' ')
    print('\n')
    print(f'P(C = 1): {class_1_prob:.2f}')
    for i, att in enumerate(att_list):
        print(f'P({att} = 0|C = 1): {prob_1[2 * i]:.2f} P({att} = 1|C = 1): {prob_1[2 * i + 1]:.2f}', end=' ')
def predict_class(row, prob_0, prob_1, class_0_prob, class_1_prob):
    p0 = class_0_prob
    p1 = class_1_prob
    for i in range(len(row)):
        if row[i] == '0':
            p0 *= prob_0[2 * i]
            p1 *= prob_1[2 * i]
        else:
            p0 *= prob_0[2 * i + 1]
            p1 *= prob_1[2 * i + 1]
    return '1' if p1 > p0 else '0'
def calculate_accuracy(data, class_list, prob_0, prob_1, class_0_prob, class_1_prob):
    correct_predictions = sum(predict_class(data[i], prob_0, prob_1, class_0_prob, class_1_prob) == class_list[i]
                              for i in range(len(data)))
    return (correct_predictions / len(data)) * 100
def main():
    train_file = input('Please input the name of the training dataset (with file extension): ')
    test_file = input('Please input the name of the test dataset (with file extension): ')
    att_list, train_data, train_classes = load_data(train_file)
    num_attributes = len(att_list)
    class_0_prob, class_1_prob, prob_0, prob_1 = calculate_probabilities(train_data, train_classes, num_attributes)
    print_probabilities(class_0_prob, class_1_prob, prob_0, prob_1, att_list)
    train_accuracy = calculate_accuracy(train_data, train_classes, prob_0, prob_1, class_0_prob, class_1_prob)
    print(f'\n\nAccuracy on training set ({len(train_data)} instances): {train_accuracy:.2f}%')
    att_list, test_data, test_classes = load_data(test_file)
    test_accuracy = calculate_accuracy(test_data, test_classes, prob_0, prob_1, class_0_prob, class_1_prob)
    print(f'\n\nAccuracy on test set ({len(test_data)} instances): {test_accuracy:.2f}%')
if __name__ == "__main__":
    main()