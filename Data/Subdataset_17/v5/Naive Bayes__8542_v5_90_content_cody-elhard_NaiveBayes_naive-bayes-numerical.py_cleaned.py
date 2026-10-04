import pandas as pd
import numpy as np
DEBUG = False
TRAINING_FILE = "irisTraining.txt"
TESTING_FILE = "irisTesting.txt"
def load_data(file_path):
    data = pd.read_csv(file_path, sep=" ", header=None)
    return data
def set_column_names(data):
    columns = list(range(data.shape[1] - 1)) + ["label"]
    data.columns = columns
    return data
def normal_pdf(x, mean, std_dev):
    exponent = np.exp(-((x - mean) ** 2 / (2 * std_dev ** 2)))
    return (1 / (np.sqrt(2 * np.pi) * std_dev)) * exponent
def classify_record(test_row, train_data, yes_count, no_count):
    yes_prob = 1
    no_prob = 1
    for attribute, value in test_row.iteritems():
        yes_data = train_data[train_data['label'] == 1][attribute]
        no_data = train_data[train_data['label'] == -1][attribute]
        yes_mean = yes_data.mean()
        yes_std_dev = yes_data.std()
        no_mean = no_data.mean()
        no_std_dev = no_data.std()
        yes_prob *= normal_pdf(value, yes_mean, yes_std_dev)
        no_prob *= normal_pdf(value, no_mean, no_std_dev)
    yes_prob *= yes_count
    no_prob *= no_count
    return 1 if yes_prob > no_prob else -1
def evaluate_model(test_data, class_labels, train_data, yes_count, no_count):
    metrics = {
        'true_positive': 0,
        'true_negative': 0,
        'false_positive': 0,
        'false_negative': 0
    }
    for i in range(test_data.shape[0]):
        test_row = test_data.iloc[i]
        predicted_class = classify_record(test_row, train_data, yes_count, no_count)
        actual_class = class_labels.values[i]
        if predicted_class == 1:
            if actual_class == 1:
                metrics['true_positive'] += 1
            else:
                metrics['false_positive'] += 1
        else:
            if actual_class == -1:
                metrics['true_negative'] += 1
            else:
                metrics['false_negative'] += 1
    return metrics
def calculate_performance_metrics(metrics, total_count):
    tp = metrics['true_positive']
    tn = metrics['true_negative']
    fp = metrics['false_positive']
    fn = metrics['false_negative']
    accuracy = (tp + tn) / total_count
    sensitivity = tp / (tp + fn)
    specificity = tn / (tn + fp)
    precision = tp / (tp + fp)
    return {
        'accuracy': accuracy,
        'sensitivity': sensitivity,
        'specificity': specificity,
        'precision': precision
    }
def print_metrics(metrics):
    print('--- Performance Metrics ---')
    print(f"True Positive Count: {metrics['true_positive']}")
    print(f"True Negative Count: {metrics['true_negative']}")
    print(f"False Positive Count: {metrics['false_positive']}")
    print(f"False Negative Count: {metrics['false_negative']}")
    print(f"Accuracy: {metrics['accuracy']:.2f}")
    print(f"Sensitivity / Recall: {metrics['sensitivity']:.2f}")
    print(f"Specificity: {metrics['specificity']:.2f}")
    print(f"Precision: {metrics['precision']:.2f}")
def main():
    train_data = load_data(TRAINING_FILE)
    test_data = load_data(TESTING_FILE)
    train_data = set_column_names(train_data)
    test_data = set_column_names(test_data)
    yes_count = train_data[train_data['label'] == 1].shape[0]
    no_count = train_data[train_data['label'] == -1].shape[0]
    class_labels = test_data['label']
    test_data = test_data.drop(columns=['label'])
    metrics = evaluate_model(test_data, class_labels, train_data, yes_count, no_count)
    total_test_rows = test_data.shape[0]
    performance_metrics = calculate_performance_metrics(metrics, total_test_rows)
    print_metrics({**metrics, **performance_metrics})
if __name__ == "__main__":
    main()