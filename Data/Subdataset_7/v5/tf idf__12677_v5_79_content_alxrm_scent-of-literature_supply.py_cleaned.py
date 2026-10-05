import pandas as pd
from format import clean_str, shuffle_both
def fonk1(file_name, x_col, y_col, b1 = '\t', b5=True, with_header=False, with_shuffle=True):
    b2 = pd.read_csv(file_name, sep=b1, header=None if not with_header else 'infer', skiprows=0 if with_header else 1)
    b3 = fonk3(b2[x_col].tolist(), b5)
    b4 = b2[y_col].tolist()
    if with_shuffle:
        return shuffle_both(b3, b4)
    else:
        return b3, b4
def fonk2(file_name, x_col, b5 = True):
    b2 = pd.read_csv(file_name, header=None, skiprows=1)
    b3 = fonk3(b2[x_col], b5)
    return b3
def fonk3(lines, b5 = True):
    return [clean_str(sentence) for sentence in lines] if b5 else lines