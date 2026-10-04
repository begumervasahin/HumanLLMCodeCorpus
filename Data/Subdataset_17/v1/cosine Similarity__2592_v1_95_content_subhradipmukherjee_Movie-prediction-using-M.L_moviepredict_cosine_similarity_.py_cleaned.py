import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import movie_predict_knn
def get_title(index, df):
    return df[df.index == index]["title"].values[0]
def get_index(title, df):
    return df[df.title == title]["index"].values[0]
def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
def main():
    df = pd.read_csv("D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv")
    features = ['keywords', 'cast', 'genres', 'director']
    for feature in features:
        df[feature] = df[feature].fillna('')
    df["combined_features"] = df.apply(combine_features, axis=1)
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    movie = "Avengers: Age of Ultron"
    index = int(get_index(movie, df))
    similar_movies = list(enumerate(cosine_sim[index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    print("Result with cosine similarity:")
    i = 0
    a = []
    for movie in sorted_similar_movies:
        print(get_title(movie[0], df))
        a.append(get_title(movie[0], df))
        i += 1
        if i > 5:
            break
    print("Result with KNN:")
    K = 5
    movie_predict_knn.main(index, K)
if __name__ == '__main__':
    main()