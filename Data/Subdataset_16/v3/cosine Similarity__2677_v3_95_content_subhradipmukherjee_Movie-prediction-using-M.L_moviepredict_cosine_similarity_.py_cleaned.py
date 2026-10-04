import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import movie_predict_knn
def fonk1(index, b2):
    return b2.iloc[index]["b1"]
def fonk2(b1, b2):
    return b2[b2.b1 = = b1].index[0]
def fonk3(row):
    return f"{row['keywords']} {row['cast']} {row['genres']} {row['director']}"
def fonk4(b11):
    b2 = pd.read_csv(b11)
    b3 = ['keywords', 'cast', 'genres', 'director']
    for feature in b3:
        b2[feature] = b2[feature].fillna('')
    b2["combined_features"] = b2.apply(combine_features, b4 = 1)
    return b2
def fonk5(b2):
    b5 = CountVectorizer(stop_words='english')
    b6 = b5.fit_transform(b2["combined_features"])
    b7 = cosine_similarity(b6)
    return b7
def fonk6(b12, b2, b7):
    b8 = fonk2(b12, b2)
    b9 = list(enumerate(b7[b8]))
    b10 = sorted(b9, key=lambda x: x[1], reverse=True)
    print("Results with cosine similarity:")
    for i, b12 in enumerate(b10):
        print(fonk1(b12[0], b2))
        if i >= 5:
            break
def fonk7():
    b11 = "D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv"
    b2 = fonk4(b11)
    b7 = fonk5(b2)
    b12 = "Avengers: Age of Ultron"
    fonk6(b12, b2, b7)
    print("Results with KNN:")
    b8 = fonk2(b12, b2)
    a1 = 5
    movie_predict_knn.fonk7(b8, a1)
if b13 = = '__main__':
    fonk7()