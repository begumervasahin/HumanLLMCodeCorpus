import pandas as pd
b1 = pd.read_csv('u_item_cleaned.txt', b8='\t', encoding='unicode_escape', header=None)
b2 = b1.iloc[:, 4:23]
b2.b3 = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
                 "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
                 "War", "Western"]
b2['GENRE'] = ""
for index, row in b2.iterrows():
    b4 = ""
    if row['unknown'] == 1:
        b4 += ",unknown"
    if row['Action'] == 1:
        b4 += ",Action"
    if row['Adventure'] == 1:
        b4 += ",Adventure"
    if row['Animation'] == 1:
        b4 += ",Animation"
    if row['Children'] == 1:
        b4 += ",Children"
    if row['Comedy'] == 1:
        b4 += ",Comedy"
    if row['Crime'] == 1:
        b4 += ",Crime"
    if row['Documentary'] == 1:
        b4 += ",Documentary"
    if row['Drama'] == 1:
        b4 += ",Drama"
    if row['Fantasy'] == 1:
        b4 += ",Fantasy"
    if row['Film_Noir'] == 1:
        b4 += ",Film_Noir"
    if row['Horror'] == 1:
        b4 += ",Horror"
    if row['Musical'] == 1:
        b4 += ",Musical"
    if row['Mystery'] == 1:
        b4 += ",Mystery"
    if row['Romance'] == 1:
        b4 += ",Romance"
    if row['Sci_Fi'] == 1:
        b4 += ",Sci_Fi"
    if row['Thriller'] == 1:
        b4 += ",Thriller"
    if row['War'] == 1:
        b4 += ",War"
    if row['Western'] == 1:
        b4 += ",Western"
    b2.at[index, 'GENRE'] = b4[1:]
b5 = b1.iloc[:, 0:3]
b6 = b2.iloc[:, -1]
b7 = pd.concat([b5, b6], axis=1)
b7.to_csv('movie_details.csv', b8 = '\t', index=None, header=None)