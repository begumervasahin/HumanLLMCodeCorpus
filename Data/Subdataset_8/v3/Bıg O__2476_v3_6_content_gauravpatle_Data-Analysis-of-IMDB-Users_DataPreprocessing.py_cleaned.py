import pandas as pd
def read_movie_data(file_path):
    return pd.read_csv(file_path, sep='\t', encoding='unicode_escape', header=None)
def extract_genres(data):
    genre = data.iloc[:, 4:23]
    genre.columns = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
                     "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
                     "War", "Western"]
    return genre
def concatenate_genres(genre):
    genre['GENRE'] = ""
    for index, row in genre.iterrows():
        res = ""
        for column in genre.columns[:-1]:
            if row[column] == 1:
                res += "," + column
        genre.at[index, 'GENRE'] = res[1:]
    return genre['GENRE']
def prepare_final_dataframe(data, genre):
    data_part1 = data.iloc[:, 0:3]
    data_part2 = concatenate_genres(genre)
    return pd.concat([data_part1, data_part2], axis=1)
def write_final_dataframe(final_dataframe, output_file):
    final_dataframe.to_csv(output_file, sep='\t', index=None, header=None)
def main():
    file_path = 'u_item_cleaned.txt'
    output_file = 'movie_details.csv'
    data = read_movie_data(file_path)
    genre = extract_genres(data)
    final_dataframe = prepare_final_dataframe(data, genre)
    write_final_dataframe(final_dataframe, output_file)
if __name__ == "__main__":
    main()