import pandas as pd
b1 = pd.read_csv('u_item_cleaned.txt', b8='\t', encoding='unicode_escape', header=None)
b2 = b1.iloc[:, 4:23]
b2.b3 = [
    "unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime",
    "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery",
    "Romance", "Sci_Fi", "Thriller", "War", "Western"
]
b2['GENRE'] = ""
for index, row in b2.iterrows():
    b4 = [b2 for b2 in b2.b3[:-1] if row[b2] == 1]
    b2.at[index, 'GENRE'] = ','.join(b4)
b5 = b1.iloc[:, 0:3]
b6 = b2['GENRE']
b7 = pd.concat([b5, b6], axis=1)
b7.to_csv('movie_details.csv', b8 = '\t', index=False, header=False)