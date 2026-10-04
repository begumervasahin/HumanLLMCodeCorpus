import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import movie_predict_knn
def get_title(index, df):
    return df.iloc[index]["title"]
def get_index(title, df):
    return df[df.title == title].index[0]
def combine_features(row):
    return f"{row['keywords']} {row['cast']} {row['genres']} {row['director']}"
def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    features = ['keywords', 'cast', 'genres', 'director']
    for feature in features:
        df[feature] = df[feature].fillna('')
    df["combined_features"] = df.apply(combine_features, axis=1)
    return df
def compute_cosine_similarity(df):
    vectorizer = CountVectorizer(stop_words='english')
    count_matrix = vectorizer.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    return cosine_sim
def print_similar_movies(movie, df, cosine_sim):
    movie_index = get_index(movie, df)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    print("Results with cosine similarity:")
    for i, movie in enumerate(sorted_similar_movies):
        print(get_title(movie[0], df))
        if i >= 5:
            break
def main():
    file_path = "D:/roops_backup/projects/data mining project/movie_recommender/movie_dataset.csv"
    df = preprocess_data(file_path)
    cosine_sim = compute_cosine_similarity(df)
    movie = "Avengers: Age of Ultron"
    print_similar_movies(movie, df, cosine_sim)
    print("Results with KNN:")
    movie_index = get_index(movie, df)
    K = 5
    movie_predict_knn.main(movie_index, K)
if __name__ == '__main__':
    main()