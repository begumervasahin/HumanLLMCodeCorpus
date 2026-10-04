import csv
import numpy as np
def split_data(ifname, delimiter=None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    test_rows = np.unique(np.array(np.random.uniform(size = int(fraction*1599))*1599).astype(int))
    print(test_rows)
    if delimiter is None:
        delimiter = '\t'
    with open(ifname, 'r') as ifile:
        datareader = csv.reader(ifile, delimiter=delimiter)
        if has_header:
            field_names = next(datareader)
        training_data = []
        test_data = []
        count = 0
        for row in datareader:
            if not columns is None:
                row = [row[c] for c in columns]
            if(count in test_rows):
                test_data.append(row)
            else:
                training_data.append(row)
            count+=1
    print("There are %d training entries" % len(training_data))
    print("There are %d test entries" % len(test_data))
    print("Each row has %d elements" % len(training_data[0]))
    training_data_as_array = np.array(training_data).astype(float)
    test_data_as_array = np.array(test_data).astype(float)
    return training_data_as_array, test_data_as_array, field_names