import pandas
import numpy
debug = False
trainingFile = "irisTraining.txt"
train_data = pandas.read_csv(trainingFile, sep=" ", header=None)
testingFile = "irisTesting.txt"
test_data = pandas.read_csv(testingFile, sep=" ", header=None)
columns_array = []
total_test_columns = test_data.shape[1]
for i in range(total_test_columns - 1):
  columns_array.append(i)
columns_array.append("label")
train_data.columns = columns_array
test_data.columns = columns_array
total_training_rows = train_data.shape[0]
total_test_rows = test_data.shape[0]
yes_count = train_data[train_data['label'] == 1].shape[0]
no_count = train_data[train_data['label'] == -1].shape[0]
class_labels = test_data['label']
del test_data['label']
true_positive_count = 0
true_negative_count = 0
false_positive_count = 0
false_negative_count = 0
def normal_pdf(x, m, s):
  return (1/(2 * numpy.pi * s**2)**0.5) * numpy.exp(-1 * (x-m)**2 / (2 * s**2))
test_records = test_data.shape[0]
for i in range(test_records):
  test_row = test_data.iloc[i]
  yes_prob = 1
  no_prob = 1
  for attribute, value in test_row.iteritems():
    numpy_array_yes = numpy.array(train_data[train_data['label'] == 1][attribute])
    yes_mean = numpy.average(numpy_array_yes)
    yes_standard_deviation = numpy.std(numpy_array_yes)
    numpy_array_no = numpy.array(train_data[train_data['label'] == -1][attribute])
    no_mean = numpy.average(numpy_array_no)
    no_standard_deviation = numpy.std(numpy_array_no)
    yes_prob *= normal_pdf(value, yes_mean, yes_standard_deviation)
    no_prob *= normal_pdf(value, no_mean, no_standard_deviation)
  yes_prob = yes_prob * yes_count
  no_prob = no_prob * no_count
  predicted_class = 1 if yes_prob > no_prob else -1
  actual_class = class_labels.values[i]
  if (predicted_class == 1):
    if (actual_class == 1):
      true_positive_count += 1
    else:
      false_positive_count += 1
  elif predicted_class == -1:
    if (actual_class == -1):
      true_negative_count += 1
    else:
      false_negative_count += 1
print('--- ---')
print('counts')
print('true_positive_count')
print(true_positive_count)
print('true_negative_count')
print(true_negative_count)
print('false_positive_count')
print(false_positive_count)
print('false_negative_count')
print(false_negative_count)
accuracy = (true_positive_count + true_negative_count) / total_test_rows
print('accuracy: ', accuracy)
sensitivity = true_positive_count / (true_positive_count + false_negative_count)
print('sensitivity / recall: ', sensitivity)
specificity = true_negative_count / (false_positive_count + true_negative_count)
print('specificity: ', specificity)
precision = true_positive_count / (true_positive_count + false_positive_count)
print('precision: ', precision)