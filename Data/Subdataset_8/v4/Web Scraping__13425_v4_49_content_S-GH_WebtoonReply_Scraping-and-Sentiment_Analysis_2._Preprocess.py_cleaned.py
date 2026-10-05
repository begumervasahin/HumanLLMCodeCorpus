import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
info_csv = pd.read_csv(info_path)
reply_csv = pd.read_csv(reply_path)
del reply_csv['Unnamed: 0']
reply_list = [[] for _ in range(10)]
info_sorted = info_csv.sort_values(by='star_point', axis=0)
lowstar_info = info_sorted.head(1000).drop_duplicates(["titleId","nom"], keep='first')
titleId_lowlst = lowstar_info['titleId']
nom_lowlst = lowstar_info['nom']
for i, (titleId, nom) in enumerate(zip(titleId_lowlst, nom_lowlst)):
    filtered_reply = reply_csv[(reply_csv['titleId'] == titleId) & (reply_csv['nom'] == nom)]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(filtered_reply[f'comment{j}'].values[0]))
        except IndexError:
            reply_list[j - 1].append('')
for i in range(10):
    lowstar_info[f'comment{i+1}'] = reply_list[i]
lowstar_info = lowstar_info[lowstar_info['comment1'] != '']
lowstar_info = lowstar_info[:500 - len(lowstar_info)]
lowstar_info.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w')
highstar_info = info_csv[info_csv['star_point'] == 9.99].sample(n=1000).drop_duplicates(["titleId","nom"], keep='first')
titleId_highlst = highstar_info['titleId']
nom_highlst = highstar_info['nom']
reply_list = [[] for _ in range(10)]
for i, (titleId, nom) in enumerate(zip(titleId_highlst, nom_highlst)):
    filtered_reply = reply_csv[(reply_csv['titleId'] == titleId) & (reply_csv['nom'] == nom)]
    for j in range(1, 11):
        try:
            reply_list[j - 1].append(str(filtered_reply[f'comment{j}'].values[0]))
        except IndexError:
            reply_list[j - 1].append('')
for i in range(10):
    highstar_info[f'comment{i+1}'] = reply_list[i]
highstar_info = highstar_info[highstar_info['comment1'] != '']
highstar_info = highstar_info[:500 - len(highstar_info)]
highstar_info.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w')