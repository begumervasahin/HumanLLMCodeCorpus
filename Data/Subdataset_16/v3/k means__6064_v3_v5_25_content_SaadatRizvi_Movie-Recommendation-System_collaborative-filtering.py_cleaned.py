import pandas as pd
def fonk1(b11, b12):
    b1 = ['a1', 'movie_id', 'rating']
    b2 = pd.read_csv(b11, sep='\t', names=b1, usecols=range(3))
    b3 = ['movie_id', 'title']
    b4 = pd.read_csv(b12, sep='|', names=b3, usecols=range(2))
    return pd.merge(b4, b2)
def fonk2(b2):
    return b2.pivot_table(b5 = 'a1', columns='title', values='rating')
def fonk3(b13):
    return b13.corr(b6 = 'pearson', min_periods=100)
def fonk4(b13, a1):
    return b13.loc[a1].dropna()
def fonk5(b14, b15):
    b7 = pd.Series(dtype=float)
    for movie in b15.b5:
        b8 = b14[movie].dropna()
        b8 = b8.map(lambda x: x * b15[movie])
        b7 = b7.append(b8)
    b7 = b7.groupby(b7.b5).sum()
    b7.sort_values(b9 = True, ascending=False)
    return b7.drop(b15.b5, b10 = 'ignore')
def fonk6():
    b11 = 'u.data'
    b12 = 'u.item'
    a1 = 2
    b2 = fonk1(b11, b12)
    b13 = fonk2(b2)
    b14 = fonk3(b13)
    b15 = fonk4(b13, a1)
    b16 = fonk5(b14, b15)
    print(b16.head())
    b16.to_csv("filteredSims.csv")
if b17 = = "__main__":
    fonk6()