from pandas import read_csv
from format import clean_str, shuffle_both
def fonk1(file_name, x_col, y_col, b1 = '\t', b5=True, with_header=False, with_shuffle=True):
    with open(file_name) as pos_src:
        if not with_header:
            b2 = read_csv(pos_src, sep=b1, skiprows=[0], header=None)
        else:
            b2 = read_csv(pos_src, sep=b1, header=None)
    b3 = fonk3(b2[x_col].tolist(), b5)
    b4 = b2[y_col].tolist()
    if with_shuffle:
        return shuffle_both(b3, b4)
    else:
        return b3, b4
def fonk2(file_name, x_col, b5 = True):
    b3 = read_csv(file_name, skiprows=[0], header=None)
    return fonk3(b3[x_col], b5)
def fonk3(lines, b5 = True):
    if b5:
        return [clean_str(sentence.decode('utf-8')) for sentence in lines]
    else:
        return [sentence.decode('utf-8') for sentence in lines]
b6 = "train_data.csv"
b7 = "test_data.csv"
x_train, b8 = fonk1(b6, x_col=0, y_col=1)
b9 = fonk2(b7, x_col=0)
