import pandas as pd
b1 = 'path/to/weebtoon_star_info.csv'
b2 = 'path/to/weebtoon_reply_info.csv'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
del b4['Unnamed: 0']
b5 = [[] for _ in range(10)]
b6 = b3.sort_values(by='star_point', axis=0)
b7 = b6.head(1000).drop_duplicates(["titleId","nom"], keep='first')
b8 = b7['titleId']
b9 = b7['nom']
for i, (titleId, nom) in enumerate(zip(b8, b9)):
    b10 = b4[(b4['titleId'] == titleId) & (b4['nom'] == nom)]
    for j in range(1, 11):
        try:
            b5[j - 1].append(str(b10[f'comment{j}'].values[0]))
        except IndexError:
            b5[j - 1].append('')
for i in range(10):
    b7[f'comment{i+1}'] = b5[i]
b7 = b7[b7['comment1'] != '']
b7 = b7[:500 - len(b7)]
b7.to_csv("./lowstar_reply.csv", b11 = "utf_8_sig", mode='w')
b12 = b3[b3['star_point'] == 9.99].sample(n=1000).drop_duplicates(["titleId","nom"], keep='first')
b13 = b12['titleId']
b14 = b12['nom']
b5 = [[] for _ in range(10)]
for i, (titleId, nom) in enumerate(zip(b13, b14)):
    b10 = b4[(b4['titleId'] == titleId) & (b4['nom'] == nom)]
    for j in range(1, 11):
        try:
            b5[j - 1].append(str(b10[f'comment{j}'].values[0]))
        except IndexError:
            b5[j - 1].append('')
for i in range(10):
    b12[f'comment{i+1}'] = b5[i]
b12 = b12[b12['comment1'] != '']
b12 = b12[:500 - len(b12)]
b12.to_csv("./highstar_reply.csv", b11 = "utf_8_sig", mode='w')