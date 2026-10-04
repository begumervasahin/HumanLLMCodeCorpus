import pandas as pd
import numpy as np
training_file = "irisTraining.txt"
testing_file = "irisTesting.txt"
train_data = pd.read_csv(training_file, sep=" ", header=None)
test_data = pd.read_csv(testing_file, sep=" ", header=None)
num_columns = test_data.shape[1]
columns = list(range(num_columns - 1)) + ["label"]
train_data.columns = columns
test_data.columns = columns
yes_count = train_data[train_data['label'] == 1].shape[0]
no_count = train_data[train_data['label'] == -1].shape[0]
test_labels = test_data['label']
test_data = test_data.drop(columns=['label'])
true_positive_count = 0
true_negative_count = 0
false_positive_count = 0
false_negative_count = 0
def normal_pdf(x, mean, std):
    return (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
for i in range(test_data.shape[0]):
    test_row = test_data.iloc[i]
    yes_prob = 1
    no_prob = 1
    for attribute, value in test_row.iteritems():
        yes_data = train_data[train_data['label'] == 1][attribute]
        no_data = train_data[train_data['label'] == -1][attribute]
        yes_mean, yes_std = yes_data.mean(), yes_data.std()
        no_mean, no_std = no_data.mean(), no_data.std()
        yes_prob *= normal_pdf(value, yes_mean, yes_std)
        no_prob *= normal_pdf(value, no_mean, no_std)
    yes_prob *= yes_count
    no_prob *= no_count
    predicted_class = 1 if yes_prob > no_prob else -1
    actual_class = test_labels.iloc[i]
    if predicted_class == 1:
        if actual_class == 1:
            true_positive_count += 1
        else:
            false_positive_count += 1
    else:
        if actual_class == -1:
            true_negative_count += 1
        else:
            false_negative_count += 1
print('--- ---')
print('counts')
print(f'true_positive_count: {true_positive_count}')
print(f'true_negative_count: {true_negative_count}')
print(f'false_positive_count: {false_positive_count}')
print(f'false_negative_count: {false_negative_count}')
total_test_rows = test_data.shape[0]
accuracy = (true_positive_count + true_negative_count) / total_test_rows
sensitivity = true_positive_count / (true_positive_count + false_negative_count)
specificity = true_negative_count / (true_negative_count + false_positive_count)
precision = true_positive_count / (true_positive_count + false_positive_count)
print(f'accuracy: {accuracy:.2f}')
print(f'sensitivity / recall: {sensitivity:.2f}')
print(f'specificity: {specificity:.2f}')
print(f'precision: {precision:.2f}')