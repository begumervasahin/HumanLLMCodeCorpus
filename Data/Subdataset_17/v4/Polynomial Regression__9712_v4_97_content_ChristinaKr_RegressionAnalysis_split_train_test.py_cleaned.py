import csv
import numpy as np
def split_data(ifname, delimiter=None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    num_rows = 1599
    test_row_indices = np.unique(np.random.choice(num_rows, size=int(fraction * num_rows), replace=False))
    if delimiter is None:
        delimiter = '\t'
    with open(ifname, 'r') as ifile:
        datareader = csv.reader(ifile, delimiter=delimiter)
        field_names = next(datareader) if has_header else None
        training_data = []
        test_data = []
        for count, row in enumerate(datareader):
            if columns is not None:
                row = [row[c] for c in columns]
            if count in test_row_indices:
                test_data.append(row)
            else:
                training_data.append(row)
    print(f"There are {len(training_data)} training entries")
    print(f"There are {len(test_data)} test entries")
    print(f"Each row has {len(training_data[0])} elements")
    training_data_as_array = np.array(training_data).astype(float)
    test_data_as_array = np.array(test_data).astype(float)
    return training_data_as_array, test_data_as_array, field_names