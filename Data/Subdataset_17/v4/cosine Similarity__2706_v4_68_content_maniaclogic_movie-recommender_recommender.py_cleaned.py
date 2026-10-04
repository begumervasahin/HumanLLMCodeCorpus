import pandas as pd
import numpy as np
from models import R, nmf, DF
def recommend(user_input_dict):
    movie_ids = sorted(R.columns)
    ratings_dict = dict(zip(movie_ids, [np.nan] * len(movie_ids)))
    for movie_id, rating in user_input_dict.items():
        ratings_dict[movie_id] = rating
    user_profile = pd.DataFrame([list(ratings_dict.values())], columns=movie_ids)
    user_profile_filled = user_profile.fillna(3.0)
    hidden_profile = nmf.transform(user_profile_filled)
    predictions = np.dot(hidden_profile, nmf.components_)
    predicted_ratings = pd.DataFrame(predictions, columns=R.columns)
    unwatched_movies = user_profile.isna().T[0]
    movies_not_watched = predicted_ratings.T[0][unwatched_movies]
    top_movie_ids = movies_not_watched.sort_values(ascending=False).index[:5]
    recommendations = DF.loc[DF['movieId'].isin(top_movie_ids), 'title'].values.tolist()
    return recommendations
if __name__ == "__main__":
    user_input_dict = {
        1: 5.0,
        2: 3.5,
    }
    recommendations = recommend(user_input_dict)
    print("Recommended Movies:")
    for movie in recommendations:
        print(movie)