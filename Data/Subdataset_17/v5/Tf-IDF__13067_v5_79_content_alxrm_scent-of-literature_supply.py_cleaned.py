import pandas as pd
from format import clean_str, shuffle_both
def read_train_data(file_name, x_col, y_col, separator='\t', with_cleaning=True, with_header=False, with_shuffle=True):
    header_option = None if with_header else 'infer'
    data = pd.read_csv(file_name, sep=separator, header=header_option)
    x_text = _process_lines(data[x_col].tolist(), with_cleaning)
    y_text = data[y_col].tolist()
    if with_shuffle:
        x_text, y_text = shuffle_both(x_text, y_text)
    return x_text, y_text
def read_test_data(file_name, x_col, with_cleaning=True):
    data = pd.read_csv(file_name, header=None)
    return _process_lines(data[x_col].tolist(), with_cleaning)
def _process_lines(lines, with_cleaning=True):
    if with_cleaning:
        return [clean_str(line.decode('utf-8')) for line in lines]
    else:
        return [line.decode('utf-8') for line in lines]