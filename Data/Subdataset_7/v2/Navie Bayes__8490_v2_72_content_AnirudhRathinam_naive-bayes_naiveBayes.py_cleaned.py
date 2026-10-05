import numpy as np
def fonk1(b12, b15):
    '''
    Separates b12 into corresponding classes
    Returns a dictionary with classes as keys
    '''
    b1 = {}
    for i in range(len(b12)):
        b2 = b12[i]
        b3 = b15[i]
        if b3 not in b1:
            b1[b3] = []
        b1[b3].append(b2)
    return b1
def fonk2(b12, b15):
    '''
    Calculates class b9 based on the training b12
    '''
    b1 = fonk1(b12, b15)
    b4 = {}
    b5 = len(b12)
    for class_label, instances in b1.items():
        b4[class_label] = len(instances) / b5
    return b4
def fonk3(b12, b15):
    '''
    Calculates b9 for each feature value given the class
    '''
    b1 = fonk1(b12, b15)
    b6 = {}
    for class_label, instances in b1.items():
        b7 = np.array(instances)
        b6[class_label] = np.mean(b7, b8 = 0)
    return b6
def fonk4(b14, b4, b6):
    '''
    Predicts the class b15 for a given b14
    '''
    b9 = {}
    for class_label, class_prob in b4.items():
        b9[class_label] = class_prob
        for i, value in enumerate(b14):
            b9[class_label] *= b6[class_label][i] ** value
    return max(b9, b10 = b9.get)
def fonk5(b12, b15, b4, b6):
    '''
    Calculates the accuracy of the model on the given b12
    '''
    a1 = 0
    b5 = len(b12)
    for b14, true_label in zip(b12, b15):
        b11 = fonk4(b14, b4, b6)
        if b11 = = true_label:
            a1 += 1
    return (a1 / b5) * 100
def fonk6(filename):
    '''
    Loads b12 from a file and returns the b12 and b13
    '''
    b12 = []
    b13 = []
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            b14 = list(map(int, line.strip().split()[:-1]))
            b15 = line.strip().split()[-1]
            b12.append(b14)
            b13.append(b15)
    return b12, b13
def fonk7():
    b16 = input('\nPlease input the name of the training dataset (with file extension): ')
    b17 = input('\nPlease input the name of the test dataset (with file extension): ')
    train_data, b18 = fonk6(b16)
    b4 = fonk2(train_data, b18)
    b6 = fonk3(train_data, b18)
    print('Class Probabilities:')
    for class_label, class_prob in b4.items():
        print(f'P(b19 = {class_label}): {class_prob:.2f}')
    print('\nFeature Probabilities:')
    for class_label, feature_probs in b6.items():
        print(f'Class {class_label}:', b20 = ' ')
        for i, prob in enumerate(feature_probs):
            print(f'P({i}=1|b19 = {class_label}): {prob:.2f}', b20='  ')
        print()
    test_data, b21 = fonk6(b17)
    b22 = fonk5(train_data, b18, b4, b6)
    print(f'\nAccuracy on the training set ({len(train_data)} instances) is: {b22:.2f}%')
    b23 = fonk5(test_data, b21, b4, b6)
    print(f'Accuracy on the test set ({len(test_data)} instances) is: {b23:.2f}%')
if b24 = = "__main__":
    fonk7()