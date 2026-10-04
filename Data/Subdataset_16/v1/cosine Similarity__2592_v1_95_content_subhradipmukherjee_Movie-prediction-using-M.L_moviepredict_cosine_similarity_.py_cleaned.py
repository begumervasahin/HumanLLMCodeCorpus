import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import movie_predict_knn
def fonk1(b1, b3):
    return b3[b3.b1 = = b1]["b2"].values[0]
def fonk2(b2, b3):
    return b3[b3.b2 = = b2]["b1"].values[0]
def fonk3(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
def fonk4():
    b3 = pd.read_csv("D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv")
    b4 = ['keywords', 'cast', 'genres', 'director']
    for feature in b4:
        b3[feature] = b3[feature].fillna('')
    b3["combined_features"] = b3.apply(combine_features, b5 = 1)
    b6 = CountVectorizer()
    b7 = b6.fit_transform(b3["combined_features"])
    b8 = cosine_similarity(b7)
    b9 = "Avengers: Age of Ultron"
    b1 = int(fonk2(b9, b3))
    b10 = list(enumerate(b8[b1]))
    b11 = sorted(b10, key=lambda x: x[1], reverse=True)
    print("Result with cosine similarity:")
    a1 = 0
    b12 = []
    for b9 in b11:
        print(fonk1(b9[0], b3))
        b12.append(fonk1(b9[0], b3))
        a1 += 1
        if a1 > 5:
            break
    print("Result with KNN:")
    a2 = 5
    movie_predict_knn.fonk4(b1, a2)
if b13 = = '__main__':
    fonk4()