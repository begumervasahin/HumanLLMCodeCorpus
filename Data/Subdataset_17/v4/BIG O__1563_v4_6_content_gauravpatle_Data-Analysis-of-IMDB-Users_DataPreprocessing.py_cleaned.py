import pandas as pd
data = pd.read_csv('u_item_cleaned.txt', sep='\t', encoding='unicode_escape', header=None)
genre = data.iloc[:, 4:23]
genre.columns = [
    "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
    "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery",
    "Romance", "Sci_Fi", "Thriller", "War", "Western"
]
genre['GENRE'] = ""
for index, row in genre.iterrows():
    genres = [genre for genre in genre.columns[:-1] if row[genre] == 1]
    genre.at[index, 'GENRE'] = ','.join(genres)
data_part1 = data.iloc[:, 0:3]
data_part2 = genre['GENRE']
final_genre = pd.concat([data_part1, data_part2], axis=1)
final_genre.to_csv('movie_details.csv', sep='\t', index=False, header=False)