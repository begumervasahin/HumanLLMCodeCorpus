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
def write_predictions(filename, predictions):
    with open(filename, 'w', newline='\n') as file:
        writer = csv.writer(file, dialect='excel')
        for prediction in predictions:
            writer.writerow([prediction])
def predict_class(train_data, test_data, num_features):
    predictions = []
    PC1, nC1 = fg.PC(train_data, '>50K')
    PC2, nC2 = fg.PC(train_data, '<=50K')
    for test_instance in test_data:
        PC1X, PC2X = PC1, PC2
        PXC1, PXC2 = 1, 1
        for feature_index in range(1, num_features):
            a, b = fg.PXC(train_data, feature_index, nC1, nC2, test_instance)
            PXC1 *= a
            PXC2 *= b
        PC1X *= PXC1
        PC2X *= PXC2
        if PC1X > PC2X:
            predictions.append('>50K')
        else:
            predictions.append('<=50K')
    return predictions
def main():
    train_data = load_data('TrainsetTugas1ML.csv')
    test_data = load_data('TestsetTugas1ML.csv')
    num_features = 8
    predictions = predict_class(train_data, test_data, num_features)
    write_predictions('TebakanTugas1ML.csv', predictions)
if __name__ == "__main__":
    main()