import csv
import fungsi as fg
C1, C2, train, test, hasil = [], [], [], [], []
with open('TrainsetTugas1ML.csv') as train_file:
    reader = csv.reader(train_file, delimiter=',')
    next(reader)
    for row in reader:
        train.append(row)
with open('TestsetTugas1ML.csv') as test_file:
    reader = csv.reader(test_file, delimiter=',')
    next(reader)
    for row in reader:
        test.append(row)
PC1, nC1 = fg.PC(train, '>50K')
PC2, nC2 = fg.PC(train, '<=50K')
n = 8
akurasi = 0
for i in range(len(test)):
    PC1X, PC2X = 1, 1
    PXC1, PXC2 = 1, 1
    for j in range(1, n):
        a, b = fg.PXC(train, j, nC1, nC2, test[i])
        PXC1 *= a
        PXC2 *= b
    PC1X = PXC1 * PC1
    PC2X = PXC2 * PC2
    hasil.append('>50K' if PC1X > PC2X else '<=50K')
with open('TebakanTugas1ML.csv', 'w', newline='\n') as output_file:
    writer = csv.writer(output_file, dialect='excel')
    for h in hasil:
        writer.writerow([h])