import pandas as pd
import numpy as np
from models import R, nmf, DF
def recommend(user_input_dict):
    movie_ids = sorted(list(R.columns))
    empty_list = [np.nan] * len(movie_ids)
    ratings_dict = dict(zip(movie_ids, empty_list))
    for key, value in user_input_dict.items():
        ratings_dict[key] = value
    user_profile = pd.DataFrame([list(ratings_dict.values())], columns=movie_ids)
    user_profile_filled = user_profile.fillna(3.0)
    hidden_profile = nmf.transform(user_profile_filled)
    prediction = np.dot(hidden_profile, nmf.components_)
    predicted_ratings = pd.DataFrame(prediction, columns=R.columns)
    movies_not_watched = predicted_ratings.T[0][user_profile.isna().T[0]]
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