import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
info_df = pd.read_csv(info_path)
reply_df = pd.read_csv(reply_path)
reply_df = reply_df.drop(columns=['Unnamed: 0'])
reply_list = [[] for _ in range(10)]
sorted_info_df = info_df.sort_values(by='star_point')
low_star_df = sorted_info_df.head(1000).drop_duplicates(subset=["titleId", "nom"])
print(low_star_df)
low_star_title_ids = low_star_df['titleId'].tolist()
low_star_noms = low_star_df['nom'].tolist()
for title_id, nom in zip(low_star_title_ids, low_star_noms):
    filtered_replies = reply_df[(reply_df['titleId'] == title_id) & (reply_df['nom'] == nom)]
    for i in range(10):
        try:
            reply_list[i].append(str(filtered_replies[f'comment{i+1}'].values[0]))
        except IndexError:
            reply_list[i].append('')
for i in range(10):
    low_star_df[f'comment{i+1}'] = reply_list[i]
low_star_df = low_star_df[low_star_df['comment1'] != '']
print(low_star_df)
low_star_df = low_star_df.head(500)
print(low_star_df)
low_star_df.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w')
high_star_df = info_df[info_df['star_point'] == 9.99].sample(n=1000).drop(columns=['Unnamed: 0'])
high_star_df = high_star_df.drop_duplicates(subset=["titleId", "nom"])
high_star_title_ids = high_star_df['titleId'].tolist()
high_star_noms = high_star_df['nom'].tolist()
reply_list = [[] for _ in range(10)]
for title_id, nom in zip(high_star_title_ids, high_star_noms):
    filtered_replies = reply_df[(reply_df['titleId'] == title_id) & (reply_df['nom'] == nom)]
    for i in range(10):
        try:
            reply_list[i].append(str(filtered_replies[f'comment{i+1}'].values[0]))
        except IndexError:
            reply_list[i].append('')
for i in range(10):
    high_star_df[f'comment{i+1}'] = reply_list[i]
high_star_df = high_star_df[high_star_df['comment1'] != '']
print(high_star_df)
high_star_df = high_star_df.head(500)
print(high_star_df)
high_star_df.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w')