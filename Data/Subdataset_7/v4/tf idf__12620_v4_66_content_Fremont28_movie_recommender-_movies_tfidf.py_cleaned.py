import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
b1.head(3)
b2 = len(b1)
b3 = b1.groupby(['original_title']).agg({'popularity':'count'}).reset_index()
b4 = len(b1['original_title'].unique())
b5 = b1['original_language'].unique()
b6 = TfidfVectorizer(stop_words='english')
b1['overview'] = b1['overview'].fillna('')
b7 = b6.fit_transform(b1['overview'])
b8 = b7.shape
b9 = linear_kernel(b7, b7)
b10 = pd.Series(b1.index, index=b1['original_title']).drop_duplicates()
def fonk1(title, b9 = b9):
    b11 = b10[title]
    b12 = list(enumerate(b9[b11]))
    b12 = sorted(b12, key=lambda x: x[1], reverse=True)
    b12 = b12[1:20]
    b13 = [i[0] for i in b12]
    return b1['original_title'].iloc[b13]
b14 = fonk1("No Reservations")