import csv
import fungsi as fg
def load_data(file_path):
    data = []
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            data.append(row)
    return data
def calculate_class_probabilities(train_data):
    PC1, nC1 = fg.PC(train_data, '>50K')
    PC2, nC2 = fg.PC(train_data, '<=50K')
    return PC1, nC1, PC2, nC2
def predict(test_data, train_data, PC1, nC1, PC2, nC2, num_features):
    predictions = []
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
    return predictions
def write_predictions(predictions, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        for result in predictions:
            writer.writerow([result])
def main():
    train_data = load_data('TrainsetTugas1ML.csv')
    test_data = load_data('TestsetTugas1ML.csv')
    PC1, nC1, PC2, nC2 = calculate_class_probabilities(train_data)
    num_features = 8
    predictions = predict(test_data, train_data, PC1, nC1, PC2, nC2, num_features)
    write_predictions(predictions, 'TebakanTugas1ML.csv')
if __name__ == "__main__":
    main()