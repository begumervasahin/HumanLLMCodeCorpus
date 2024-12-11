import pandas as pd
def fonk1(b8):
    return pd.read_csv(b8, b1 = '\t', encoding='unicode_escape', header=None)
def fonk2(b10):
    b2 = b10.iloc[:, 4:23]
    b2.b3 = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
                     "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
                     "War", "Western"]
    return b2
def fonk3(b2):
    b2['GENRE'] = ""
    for index, row in b2.iterrows():
        b4 = ""
        for column in b2.b3[:-1]:
            if row[column] == 1:
                b4 += "," + column
        b2.at[index, 'GENRE'] = b4[1:]
    return b2['GENRE']
def fonk4(b10, b2):
    b5 = b10.iloc[:, 0:3]
    b6 = fonk3(b2)
    return pd.concat([b5, b6], b7 = 1)
def fonk5(b11, b9):
    b11.to_csv(b9, b1 = '\t', index=None, header=None)
def fonk6():
    b8 = 'u_item_cleaned.txt'
    b9 = 'movie_details.csv'
    b10 = fonk1(b8)
    b2 = fonk2(b10)
    b11 = fonk4(b10, b2)
    fonk5(b11, b9)
if b12 = = "__main__":
    fonk6()