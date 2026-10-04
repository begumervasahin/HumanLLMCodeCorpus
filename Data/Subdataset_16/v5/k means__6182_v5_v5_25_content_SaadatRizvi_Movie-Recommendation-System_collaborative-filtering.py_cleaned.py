import pandas as pd
def fonk1():
    b1 = ['b16', 'movie_id', 'rating']
    b2 = ['movie_id', 'title']
    b3 = pd.read_csv('u.data', sep='\t', names=b1, usecols=range(3))
    b4 = pd.read_csv('u.item', sep='|', names=b2, usecols=range(2))
    return b3, b4
def fonk2(b3, b4):
    return pd.merge(b4, b3)
def fonk3(b3):
    return b3.pivot_table(b5 = 'b16', columns='title', values='rating')
def fonk4(b11):
    return b11.corr(b6 = 'pearson', min_periods=100)
def fonk5(b11, b16):
    return b11.loc[b16].dropna()
def fonk6(b11, b13, b12):
    b7 = pd.Series()
    for movie in b13.b5:
        b8 = b12[movie].dropna()
        b8 = b8.map(lambda x: x * b13[movie])
        b7 = b7.append(b8)
    b7 = b7.groupby(b7.b5).sum()
    b7.sort_values(b9 = True, ascending=False)
    return b7
def fonk7(b7, b13):
    return b7.drop(b13.b5, b10 = 'ignore')
def fonk8(b16):
    b3, b4 = fonk1()
    b3 = fonk2(b3, b4)
    b11 = fonk3(b3)
    b12 = fonk4(b11)
    b13 = fonk5(b11, b16)
    b7 = fonk6(b11, b13, b12)
    b14 = fonk7(b7, b13)
    print(b14.head())
    b14.to_csv("filteredSims.csv")
if b15 = = "__main__":
    fonk8(b16 = 2)