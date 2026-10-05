import pandas as pd
def fonk1(file_path):
    return pd.fonk1(file_path).drop(b1 = ['Unnamed: 0'], errors='ignore')
b2 = fonk1('path/to/weebtoon_star_info.csv')
b3 = fonk1('path/to/weebtoon_reply_info.csv')
def fonk2(csv, titles, noms):
    b4 = [[] for _ in range(10)]
    for title, nom in zip(titles, noms):
        b5 = csv[(csv['titleId'] == title) & (csv['nom'] == nom)]
        for j in range(1, 11):
            try:
                b4[j - 1].append(str(b5[f'comment{j}'].values[0]))
            except IndexError:
                b4[j - 1].append('')
    return b4
b6 = b2.sort_values(by='star_point')
b7 = b6.head(1000).drop_duplicates(["titleId", "nom"], keep='first')
b8 = b7['titleId']
b9 = b7['nom']
b10 = fonk2(b3, b8, b9)
for i, b4 in enumerate(b10):
    b7[f'comment{i+1}'] = b4
b7 = b7[b7['comment1'] != ''].head(500)
b7.to_csv("./lowstar_reply.csv", b11 = "utf_8_sig", mode='w')
b12 = b2[b2['star_point'] == 9.99].sample(n=1000).drop_duplicates(["titleId", "nom"], keep='first')
b13 = b12['titleId']
b14 = b12['nom']
b15 = fonk2(b3, b13, b14)
for i, b4 in enumerate(b15):
    b12[f'comment{i+1}'] = b4
b12 = b12[b12['comment1'] != ''].head(500)
b12.to_csv("./highstar_reply.csv", b11 = "utf_8_sig", mode='w')