import pandas as pd
def fonk1():
    b1 = 'path/to/weebtoon_star_info.csv'
    b2 = 'path/to/weebtoon_reply_info.csv'
    b3 = pd.read_csv(b1)
    b4 = pd.read_csv(b2)
    del b4['Unnamed: 0']
    b5 = [[] for _ in range(10)]
    b6 = b3.sort_values(by='star_point', axis=0)
    b7 = b6[:1000].drop_duplicates(["titleId", "nom"], keep='first')
    b8 = list(b7['titleId'])
    b9 = list(b7['nom'])
    for i in range(len(b8)):
        b10 = b4[b4['titleId'].isin([f'{b8[i]}'])]
        b11 = b10[b10['nom'].isin([f'{b9[i]}'])]
        for j in range(1, 11):
            try:
                b5[j - 1].append(str(b11[f'comment{j}'].values[0]))
            except:
                b5[j - 1].append('')
                pass
    for i in range(10):
        b7[f'comment{i+1}'] = b5[i]
    b12 = b7[b7['comment1']==''].index
    b7 = b7.drop(b12)
    b7 = b7[:500 - len(b7)]
    b7.to_csv("./lowstar_reply.csv", b13 = "utf_8_sig", mode='w', index=False)
    b14 = b3[b3['star_point'].isin([9.99])].sample(n=1000).drop_duplicates(["titleId", "nom"], keep='first')
    b5 = [[] for _ in range(10)]
    b15 = list(b14['titleId'])
    b16 = list(b14['nom'])
    for i in range(len(b15)):
        b10 = b4[b4['titleId'].isin([f'{b15[i]}'])]
        b11 = b10[b10['nom'].isin([f'{b16[i]}'])]
        for j in range(1, 11):
            try:
                b5[j - 1].append(str(b11[f'comment{j}'].values[0]))
            except:
                b5[j - 1].append('')
                pass
    for i in range(10):
        b14[f'comment{i+1}'] = b5[i]
    b12 = b14[b14['comment1']==''].index
    b14 = b14.drop(b12)
    b14 = b14[:500 - len(b14)]
    b14.to_csv("./highstar_reply.csv", b13 = "utf_8_sig", mode='w', index=False)
if b17 = = "__main__":
    fonk1()