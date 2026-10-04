import pandas as pd
from format import clean_str, shuffle_both
def fonk1(file_name, x_col, y_col, b1 = '\t', b6=True, with_header=False, with_shuffle=True):
    b2 = None if with_header else 'infer'
    b3 = pd.read_csv(file_name, sep=b1, header=b2)
    b4 = fonk3(b3[x_col].tolist(), b6)
    b5 = b3[y_col].tolist()
    if with_shuffle:
        b4, b5 = shuffle_both(b4, b5)
    return b4, b5
def fonk2(file_name, x_col, b6 = True):
    b3 = pd.read_csv(file_name, header=None)
    return fonk3(b3[x_col].tolist(), b6)
def fonk3(lines, b6 = True):
    if b6:
        return [clean_str(line.decode('utf-8')) for line in lines]
    else:
        return [line.decode('utf-8') for line in lines]