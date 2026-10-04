import pandas as pd
b1 = ['a1', 'movie_id', 'rating']
b2 = pd.read_csv('u.data', sep='\t', names=b1, usecols=range(3))
b3 = ['movie_id', 'title']
b4 = pd.read_csv('u.item', sep='|', names=b3, usecols=range(2))
b2 = pd.merge(b4, b2)
b5 = b2.pivot_table(index='a1', columns='title', values='rating')
b6 = b5.corr(method='pearson', min_periods=100)
a1 = 2
b7 = b5.loc[a1].dropna()
b8 = pd.Series(dtype='float64')
for movie in b7.index:
    b9 = b6[movie].dropna()
    b9 = b9.map(lambda x: x * b7[movie])
    b8 = b8.append(b9)
b8 = b8.groupby(b8.index).sum()
b8.sort_values(b10 = True, ascending=False)
b11 = b8.drop(b7.index, errors='ignore')
print(b11.head())
b11.to_csv("filteredSims.csv")