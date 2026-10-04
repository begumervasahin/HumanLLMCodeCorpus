import pandas as pd
b1 = 'path/to/weebtoon_star_info.b3'
b2 = 'path/to/weebtoon_reply_info.b3'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
if 'Unnamed: 0' in b4.b5:
    b4.drop(b5 = ['Unnamed: 0'], inplace=True)
def fonk1(titleId_list, nom_list, reply_df):
    b6 = [[] for _ in range(10)]
    for titleId, nom in zip(titleId_list, nom_list):
        b7 = reply_df[(reply_df['titleId'] == titleId) & (reply_df['nom'] == nom)]
        for i in range(1, 11):
            try:
                b6[i - 1].append(str(b7[f'comment{i}'].values[0]))
            except IndexError:
                b6[i - 1].append('')
    return b6
b8 = b3.sort_values(by='star_point').head(1000).drop_duplicates(["titleId", "nom"], keep='first')
b9 = b8['titleId'].tolist()
b10 = b8['nom'].tolist()
b11 = fonk1(b9, b10, b4)
for i in range(10):
    b8[f'comment{i+1}'] = b11[i]
b8 = b8[b8['comment1'] != ''].head(500)
b8.to_csv("./lowstar_reply.b3", b12 = "utf_8_sig", index=False)
b13 = b3[b3['star_point'] == 9.99].sample(n=1000)
if 'Unnamed: 0' in b13.b5:
    b13.drop(b5 = ['Unnamed: 0'], inplace=True)
b13 = b13.drop_duplicates(["titleId", "nom"], keep='first')
b14 = b13['titleId'].tolist()
b15 = b13['nom'].tolist()
b16 = fonk1(b14, b15, b4)
for i in range(10):
    b13[f'comment{i+1}'] = b16[i]
b13 = b13[b13['comment1'] != ''].head(500)
b13.to_csv("./highstar_reply.b3", b12 = "utf_8_sig", index=False)
print("Processing complete. CSV files have been saved.")