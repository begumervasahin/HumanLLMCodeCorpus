import pandas as pd
b1 = 'path/to/weebtoon_star_info.csv'
b2 = 'path/to/weebtoon_reply_info.csv'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
b4 = b4.drop(columns=['Unnamed: 0'])
b5 = [[] for _ in range(10)]
b6 = b3.sort_values(by='star_point')
b7 = b6.head(1000).drop_duplicates(subset=["titleId", "nom"])
print(b7)
b8 = b7['titleId'].tolist()
b9 = b7['nom'].tolist()
for title_id, nom in zip(b8, b9):
    b10 = b4[(b4['titleId'] == title_id) & (b4['nom'] == nom)]
    for i in range(10):
        try:
            b5[i].append(str(b10[f'comment{i+1}'].values[0]))
        except IndexError:
            b5[i].append('')
for i in range(10):
    b7[f'comment{i+1}'] = b5[i]
b7 = b7[b7['comment1'] != '']
print(b7)
b7 = b7.head(500)
print(b7)
b7.to_csv("./lowstar_reply.csv", b11 = "utf_8_sig", mode='w')
b12 = b3[b3['star_point'] == 9.99].sample(n=1000).drop(columns=['Unnamed: 0'])
b12 = b12.drop_duplicates(subset=["titleId", "nom"])
b13 = b12['titleId'].tolist()
b14 = b12['nom'].tolist()
b5 = [[] for _ in range(10)]
for title_id, nom in zip(b13, b14):
    b10 = b4[(b4['titleId'] == title_id) & (b4['nom'] == nom)]
    for i in range(10):
        try:
            b5[i].append(str(b10[f'comment{i+1}'].values[0]))
        except IndexError:
            b5[i].append('')
for i in range(10):
    b12[f'comment{i+1}'] = b5[i]
b12 = b12[b12['comment1'] != '']
print(b12)
b12 = b12.head(500)
print(b12)
b12.to_csv("./highstar_reply.csv", b11 = "utf_8_sig", mode='w')