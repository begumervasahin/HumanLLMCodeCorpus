import pandas as pd
b1 = pd.read_csv('u_item_cleaned.txt', b9='\t', encoding='unicode_escape', header=None)
b2 = ["unknown", "Action", "Adventure", "Animation", "Children", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film_Noir", "Horror", "Musical", "Mystery", "Romance", "Sci_Fi", "Thriller", "War", "Western"]
b3 = b1.iloc[:, 4:23]
b3.b4 = b2
b3['GENRE'] = ""
for index, row in b3.iterrows():
    b5 = [col for col in b2 if row[col] == 1]
    b3.at[index, 'GENRE'] = ','.join(b5)
b6 = b1.iloc[:, 0:3]
b7 = b3['GENRE']
b8 = pd.concat([b6, b7], axis=1)
b8.to_csv('movie_details.csv', b9 = '\t', index=False, header=False)