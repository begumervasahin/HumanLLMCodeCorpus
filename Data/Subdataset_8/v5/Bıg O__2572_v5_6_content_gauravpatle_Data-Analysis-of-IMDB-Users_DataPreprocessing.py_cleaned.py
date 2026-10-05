import pandas as pd
def read_data(filename):
    data = pd.read_csv(filename, sep='\t', encoding='unicode_escape', header=None)
    return data
def extract_genre_columns(data):
    genre = data.iloc[:, 4:23]
    genre.columns = [
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
        "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
        "War", "Western"
    ]
    return genre
def generate_genre_string(genre):
    genre['GENRE'] = ""
    for index, row in genre.iterrows():
        res = ""
        for col_name in genre.columns[:-1]:
            if row[col_name] == 1:
                res += f",{col_name}"
        genre.at[index, 'GENRE'] = res[1:]
    return genre['GENRE']
def extract_relevant_columns(data, genre):
    data_part1 = data.iloc[:, 0:3]
    data_part2 = genre
    final_genre = pd.concat([data_part1, data_part2], axis=1)
    return final_genre
def save_to_file(data, filename):
    data.to_csv(filename, sep='\t', index=None, header=None)
def main():
    filename = 'u_item_cleaned.txt'
    data = read_data(filename)
    genre = extract_genre_columns(data)
    genre_string = generate_genre_string(genre)
    final_data = extract_relevant_columns(data, genre_string)
    output_filename = 'movie_details.csv'
    save_to_file(final_data, output_filename)
if __name__ == "__main__":
    main()