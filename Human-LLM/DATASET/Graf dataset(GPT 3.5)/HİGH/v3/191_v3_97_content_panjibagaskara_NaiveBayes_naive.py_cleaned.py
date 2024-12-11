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
b3 = fonk1('TrainsetTugas1ML.csv')
b4 = fonk1('TestsetTugas1ML.csv')
def fonk2(b1, target_class):
    PC, b5 = fg.PC(b1, target_class)
    return PC, b5
PC1, b6 = fonk2(b3, '>50K')
PC2, b7 = fonk2(b3, '<=50K')
def fonk3(b4, n, PC1, PC2, b6, b7):
    b8 = []
    for i in range(len(b4)):
        b12, b9 = 1, 1
        PXC1, b10 = 1, 1
        for j in range(1, n):
            a, b11 = fg.PXC(b3, j, b6, b7, b4[i])
            PXC1 *= a
            b10 *= b11
        b12 = PXC1 * PC1
        b9 = b10 * PC2
        b8.append('>50K' if b12 > b9 else '<=50K')
    return b8
b8 = fonk3(b4, 8, PC1, PC2, b6, b7)
def fonk4(filename, b8):
    with open(filename, 'w', b13 = '\n') as output_file:
        b14 = csv.b14(output_file, dialect='excel')
        for h in b8:
            b14.writerow([h])
fonk4('TebakanTugas1ML.csv', b8)