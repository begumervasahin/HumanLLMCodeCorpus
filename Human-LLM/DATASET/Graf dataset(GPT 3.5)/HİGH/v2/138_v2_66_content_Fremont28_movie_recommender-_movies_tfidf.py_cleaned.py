import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("tmdb_5000_movies.csv", encoding="latin-1")
print("First few rows of the dataset:")
print(b1.head(3))
b2 = len(b1)
print("Total number of movies in the dataset:", b2)
b3 = len(b1['original_title'].unique())
print("Number of unique movie titles:", b3)
b4 = b1['original_language'].unique()
print("Unique languages in the dataset:", b4)
b5 = TfidfVectorizer(stop_words='english')
b1['overview'] = b1['overview'].fillna('')
b6 = b5.fit_transform(b1['overview'])
print("TF-IDF matrix shape:", b6.shape)
b7 = linear_kernel(b6, b6)
b8 = pd.Series(b1.index, index=b1['original_title']).drop_duplicates()
def fonk1(movie_title, b7 = b7):
    b9 = b8[movie_title]
    b10 = list(enumerate(b7[b9]))
    b10 = sorted(b10, key=lambda x: x[1], reverse=True)
    b11 = [index[0] for index in b10[1:20]]
    return b1['original_title'].iloc[b11]
b12 = fonk1("No Reservations")
print("Recommendations for 'No Reservations':")
print(b12)