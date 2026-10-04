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
num_features = 8
akurasi = 0
for test_instance in test:
    PC1X, PC2X = PC1, PC2
    PXC1, PXC2 = 1, 1
    for feature_index in range(1, num_features):
        a, b = fg.PXC(train, feature_index, nC1, nC2, test_instance)
        PXC1 *= a
        PXC2 *= b
    PC1X *= PXC1
    PC2X *= PXC2
    if PC1X > PC2X:
        hasil.append('>50K')
    else:
        hasil.append('<=50K')
with open('TebakanTugas1ML.csv', 'w', newline='\n') as output_file:
    writer = csv.writer(output_file, dialect='excel')
    for result in hasil:
        writer.writerow([result])