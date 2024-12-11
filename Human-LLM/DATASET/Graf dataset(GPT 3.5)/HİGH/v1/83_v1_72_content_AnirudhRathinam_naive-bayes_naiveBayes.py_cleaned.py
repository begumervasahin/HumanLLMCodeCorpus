import numpy as np
def fonk1(b11, b14):
    '''
    Separates b11 into corresponding classes
    returns a dict with classes for keys
    '''
    b1 = {}
    for i in range(len(b11)):
        b2 = b11[i]
        b3 = b14[i]
        if b3 not in b1:
            b1[b3] = []
        b1[b3].append(b2)
    return b1
def fonk2(b11, b14):
    '''
    Calculates class b8 based on the training b11
    '''
    b1 = fonk1(b11, b14)
    b4 = {}
    for class_label, instances in b1.items():
        b4[class_label] = len(instances) / len(b11)
    return b4
def fonk3(b11, b14):
    '''
    Calculates b8 for each feature value given the class
    '''
    b1 = fonk1(b11, b14)
    b5 = {}
    for class_label, instances in b1.items():
        b6 = np.array(instances)
        b5[class_label] = np.mean(b6, b7 = 0)
    return b5
def fonk4(b13, b4, b5):
    '''
    Predicts the class b14 for a given b13
    '''
    b8 = {}
    for class_label, class_prob in b4.items():
        b8[class_label] = class_prob
        for i, value in enumerate(b13):
            b8[class_label] *= b5[class_label][i] ** value
    return max(b8, b9 = b8.get)
def fonk5(b11, b14, b4, b5):
    '''
    Calculates the accuracy of the model on the given b11
    '''
    a1 = 0
    for b13, true_label in zip(b11, b14):
        b10 = fonk4(b13, b4, b5)
        if b10 = = true_label:
            a1 += 1
    return a1 / len(b11) * 100
def fonk6(filename):
    '''
    Loads b11 from a file and returns the b11 and b12
    '''
    b11 = []
    b12 = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            b13 = list(map(int, line.strip().split()[:-1]))
            b14 = line.strip().split()[-1]
            b11.append(b13)
            b12.append(b14)
    return b11, b12
def fonk7():
    b15 = input('\nPlease input name of training dataset (with file extension): ')
    b16 = input('\nPlease input name of test dataset (with file extension): ')
    train_data, b17 = fonk6(b15)
    b4 = fonk2(train_data, b17)
    b5 = fonk3(train_data, b17)
    print('Class Probabilities:')
    for class_label, class_prob in b4.items():
        print(f'P(b18 = {class_label}): {class_prob:.2f}')
    print('\nFeature Probabilities:')
    for class_label, feature_probs in b5.items():
        print(f'Class {class_label}:', b19 = ' ')
        for i, prob in enumerate(feature_probs):
            print(f'P({i}=1|b18 = {class_label}): {prob:.2f}', b19='  ')
        print()
    test_data, b20 = fonk6(b16)
    b21 = fonk5(train_data, b17, b4, b5)
    print(f'\nAccuracy on training set ({len(train_data)} instances) is: {b21:.2f}%')
    b22 = fonk5(test_data, b20, b4, b5)
    print(f'Accuracy on test set ({len(test_data)} instances) is: {b22:.2f}%')
if b23 = = "__main__":
    fonk7()