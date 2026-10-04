import pandas as pd
def load_data(file_path):
    return pd.read_csv(file_path, sep='\t', encoding='unicode_escape', header=None)
def extract_genre_columns(data):
    genre_columns = [
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
        "Crime", "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror",
        "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller", "War", "Western"
    ]
    genre_data = data.iloc[:, 4:23]
    genre_data.columns = genre_columns
    return genre_data
def concatenate_genres(genre_data):
    genre_data['GENRE'] = ""
    for index, row in genre_data.iterrows():
        genres = [col for col in genre_data.columns if row[col] == 1]
        genre_data.at[index, 'GENRE'] = ','.join(genres)
    return genre_data['GENRE']
def combine_data(original_data, genre_column):
    data_part1 = original_data.iloc[:, 0:3]
    return pd.concat([data_part1, genre_column], axis=1)
def save_data(data, output_file):
    data.to_csv(output_file, sep='\t', index=False, header=False)
def main():
    input_file = 'u_item_cleaned.txt'
    output_file = 'movie_details.csv'
    data = load_data(input_file)
    genre_data = extract_genre_columns(data)
    genre_column = concatenate_genres(genre_data)
    final_data = combine_data(data, genre_column)
    save_data(final_data, output_file)
if __name__ == "__main__":
    main()