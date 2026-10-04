import pandas as pd
import numpy as nm
import movie_predict_knn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(b1):
    return b3[b3.b1 = = b1]["b2"].values[0]
def fonk2(b2):
    return b3[b3.b2 = = b2]["b1"].values[0]
b3 = pd.read_csv("D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv")
b4 = ['keywords','cast','genres','director']
for feature in b4:
    b3[feature] = b3[feature].fillna('')
def fonk3(row):
    return row['keywords'] +" "+row['cast']+" "+row['genres']+" "+row['director']
b3["combined_features"] = b3.apply(combine_features,b5 = 1)
b6 = CountVectorizer()
b7 = b6.fit_transform(b3["combined_features"])
b8 = cosine_similarity(b7)
b9 = "Avengers: Age of Ultron"
b1 = fonk2(b9)
b1 = int(b1)
b10 = []
b11 = list(enumerate(b8[b1]))
b12 = sorted(b11,key=lambda x:x[1],reverse=True)
a1 = 0
print("result with cosine similarity")
for movies in b12:
    print (fonk1(movies[0]))
    b10.append(fonk1(movies[0]))
    a1 = a1+1
    if (a1>5):
       break
print("result with knn")
a2 = 5
b13 = []
movie_predict_knn.main(b1,a2)