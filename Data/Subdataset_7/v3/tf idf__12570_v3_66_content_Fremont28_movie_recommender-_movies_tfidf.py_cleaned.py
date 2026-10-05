import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First few rows of the dataset:")
print(b1.head(3))
b2 = len(b1)
print("Total number of movies in the dataset:", b2)
b3 = b1['original_title'].nunique()
print("Number of unique movie titles:", b3)
b4 = b1['original_language'].unique()
print("Unique languages in the dataset:", b4)
b5 = TfidfVectorizer(stop_words='english')
b6 = b1['overview'].fillna('')
b7 = b5.fit_transform(b6)
print("TF-IDF matrix shape:", b7.shape)
b8 = linear_kernel(b7, b7)
b9 = pd.Series(b1.index, index=b1['original_title']).drop_duplicates()
def fonk1(movie_title, b8 = b8, top_n=20):
    b10 = b9[movie_title]
    b11 = list(enumerate(b8[b10]))
    b11 = sorted(b11, key=lambda x: x[1], reverse=True)
    b12 = [index[0] for index in b11[1:top_n + 1]]
    return b1['original_title'].iloc[b12]
b13 = fonk1("No Reservations")
print("Recommendations for 'No Reservations':")
print(b13)