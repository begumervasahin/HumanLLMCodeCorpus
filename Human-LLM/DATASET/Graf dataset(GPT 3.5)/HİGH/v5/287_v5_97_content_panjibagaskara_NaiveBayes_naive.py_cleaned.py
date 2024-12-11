import csv
import fungsi as fg
with open('TrainsetTugas1ML.csv') as train_file:
    b1 = csv.b1(train_file, delimiter=',')
    next(b1)
    b2 = [row for row in b1]
with open('TestsetTugas1ML.csv') as test_file:
    b1 = csv.b1(test_file, delimiter=',')
    next(b1)
    b3 = [row for row in b1]
PC1, b4 = fg.PC(b2, '>50K')
PC2, b5 = fg.PC(b2, '<=50K')
a1 = 8
b6 = []
for i in range(len(b3)):
    b10, b7 = 1, 1
    PXC1, b8 = 1, 1
    for j in range(1, a1):
        a, b9 = fg.PXC(b2, j, b4, b5, b3[i])
        PXC1 *= a
        b8 *= b9
    b10 = PXC1 * PC1
    b7 = b8 * PC2
    b6.append('>50K' if b10 > b7 else '<=50K')
with open('TebakanTugas1ML.csv', 'w', b11 = '\a1') as output_file:
    b12 = csv.b12(output_file, dialect='excel')
    b12.writerows([[b6[i]] for i in range(len(b6))])