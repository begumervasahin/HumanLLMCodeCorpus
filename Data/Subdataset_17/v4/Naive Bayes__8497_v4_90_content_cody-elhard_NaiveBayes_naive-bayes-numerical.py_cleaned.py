import pandas as pd
import numpy as np
debug = False
training_file = "irisTraining.txt"
testing_file = "irisTesting.txt"
train_data = pd.read_csv(training_file, sep=" ", header=None)
test_data = pd.read_csv(testing_file, sep=" ", header=None)
columns_array = list(range(test_data.shape[1] - 1)) + ["label"]
train_data.columns = columns_array
test_data.columns = columns_array
yes_count = train_data[train_data['label'] == 1].shape[0]
no_count = train_data[train_data['label'] == -1].shape[0]
class_labels = test_data['label']
del test_data['label']
true_positive_count = 0
true_negative_count = 0
false_positive_count = 0
false_negative_count = 0
def normal_pdf(x, mean, std_dev):
    return (1 / (2 * np.pi * std_dev**2)**0.5) * np.exp(-1 * (x - mean)**2 / (2 * std_dev**2))
for i in range(test_data.shape[0]):
    test_row = test_data.iloc[i]
    yes_prob = 1
    no_prob = 1
    for attribute, value in test_row.iteritems():
        yes_data = np.array(train_data[train_data['label'] == 1][attribute])
        no_data = np.array(train_data[train_data['label'] == -1][attribute])
        yes_mean = np.mean(yes_data)
        yes_std_dev = np.std(yes_data)
        no_mean = np.mean(no_data)
        no_std_dev = np.std(no_data)
        yes_prob *= normal_pdf(value, yes_mean, yes_std_dev)
        no_prob *= normal_pdf(value, no_mean, no_std_dev)
    yes_prob *= yes_count
    no_prob *= no_count
    predicted_class = 1 if yes_prob > no_prob else -1
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
total_test_rows = test_data.shape[0]
accuracy = (true_positive_count + true_negative_count) / total_test_rows
sensitivity = true_positive_count / (true_positive_count + false_negative_count)
specificity = true_negative_count / (true_negative_count + false_positive_count)
precision = true_positive_count / (true_positive_count + false_positive_count)
print('--- Performance Metrics ---')
print(f'True Positive Count: {true_positive_count}')
print(f'True Negative Count: {true_negative_count}')
print(f'False Positive Count: {false_positive_count}')
print(f'False Negative Count: {false_negative_count}')
print(f'Accuracy: {accuracy:.2f}')
print(f'Sensitivity / Recall: {sensitivity:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Precision: {precision:.2f}')