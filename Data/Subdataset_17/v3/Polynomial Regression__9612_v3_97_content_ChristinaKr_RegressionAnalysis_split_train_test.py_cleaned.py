import csv
import numpy as np
def split_data(ifname, delimiter=None, has_header=False, columns=None, seed=42, fraction=0.15):
    np.random.seed(seed)
    with open(ifname, 'r') as ifile:
        datareader = csv.reader(ifile, delimiter=delimiter if delimiter else '\t')
        field_names = next(datareader) if has_header else None
        data = list(datareader)
    if columns is not None:
        data = [[row[c] for c in columns] for row in data]
    data = np.array(data).astype(float)
    num_rows = data.shape[0]
    indices = np.arange(num_rows)
    np.random.shuffle(indices)
    test_size = int(fraction * num_rows)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    test_data = data[test_indices]
    training_data = data[train_indices]
    print(f"There are {len(training_data)} training entries")
    print(f"There are {len(test_data)} test entries")
    print(f"Each row has {len(training_data[0])} elements")
    return training_data, test_data, field_names
