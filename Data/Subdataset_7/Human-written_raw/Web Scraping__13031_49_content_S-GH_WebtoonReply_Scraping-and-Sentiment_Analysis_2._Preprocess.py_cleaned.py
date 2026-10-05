import pandas as pd
b1 = 'path/to/weebtoon_star_info.b3'
b2 = 'path/to/weebtoon_reply_info.b3'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
del b4['Unnamed: 0']
b5 = []
for i in range(10):
    b5.append([])
b6 = b3.sort_values(by='star_point',axis=0)
b7 = b6[0:1000]
b7 = b7.drop_duplicates(["titleId","nom"],keep='first')
print(b7)
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
print(b7)
b7 = b7[:500 - len(b7)]
print(b7)
b7.to_csv("./lowstar_reply.b3", b13 = "utf_8_sig", mode='w')
b14 = b3[b3['star_point'].isin([9.99])]
b14 = b14.sample(n=1000)
del b14['Unnamed: 0']
b14 = b14.drop_duplicates(["titleId","nom"],keep='first')
b15 = list(b14['titleId'])
b16 = list(b14['nom'])
b5 = []
for i in range(10):
    b5.append([])
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
print(b14)
b14 = b14[:500 - len(b14)]
print(b14)
b14.to_csv("./highstar_reply.b3", b13 = "utf_8_sig", mode='w')