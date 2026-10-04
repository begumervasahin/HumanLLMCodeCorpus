import csv
import fungsi as fg
train_data, test_data, predictions = [], [], []
with open('TrainsetTugas1ML.csv') as train_file:
    reader = csv.reader(train_file, delimiter=',')
    next(reader)
    for row in reader:
        train_data.append(row)
with open('TestsetTugas1ML.csv') as test_file:
    reader = csv.reader(test_file, delimiter=',')
    next(reader)
    for row in reader:
        test_data.append(row)
PC1, nC1 = fg.PC(train_data, '>50K')
PC2, nC2 = fg.PC(train_data, '<=50K')
num_features = 8
for test_instance in test_data:
    PC1X, PC2X = 1, 1
    PXC1, PXC2 = 1, 1
    for feature_index in range(1, num_features):
        prob_c1, prob_c2 = fg.PXC(train_data, feature_index, nC1, nC2, test_instance)
        PXC1 *= prob_c1
        PXC2 *= prob_c2
    PC1X = PXC1 * PC1
    PC2X = PXC2 * PC2
    if PC1X > PC2X:
        predictions.append('>50K')
    else:
        predictions.append('<=50K')
with open('TebakanTugas1ML.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file, dialect='excel')
    for result in predictions:
        writer.writerow([result])