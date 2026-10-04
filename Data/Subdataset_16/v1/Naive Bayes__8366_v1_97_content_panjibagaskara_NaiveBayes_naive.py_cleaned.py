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
for i in range(len(test)):
    b8, b5 = 1, 1
    PXC1, b6 = 1, 1
    for j in range(1, a1):
        a, b7 = fg.PXC(train, j, b3, b4, test[i])
        PXC1 *= a
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