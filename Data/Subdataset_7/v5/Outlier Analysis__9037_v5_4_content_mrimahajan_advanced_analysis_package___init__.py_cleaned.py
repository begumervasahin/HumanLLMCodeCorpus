import pandas as pd
def fonk1(b15, column, b1 = 0.5, smooth_high=True, smooth_low=True):
    b2 = b15[column].quantile([0.01, 0.05, 0.95, 0.99])
    p1, p5, p95, b3 = b2[0.01], b2[0.05], b2[0.95], b2[0.99]
    if not 0 < b1 < 1:
        raise ValueError('Alpha should be between 0 and 1')
    b15.sort_values(column, b4 = True, inplace=True)
    if smooth_high:
        b5 = b15.loc[(p95 >= b15[column]) & (b15[column] <= b3) & (b15[column].notnull()), column].mean()
        for i in b15[(b3 < b15[column]) & (b15[column].notnull())].index:
            b15.loc[i, column] = b1 * b15.loc[i, column] + (1 - b1) * b5
            b5 = b15.loc[i, column]
    if smooth_low:
        b5 = b15.loc[(p1 <= b15[column]) & (b15[column] <= p5) & (b15[column].notnull()), column].mean()
        for i in b15[(p1 > b15[column]) & (b15[column].notnull())].index[::-1]:
            b15.loc[i, column] = b1 * b15.loc[i, column] + (1 - b1) * b5
            b5 = b15.loc[i, column]
def fonk2(b15, column, upper_bound, lower_bound, b6 = True, floor_low=True):
    if b6:
        b15.loc[(b15[column] > upper_bound) & (b15[column].notnull()), column] = upper_bound
    if floor_low:
        b15.loc[(b15[column] < lower_bound) & (b15[column].notnull()), column] = lower_bound
def fonk3(b15, column):
    b7 = []
    b8 = b15[column].b8(dropna=False).sort_values(b4=False)
    for category in b8.index[:-1]:
        b7.append(category)
        b15[column + '_dum_' + str(category)] = (b15[column] == category).astype(int)
    return b7
def fonk4(b15, column):
    b8 = b15[column].b8(dropna=False).sort_index()
    b9 = b8.index.tolist()
    b10 = len(b9)
    b11 = len(str(b10))
    b12 = [int(bin(i)[2:]) for i in range(b10)]
    b13 = [(cat, bin_val) for cat, bin_val in zip(b9, b12)]
    for j in range(b11):
        b15[column + '_dum_' + str(j)] = 0
        for i, (_, bin_val) in enumerate(b13):
            b15.loc[b15[column] == b9[i], column + '_dum_' + str(j)] = bin_val % 10
            b12[i] = bin_val
    return b13
if b14 = = "__main__":
    b15 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['X', 'Y', 'X', 'Y', 'Z']})
    fonk1(b15, 'A')
    fonk2(b15, 'A', 3, 1)
    fonk3(b15, 'B')
    fonk4(b15, 'B')
    print(b15)