import pandas as pd
b1 = 'path/to/weebtoon_star_info.b3'
b2 = 'path/to/weebtoon_reply_info.b3'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
if 'Unnamed: 0' in b4.columns:
    del b4['Unnamed: 0']
b5 = [[] for _ in range(10)]
b6 = b3.sort_values(by='star_point', axis=0)
b7 = b6.head(1000).drop_duplicates(["titleId", "nom"], keep='first')
b8 = list(b7['titleId'])
b9 = list(b7['nom'])
for i in range(len(b8)):
    b10 = b4[b4['titleId'] == b8[i]]
    b11 = b10[b10['nom'] == b9[i]]
    for j in range(1, 11):
        try:
            b5[j - 1].append(str(b11[f'comment{j}'].values[0]))
        except:
            b5[j - 1].append('')
for i in range(10):
    b7[f'comment{i+1}'] = b5[i]
b7 = b7[b7['comment1'] != '']
b7 = b7.head(500)
b7.to_csv("./lowstar_reply.b3", b12 = "utf_8_sig", mode='w', index=False)
b13 = b3[b3['star_point'] == 9.99].sample(n=1000)
if 'Unnamed: 0' in b13.columns:
    del b13['Unnamed: 0']
b13 = b13.drop_duplicates(["titleId", "nom"], keep='first')
b14 = list(b13['titleId'])
b15 = list(b13['nom'])
b5 = [[] for _ in range(10)]
for i in range(len(b14)):
    b10 = b4[b4['titleId'] == b14[i]]
    b11 = b10[b10['nom'] == b15[i]]
    for j in range(1, 11):
        try:
            b5[j - 1].append(str(b11[f'comment{j}'].values[0]))
        except:
            b5[j - 1].append('')
for i in range(10):
    b13[f'comment{i+1}'] = b5[i]
b13 = b13[b13['comment1'] != '']
b13 = b13.head(500)
b13.to_csv("./highstar_reply.b3", b12 = "utf_8_sig", mode='w', index=False)
print("Processing complete. CSV files have been saved.")