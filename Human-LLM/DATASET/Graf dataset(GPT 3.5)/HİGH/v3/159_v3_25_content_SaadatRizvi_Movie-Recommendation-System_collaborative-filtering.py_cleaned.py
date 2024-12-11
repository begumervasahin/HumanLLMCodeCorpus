import pandas as pd
b1 = pd.read_csv('u.data', sep='\t', names=['a1', 'movie_id', 'rating'])
b2 = pd.read_csv('u.item', sep='|', names=['movie_id', 'title'])
b3 = pd.merge(b2, b1)
b4 = b3.pivot_table(index='a1', columns='title', values='rating')
b5 = b4.corr(method='pearson', min_periods=100)
a1 = 2
b6 = b4.loc[a1].dropna()
b7 = pd.Series()
for movie_title, rating in b6.items():
    b8 = b5[rating].dropna()
    b8 = b8.map(lambda x: x * rating)
    b7 = b7.append(b8)
b7.sort_values(b9 = True, ascending=False)
b7 = b7.groupby(b7.index).sum()
b10 = b7.drop(b6.index, errors='ignore')
print(b10.head())
b10.to_csv("filteredSims.csv")