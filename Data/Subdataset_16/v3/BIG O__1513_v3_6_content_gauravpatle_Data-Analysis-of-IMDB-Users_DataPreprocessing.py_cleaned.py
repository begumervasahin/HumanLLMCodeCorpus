import pandas as pd
def fonk1(file_path):
    return pd.read_csv(file_path, b1 = '\t', encoding='unicode_escape', header=None)
def fonk2(b10):
    b2 = [
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy",
        "Crime", "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror",
        "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller", "War", "Western"
    ]
    b3 = b10.iloc[:, 4:23]
    b3.b4 = b2
    return b3
def fonk3(b3):
    b3['GENRE'] = ""
    for index, row in b3.iterrows():
        b5 = [col for col in b3.b4 if row[col] == 1]
        b3.at[index, 'GENRE'] = ','.join(b5)
    return b3['GENRE']
def fonk4(original_data, b11):
    b6 = original_data.iloc[:, 0:3]
    return pd.concat([b6, b11], b7 = 1)
def fonk5(b10, b9):
    b10.to_csv(b9, b1 = '\t', index=False, header=False)
def fonk6():
    b8 = 'u_item_cleaned.txt'
    b9 = 'movie_details.csv'
    b10 = fonk1(b8)
    b3 = fonk2(b10)
    b11 = fonk3(b3)
    b12 = fonk4(b10, b11)
    fonk5(b12, b9)
if b13 = = "__main__":
    fonk6()