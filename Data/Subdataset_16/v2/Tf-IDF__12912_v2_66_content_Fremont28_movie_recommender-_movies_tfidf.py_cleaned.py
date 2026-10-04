import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First 3 rows of the dataset:")
print(b1.head(3))
b2 = len(b1)
print(f"Total number of movies in the dataset: {b2}")
b3 = b1.groupby(['original_title']).agg({'popularity': 'count'}).reset_index()
b4 = b1['original_title'].unique()
print(f"Number of unique movie titles: {len(b4)}")
b5 = b1['original_language'].unique()
print(f"Languages in the dataset: {b5}")
b1['overview'] = b1['overview'].fillna('')
b6 = TfidfVectorizer(stop_words='english')
b7 = b6.fit_transform(b1['overview'])
print(f"TF-IDF matrix shape: {b7.shape}")
b8 = linear_kernel(b7, b7)
b9 = pd.Series(b1.index, index=b1['original_title']).drop_duplicates()
def fonk1(title, b8 = b8):
    b10 = b9[title]
    b11 = list(enumerate(b8[b10]))
    b11 = sorted(b11, key=lambda x: x[1], reverse=True)
    b11 = b11[1:20]
    b12 = [i[0] for i in b11]
    return b1['original_title'].iloc[b12]
b13 = fonk1("No Reservations")
print(f"Movies recommended for 'No Reservations':\n{b13}")