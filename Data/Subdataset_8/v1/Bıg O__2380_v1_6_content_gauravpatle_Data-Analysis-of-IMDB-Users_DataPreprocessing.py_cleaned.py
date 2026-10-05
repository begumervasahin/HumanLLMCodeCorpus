import pandas as pd
data = pd.read_csv('u_item_cleaned.txt', sep='\t', encoding='unicode_escape', header=None)
genre = data.iloc[:, 4:23]
genre.columns = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary",
                 "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller",
                 "War", "Western"]
genre['GENRE'] = ""
for index, row in genre.iterrows():
    res = ""
    if row['unknown'] == 1:
        res += ",unknown"
    if row['Action'] == 1:
        res += ",Action"
    if row['Adventure'] == 1:
        res += ",Adventure"
    if row['Animation'] == 1:
        res += ",Animation"
    if row['Children'] == 1:
        res += ",Children"
    if row['Comedy'] == 1:
        res += ",Comedy"
    if row['Crime'] == 1:
        res += ",Crime"
    if row['Documentary'] == 1:
        res += ",Documentary"
    if row['Drama'] == 1:
        res += ",Drama"
    if row['Fantasy'] == 1:
        res += ",Fantasy"
    if row['Film_Noir'] == 1:
        res += ",Film_Noir"
    if row['Horror'] == 1:
        res += ",Horror"
    if row['Musical'] == 1:
        res += ",Musical"
    if row['Mystery'] == 1:
        res += ",Mystery"
    if row['Romance'] == 1:
        res += ",Romance"
    if row['Sci_Fi'] == 1:
        res += ",Sci_Fi"
    if row['Thriller'] == 1:
        res += ",Thriller"
    if row['War'] == 1:
        res += ",War"
    if row['Western'] == 1:
        res += ",Western"
    genre.at[index, 'GENRE'] = res[1:]
data_part1 = data.iloc[:, 0:3]
data_part2 = genre.iloc[:, -1]
final_genre = pd.concat([data_part1, data_part2], axis=1)
final_genre.to_csv('movie_details.csv', sep='\t', index=None, header=None)