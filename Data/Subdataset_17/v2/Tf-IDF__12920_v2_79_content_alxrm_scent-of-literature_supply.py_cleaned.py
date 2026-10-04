import pandas as pd
from format import clean_str, shuffle_both
def read_train_data(file_name, x_col, y_col, separator='\t', with_cleaning=True, with_header=False, with_shuffle=True):
    header = 0 if with_header else None
    data = pd.read_csv(file_name, sep=separator, header=header)
    x_text = _process_text_lines(data[x_col].tolist(), with_cleaning)
    y_text = data[y_col].tolist()
    if with_shuffle:
        return shuffle_both(x_text, y_text)
    else:
        return x_text, y_text
def read_test_data(file_name, x_col, with_cleaning=True):
    data = pd.read_csv(file_name, header=None, skiprows=[0])
    x_text = data[x_col].tolist()
    return _process_text_lines(x_text, with_cleaning)
def _process_text_lines(lines, with_cleaning=True):
    if with_cleaning:
        return [clean_str(sentence) for sentence in lines]
    else:
        return lines
