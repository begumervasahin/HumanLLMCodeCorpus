import pandas as pd
def fonk1(b13, b14):
    b1 = ['a1', 'movie_id', 'rating']
    b2 = ['movie_id', 'title']
    b3 = pd.read_csv(b13, sep='\t', names=b1, usecols=range(3))
    b4 = pd.read_csv(b14, sep='|', names=b2, usecols=range(2))
    return pd.merge(b4, b3)
def fonk2(b3):
    return b3.pivot_table(b5 = 'a1', columns='title', values='rating')
def fonk3(b15, b6 = 100):
    return b15.corr(b7 = 'pearson', b6=b6)
def fonk4(b15, b16, a1):
    b8 = b15.loc[a1].dropna()
    b9 = pd.Series(dtype='float64')
    for movie in b8.b5:
        b10 = b16[movie].dropna()
        b10 = b10.map(lambda x: x * b8[movie])
        b9 = b9.append(b10)
    b9 = b9.groupby(b9.b5).sum()
    b9.sort_values(b11 = True, ascending=False)
    return b9.drop(b8.b5, b12 = 'ignore')
def fonk5():
    b13 = 'u.data'
    b14 = 'u.item'
    a1 = 2
    b3 = fonk1(b13, b14)
    b15 = fonk2(b3)
    b16 = fonk3(b15)
    b17 = fonk4(b15, b16, a1)
    print(b17.head())
    b17.to_csv("filteredSims.csv")
if b18 = = "__main__":
    fonk5()