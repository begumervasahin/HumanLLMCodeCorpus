import pandas as pd
import numpy as np
def load_data(training_file, testing_file):
    train_data = pd.read_csv(training_file, sep=" ", header=None)
    test_data = pd.read_csv(testing_file, sep=" ", header=None)
    total_test_columns = test_data.shape[1]
    columns_array = list(range(total_test_columns - 1))
    columns_array.append("label")
    train_data.columns = columns_array
    test_data.columns = columns_array
    return train_data, test_data
def calculate_class_counts(train_data):
    yes_count = train_data[train_data['label'] == 1].shape[0]
    no_count = train_data[train_data['label'] == -1].shape[0]
    return yes_count, no_count
def normal_pdf(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
def classify_record(test_row, train_data, yes_count, no_count):
    yes_prob = 1
    no_prob = 1
    for attribute, value in test_row.iteritems():
        np_array_yes = np.array(train_data[train_data['label'] == 1][attribute])
        yes_mean = np.average(np_array_yes)
        yes_standard_deviation = np.std(np_array_yes)
        np_array_no = np.array(train_data[train_data['label'] == -1][attribute])
        no_mean = np.average(np_array_no)
        no_standard_deviation = np.std(np_array_no)
        yes_prob *= normal_pdf(value, yes_mean, yes_standard_deviation)
        no_prob *= normal_pdf(value, no_mean, no_standard_deviation)
    yes_prob = yes_prob * yes_count
    no_prob = no_prob * no_count
    predicted_class = 1 if yes_prob > no_prob else -1
    return predicted_class
def evaluate_predictions(test_data, class_labels, train_data, yes_count, no_count):
    true_positive_count = 0
    true_negative_count = 0
    false_positive_count = 0
    false_negative_count = 0
    for i in range(test_data.shape[0]):
        test_row = test_data.iloc[i]
        predicted_class = classify_record(test_row, train_data, yes_count, no_count)
        actual_class = class_labels.values[i]
        if predicted_class == 1:
            if actual_class == 1:
                true_positive_count += 1
            else:
                false_positive_count += 1
        elif predicted_class == -1:
            if actual_class == -1:
                true_negative_count += 1
            else:
                false_negative_count += 1
    return true_positive_count, true_negative_count, false_positive_count, false_negative_count
def print_evaluation_metrics(true_positive_count, true_negative_count, false_positive_count, false_negative_count, total_test_rows):
    print('--- ---')
    print('Counts:')
    print('True Positive Count:', true_positive_count)
    print('True Negative Count:', true_negative_count)
    print('False Positive Count:', false_positive_count)
    print('False Negative Count:', false_negative_count)
    accuracy = (true_positive_count + true_negative_count) / total_test_rows
    print('Accuracy:', accuracy)
    sensitivity = true_positive_count / (true_positive_count + false_negative_count)
    print('Sensitivity / Recall:', sensitivity)
    specificity = true_negative_count / (false_positive_count + true_negative_count)
    print('Specificity:', specificity)
    precision = true_positive_count / (true_positive_count + false_positive_count)
    print('Precision:', precision)
if __name__ == "__main__":
    training_file = "irisTraining.txt"
    testing_file = "irisTesting.txt"
    train_data, test_data = load_data(training_file, testing_file)
    yes_count, no_count = calculate_class_counts(train_data)
    class_labels = test_data['label']
    del test_data['label']
    true_positive_count, true_negative_count, false_positive_count, false_negative_count = evaluate_predictions(test_data, class_labels, train_data, yes_count, no_count)
    print_evaluation_metrics(true_positive_count, true_negative_count, false_positive_count, false_negative_count, test_data.shape[0])