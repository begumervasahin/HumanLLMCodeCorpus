import csv
import fungsi as fg
def fonk1(filename):
    b1 = []
    with open(filename) as file:
        b2 = csv.b2(file, delimiter=',')
        next(b2)
        for row in b2:
            b1.append(row)
    return b1
def fonk2(filename, b5):
    with open(filename, 'w', b3 = '\n') as file:
        b4 = csv.b4(file, dialect='excel')
        for prediction in b5:
            b4.writerow([prediction])
def fonk3(b11, b12, a1):
    b5 = []
    PC1, b6 = fg.PC(b11, '>50K')
    PC2, b7 = fg.PC(b11, '<=50K')
    for test_instance in b12:
        PC1X, b8 = PC1, PC2
        PXC1, b9 = 1, 1
        for feature_index in range(1, a1):
            a, b10 = fg.PXC(b11, feature_index, b6, b7, test_instance)
            PXC1 *= a
            b9 *= b10
        PC1X *= PXC1
        b8 *= b9
        if PC1X > b8:
            b5.append('>50K')
        else:
            b5.append('<=50K')
    return b5
def fonk4():
    b11 = fonk1('TrainsetTugas1ML.csv')
    b12 = fonk1('TestsetTugas1ML.csv')
    a1 = 8
    b5 = fonk3(b11, b12, a1)
    fonk2('TebakanTugas1ML.csv', b5)
if b13 = = "__main__":
    fonk4()