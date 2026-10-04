import pandas as pd
data = pd.read_csv('u_item_cleaned.txt', sep='\t', encoding='unicode_escape', header=None)
genre_columns = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller", "War", "Western"]
genre_data = data.iloc[:, 4:23]
genre_data.columns = genre_columns
genre_data['GENRE'] = ""
for index, row in genre_data.iterrows():
    genres = [col for col in genre_columns if row[col] == 1]
    genre_data.at[index, 'GENRE'] = ','.join(genres)
data_part1 = data.iloc[:, 0:3]
genre_column = genre_data['GENRE']
final_data = pd.concat([data_part1, genre_column], axis=1)
final_data.to_csv('movie_details.csv', sep='\t', index=False, header=False)