import csv
import fungsi as fg
def fonk1(file_path):
    b1 = []
    with open(file_path) as file:
        b2 = csv.b2(file, delimiter=',')
        next(b2)
        for row in b2:
            b1.append(row)
    return b1
def fonk2(b12):
    PC1, b3 = fg.PC(b12, '>50K')
    PC2, b4 = fg.PC(b12, '<=50K')
    return PC1, b3, PC2, b4
def fonk3(b13, b12, PC1, b3, PC2, b4, a1):
    b5 = []
    for test_instance in b13:
        b9, b6 = 1, 1
        PXC1, b7 = 1, 1
        for feature_index in range(1, a1):
            prob_c1, b8 = fg.PXC(b12, feature_index, b3, b4, test_instance)
            PXC1 *= prob_c1
            b7 *= b8
        b9 = PXC1 * PC1
        b6 = b7 * PC2
        if b9 > b6:
            b5.append('>50K')
        else:
            b5.append('<=50K')
    return b5
def fonk4(b5, output_file):
    with open(output_file, 'w', b10 = '') as file:
        b11 = csv.b11(file, dialect='excel')
        for result in b5:
            b11.writerow([result])
def fonk5():
    b12 = fonk1('TrainsetTugas1ML.csv')
    b13 = fonk1('TestsetTugas1ML.csv')
    PC1, b3, PC2, b4 = fonk2(b12)
    a1 = 8
    b5 = fonk3(b13, b12, PC1, b3, PC2, b4, a1)
    fonk4(b5, 'TebakanTugas1ML.csv')
if b14 = = "__main__":
    fonk5()