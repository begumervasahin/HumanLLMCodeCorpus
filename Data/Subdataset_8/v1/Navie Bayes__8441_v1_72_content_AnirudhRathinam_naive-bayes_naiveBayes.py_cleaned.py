import numpy as np
def separate_classes(data, label):
    '''
    Separates data into corresponding classes
    returns a dict with classes for keys
    '''
    separated = {}
    for i in range(len(data)):
        x = data[i]
        y = label[i]
        if y not in separated:
            separated[y] = []
        separated[y].append(x)
    return separated
def calculate_class_probabilities(data, label):
    '''
    Calculates class probabilities based on the training data
    '''
    separated = separate_classes(data, label)
    class_probabilities = {}
    for class_label, instances in separated.items():
        class_probabilities[class_label] = len(instances) / len(data)
    return class_probabilities
def calculate_feature_probabilities(data, label):
    '''
    Calculates probabilities for each feature value given the class
    '''
    separated = separate_classes(data, label)
    feature_probabilities = {}
    for class_label, instances in separated.items():
        class_data = np.array(instances)
        feature_probabilities[class_label] = np.mean(class_data, axis=0)
    return feature_probabilities
def predict(instance, class_probabilities, feature_probabilities):
    '''
    Predicts the class label for a given instance
    '''
    probabilities = {}
    for class_label, class_prob in class_probabilities.items():
        probabilities[class_label] = class_prob
        for i, value in enumerate(instance):
            probabilities[class_label] *= feature_probabilities[class_label][i] ** value
    return max(probabilities, key=probabilities.get)
def calculate_accuracy(data, label, class_probabilities, feature_probabilities):
    '''
    Calculates the accuracy of the model on the given data
    '''
    correct_count = 0
    for instance, true_label in zip(data, label):
        predicted_label = predict(instance, class_probabilities, feature_probabilities)
        if predicted_label == true_label:
            correct_count += 1
    return correct_count / len(data) * 100
def load_data(filename):
    '''
    Loads data from a file and returns the data and labels
    '''
    data = []
    labels = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            instance = list(map(int, line.strip().split()[:-1]))
            label = line.strip().split()[-1]
            data.append(instance)
            labels.append(label)
    return data, labels
def main():
    train_filename = input('\nPlease input name of training dataset (with file extension): ')
    test_filename = input('\nPlease input name of test dataset (with file extension): ')
    train_data, train_labels = load_data(train_filename)
    class_probabilities = calculate_class_probabilities(train_data, train_labels)
    feature_probabilities = calculate_feature_probabilities(train_data, train_labels)
    print('Class Probabilities:')
    for class_label, class_prob in class_probabilities.items():
        print(f'P(C={class_label}): {class_prob:.2f}')
    print('\nFeature Probabilities:')
    for class_label, feature_probs in feature_probabilities.items():
        print(f'Class {class_label}:', end=' ')
        for i, prob in enumerate(feature_probs):
            print(f'P({i}=1|C={class_label}): {prob:.2f}', end='  ')
        print()
    test_data, test_labels = load_data(test_filename)
    train_accuracy = calculate_accuracy(train_data, train_labels, class_probabilities, feature_probabilities)
    print(f'\nAccuracy on training set ({len(train_data)} instances) is: {train_accuracy:.2f}%')
    test_accuracy = calculate_accuracy(test_data, test_labels, class_probabilities, feature_probabilities)
    print(f'Accuracy on test set ({len(test_data)} instances) is: {test_accuracy:.2f}%')
if __name__ == "__main__":
    main()