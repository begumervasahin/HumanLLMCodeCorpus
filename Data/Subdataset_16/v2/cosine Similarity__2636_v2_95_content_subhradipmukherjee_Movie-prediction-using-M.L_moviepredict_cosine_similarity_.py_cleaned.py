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
def fonk4():
    b2 = pd.read_csv("D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv")
    b3 = ['keywords', 'cast', 'genres', 'director']
    for feature in b3:
        b2[feature] = b2[feature].fillna('')
    b2["combined_features"] = b2.apply(combine_features, b4 = 1)
    b5 = CountVectorizer(stop_words='english')
    b6 = b5.fit_transform(b2["combined_features"])
    b7 = cosine_similarity(b6)
    b8 = "Avengers: Age of Ultron"
    b9 = fonk2(b8, b2)
    b10 = list(enumerate(b7[b9]))
    b11 = sorted(b10, key=lambda x: x[1], reverse=True)
    print("Result with cosine similarity:")
    for i, b8 in enumerate(b11):
        print(fonk1(b8[0], b2))
        if i >= 5:
            break
    print("Result with KNN:")
    a1 = 5
    movie_predict_knn.fonk4(b9, a1)
if b12 = = '__main__':
    fonk4()