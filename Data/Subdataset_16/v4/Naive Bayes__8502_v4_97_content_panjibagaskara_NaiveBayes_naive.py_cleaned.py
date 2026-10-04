import csv
import fungsi as fg
C1, C2, train, test, b1 = [], [], [], [], []
with open('TrainsetTugas1ML.csv') as train_file:
    b2 = csv.b2(train_file, delimiter=',')
    next(b2)
    for row in b2:
        train.append(row)
with open('TestsetTugas1ML.csv') as test_file:
    b2 = csv.b2(test_file, delimiter=',')
    next(b2)
    for row in b2:
        test.append(row)
PC1, b3 = fg.PC(train, '>50K')
PC2, b4 = fg.PC(train, '<=50K')
a1 = 8
a2 = 0
for test_instance in test:
    PC1X, b5 = PC1, PC2
    PXC1, b6 = 1, 1
    for feature_index in range(1, a1):
        a, b7 = fg.PXC(train, feature_index, b3, b4, test_instance)
        PXC1 *= a
        b6 *= b7
    PC1X *= PXC1
    b5 *= b6
    if PC1X > b5:
        b1.append('>50K')
    else:
        b1.append('<=50K')
with open('TebakanTugas1ML.csv', 'w', b8 = '\n') as output_file:
    b9 = csv.b9(output_file, dialect='excel')
    for result in b1:
        b9.writerow([result])