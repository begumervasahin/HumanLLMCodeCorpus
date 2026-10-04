import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
csv = pd.read_csv(info_path)
csv2 = pd.read_csv(reply_path)
if 'Unnamed: 0' in csv2.columns:
    del csv2['Unnamed: 0']
reply_list = [[] for _ in range(10)]
csv_sort = csv.sort_values(by='star_point', axis=0)
lowstar_csv = csv_sort.head(1000).drop_duplicates(["titleId", "nom"], keep='first')
titleId_lowlst = list(lowstar_csv['titleId'])
nom_lowlst = list(lowstar_csv['nom'])
for i in range(len(titleId_lowlst)):
    aa = csv2[csv2['titleId'] == titleId_lowlst[i]]
    bb = aa[aa['nom'] == nom_lowlst[i]]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(bb[f'comment{j}'].values[0]))
        except:
            reply_list[j - 1].append('')
for i in range(10):
    lowstar_csv[f'comment{i+1}'] = reply_list[i]
lowstar_csv = lowstar_csv[lowstar_csv['comment1'] != '']
lowstar_csv = lowstar_csv.head(500)
lowstar_csv.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w', index=False)
highstar_csv = csv[csv['star_point'] == 9.99].sample(n=1000)
if 'Unnamed: 0' in highstar_csv.columns:
    del highstar_csv['Unnamed: 0']
highstar_csv = highstar_csv.drop_duplicates(["titleId", "nom"], keep='first')
titleId_highlst = list(highstar_csv['titleId'])
nom_highlst = list(highstar_csv['nom'])
reply_list = [[] for _ in range(10)]
for i in range(len(titleId_highlst)):
    aa = csv2[csv2['titleId'] == titleId_highlst[i]]
    bb = aa[aa['nom'] == nom_highlst[i]]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(bb[f'comment{j}'].values[0]))
        except:
            reply_list[j - 1].append('')
for i in range(10):
    highstar_csv[f'comment{i+1}'] = reply_list[i]
highstar_csv = highstar_csv[highstar_csv['comment1'] != '']
highstar_csv = highstar_csv.head(500)
highstar_csv.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w', index=False)
print("Processing complete. CSV files have been saved.")