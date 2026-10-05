import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
csv = pd.read_csv(info_path)
csv2 = pd.read_csv(reply_path)
del csv2['Unnamed: 0']
reply_list = []
for i in range(10):
    reply_list.append([])
csv_sort = csv.sort_values(by='star_point',axis=0)
lowstar_csv = csv_sort[0:1000]
lowstar_csv = lowstar_csv.drop_duplicates(["titleId","nom"],keep='first')
print(lowstar_csv)
titleId_lowlst = list(lowstar_csv['titleId'])
nom_lowlst = list(lowstar_csv['nom'])
for i in range(len(titleId_lowlst)):
    aa = csv2[csv2['titleId'].isin([f'{titleId_lowlst[i]}'])]
    bb = aa[aa['nom'].isin([f'{nom_lowlst[i]}'])]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(bb[f'comment{j}'].values[0]))
        except:
            reply_list[j - 1].append('')
            pass
for i in range(10):
    lowstar_csv[f'comment{i+1}'] = reply_list[i]
idx = lowstar_csv[lowstar_csv['comment1']==''].index
lowstar_csv = lowstar_csv.drop(idx)
print(lowstar_csv)
lowstar_csv = lowstar_csv[:500 - len(lowstar_csv)]
print(lowstar_csv)
lowstar_csv.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w')
highstar_csv = csv[csv['star_point'].isin([9.99])]
highstar_csv = highstar_csv.sample(n=1000)
del highstar_csv['Unnamed: 0']
highstar_csv = highstar_csv.drop_duplicates(["titleId","nom"],keep='first')
titleId_highlst = list(highstar_csv['titleId'])
nom_highlst = list(highstar_csv['nom'])
reply_list = []
for i in range(10):
    reply_list.append([])
for i in range(len(titleId_highlst)):
    aa = csv2[csv2['titleId'].isin([f'{titleId_highlst[i]}'])]
    bb = aa[aa['nom'].isin([f'{nom_highlst[i]}'])]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(bb[f'comment{j}'].values[0]))
        except:
            reply_list[j - 1].append('')
            pass
for i in range(10):
    highstar_csv[f'comment{i+1}'] = reply_list[i]
idx = highstar_csv[highstar_csv['comment1']==''].index
highstar_csv = highstar_csv.drop(idx)
print(highstar_csv)
highstar_csv = highstar_csv[:500 - len(highstar_csv)]
print(highstar_csv)
highstar_csv.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w')