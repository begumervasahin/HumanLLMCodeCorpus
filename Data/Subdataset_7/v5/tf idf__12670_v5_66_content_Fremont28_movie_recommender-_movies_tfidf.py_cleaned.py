import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First few rows of the dataset:")
print(b1.head(3))
b2 = len(b1)
b3 = b1.groupby('original_title')['popularity'].count().reset_index()
b4 = len(b3)
b5 = b1['original_language'].unique()
b6 = TfidfVectorizer(stop_words='english')
b1['overview'] = b1['overview'].fillna('')
b7 = b6.fit_transform(b1['overview'])
b8 = b7.shape
b9 = linear_kernel(b7, b7)
b10 = pd.Series(b1.index, index=b1['original_title']).drop_duplicates()
def fonk1(title, b11 = b9):
    b12 = b10[title]
    b13 = list(enumerate(b11[b12]))
    b13 = sorted(b13, key=lambda x: x[1], reverse=True)
    b13 = b13[1:20]
    b14 = [index[0] for index in b13]
    return b1['original_title'].iloc[b14]
b15 = fonk1("No Reservations")
print("\nRecommended movies for 'No Reservations':")
print(b15)