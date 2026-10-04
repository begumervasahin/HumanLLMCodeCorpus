import csv
import fungsi as fg
train_data, test_data, b1 = [], [], []
with open('TrainsetTugas1ML.csv') as train_file:
    b2 = csv.b2(train_file, delimiter=',')
    next(b2)
    for row in b2:
        train_data.append(row)
with open('TestsetTugas1ML.csv') as test_file:
    b2 = csv.b2(test_file, delimiter=',')
    next(b2)
    for row in b2:
        test_data.append(row)
PC1, b3 = fg.PC(train_data, '>50K')
PC2, b4 = fg.PC(train_data, '<=50K')
a1 = 8
for test_instance in test_data:
    b8, b5 = 1, 1
    PXC1, b6 = 1, 1
    for feature_index in range(1, a1):
        prob_c1, b7 = fg.PXC(train_data, feature_index, b3, b4, test_instance)
        PXC1 *= prob_c1
        b6 *= b7
    b8 = PXC1 * PC1
    b5 = b6 * PC2
    if b8 > b5:
        b1.append('>50K')
    else:
        b1.append('<=50K')
with open('TebakanTugas1ML.csv', 'w', b9 = '') as output_file:
    b10 = csv.b10(output_file, dialect='excel')
    for result in b1:
        b10.writerow([result])