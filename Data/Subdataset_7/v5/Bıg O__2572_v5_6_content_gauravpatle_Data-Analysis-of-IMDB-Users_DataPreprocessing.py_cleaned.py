import pandas as pd
def fonk1(b9):
    b1 = pd.read_csv(b9, b8='\t', encoding='unicode_escape', header=None)
    return b1
def fonk2(b1):
    b2 = b1.iloc[:, 4:23]
    b2.b3 = [
        "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
        "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
        "War", "Western"
    ]
    return b2
def fonk3(b2):
    b2['GENRE'] = ""
    for index, row in b2.iterrows():
        b4 = ""
        for col_name in b2.b3[:-1]:
            if row[col_name] == 1:
                b4 += f",{col_name}"
        b2.at[index, 'GENRE'] = b4[1:]
    return b2['GENRE']
def fonk4(b1, b2):
    b5 = b1.iloc[:, 0:3]
    b6 = b2
    b7 = pd.concat([b5, b6], axis=1)
    return b7
def fonk5(b1, b9):
    b1.to_csv(b9, b8 = '\t', index=None, header=None)
def fonk6():
    b9 = 'u_item_cleaned.txt'
    b1 = fonk1(b9)
    b2 = fonk2(b1)
    b10 = fonk3(b2)
    b11 = fonk4(b1, b10)
    b12 = 'movie_details.csv'
    fonk5(b11, b12)
if b13 = = "__main__":
    fonk6()