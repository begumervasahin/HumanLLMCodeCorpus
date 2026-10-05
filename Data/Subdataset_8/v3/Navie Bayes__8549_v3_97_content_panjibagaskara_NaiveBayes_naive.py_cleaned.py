import csv
import fungsi as fg
def load_data(filename):
    data = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            data.append(row)
    return data
train_data = load_data('TrainsetTugas1ML.csv')
test_data = load_data('TestsetTugas1ML.csv')
def calculate_PC(data, target_class):
    PC, nC = fg.PC(data, target_class)
    return PC, nC
PC1, nC1 = calculate_PC(train_data, '>50K')
PC2, nC2 = calculate_PC(train_data, '<=50K')
def classify(test_data, n, PC1, PC2, nC1, nC2):
    hasil = []
    for i in range(len(test_data)):
        PC1X, PC2X = 1, 1
        PXC1, PXC2 = 1, 1
        for j in range(1, n):
            a, b = fg.PXC(train_data, j, nC1, nC2, test_data[i])
            PXC1 *= a
            PXC2 *= b
        PC1X = PXC1 * PC1
        PC2X = PXC2 * PC2
        hasil.append('>50K' if PC1X > PC2X else '<=50K')
    return hasil
hasil = classify(test_data, 8, PC1, PC2, nC1, nC2)
def write_results(filename, hasil):
    with open(filename, 'w', newline='\n') as output_file:
        writer = csv.writer(output_file, dialect='excel')
        for h in hasil:
            writer.writerow([h])
write_results('TebakanTugas1ML.csv', hasil)