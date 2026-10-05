def read_dataset(file_name):
    att_list = []
    data = []
    class_list = []
    with open(file_name, 'r') as file:
        attributes = file.readline().split()[:-1]
        att_list = attributes
        for line in file:
            row = line.split()
            class_list.append(row[-1])
            data.append(row[:-1])
    return att_list, data, class_list
def calculate_probabilities(data, class_labels, attribute_names):
    num_instances = len(data)
    num_attributes = len(attribute_names)
    prob_0 = []
    prob_1 = []
    for i in range(num_attributes):
        col_values = [int(row[i]) for row in data]
        c_0_t_0_count = col_values.count(0)
        c_0_t_1_count = num_instances - c_0_t_0_count
        c_1_t_0_count = c_0_t_0_count
        c_1_t_1_count = c_0_t_1_count
        prob_0.append(c_0_t_0_count / num_instances)
        prob_0.append(c_0_t_1_count / num_instances)
        prob_1.append(c_1_t_0_count / num_instances)
        prob_1.append(c_1_t_1_count / num_instances)
    return prob_0, prob_1
def calculate_accuracy(data, class_labels, prob_0, prob_1, c0, c1):
    num_correct = 0
    for instance, true_label in zip(data, class_labels):
        predicted_label = classify_instance(instance, prob_0, prob_1, c0, c1)
        if predicted_label == true_label:
            num_correct += 1
    return num_correct / len(data) * 100
def classify_instance(instance, prob_0, prob_1, c0, c1):
    p0 = c0
    p1 = c1
    for attr_value, prob_0_attr, prob_1_attr in zip(instance, prob_0, prob_1):
        if attr_value == '0':
            p0 *= prob_0_attr
            p1 *= prob_1_attr
        else:
            p0 *= (1 - prob_0_attr)
            p1 *= (1 - prob_1_attr)
    return '1' if p1 > p0 else '0'
train_file = input('\nPlease input the name of the training dataset (with file extension): ')
test_file = input('\nPlease input the name of the test dataset (with file extension): ')
att_list_train, data_train, class_list_train = read_dataset(train_file)
att_list_test, data_test, class_list_test = read_dataset(test_file)
prob_0_train, prob_1_train = calculate_probabilities(data_train, class_list_train, att_list_train)
c0_train = class_list_train.count('0') / len(class_list_train)
c1_train = class_list_train.count('1') / len(class_list_train)
print('Class probabilities:')
print('P(C = 0):', c0_train)
print('P(C = 1):', c1_train)
print('\nConditional probabilities:')
for i, att_name in enumerate(att_list_train):
    print('P({} = 0|C = 0): {:.2f}'.format(att_name, prob_0_train[2 * i]), end=' ')
    print('P({} = 1|C = 0): {:.2f}'.format(att_name, prob_0_train[2 * i + 1]), end=' ')
    print('P({} = 0|C = 1): {:.2f}'.format(att_name, prob_1_train[2 * i]), end=' ')
    print('P({} = 1|C = 1): {:.2f}'.format(att_name, prob_1_train[2 * i + 1]))
accuracy_train = calculate_accuracy(data_train, class_list_train, prob_0_train, prob_1_train, c0_train, c1_train)
print('\nAccuracy on the training set is: {:.2f}%'.format(accuracy_train))
accuracy_test = calculate_accuracy(data_test, class_list_test, prob_0_train, prob_1_train, c0_train, c1_train)
print('Accuracy on the test set is: {:.2f}%'.format(accuracy_test))