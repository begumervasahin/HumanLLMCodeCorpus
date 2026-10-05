import pandas as pd
def read_csv(file_path):
    return pd.read_csv(file_path).drop(columns=['Unnamed: 0'], errors='ignore')
info_csv = read_csv('path/to/weebtoon_star_info.csv')
reply_csv = read_csv('path/to/weebtoon_reply_info.csv')
def extract_comments(csv, titles, noms):
    comments = [[] for _ in range(10)]
    for title, nom in zip(titles, noms):
        filtered_data = csv[(csv['titleId'] == title) & (csv['nom'] == nom)]
        for j in range(1, 11):
            try:
                comments[j - 1].append(str(filtered_data[f'comment{j}'].values[0]))
            except IndexError:
                comments[j - 1].append('')
    return comments
lowstar_sorted = info_csv.sort_values(by='star_point')
lowstar_info = lowstar_sorted.head(1000).drop_duplicates(["titleId", "nom"], keep='first')
lowstar_titles = lowstar_info['titleId']
lowstar_noms = lowstar_info['nom']
lowstar_comments = extract_comments(reply_csv, lowstar_titles, lowstar_noms)
for i, comments in enumerate(lowstar_comments):
    lowstar_info[f'comment{i+1}'] = comments
lowstar_info = lowstar_info[lowstar_info['comment1'] != ''].head(500)
lowstar_info.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", mode='w')
highstar_info = info_csv[info_csv['star_point'] == 9.99].sample(n=1000).drop_duplicates(["titleId", "nom"], keep='first')
highstar_titles = highstar_info['titleId']
highstar_noms = highstar_info['nom']
highstar_comments = extract_comments(reply_csv, highstar_titles, highstar_noms)
for i, comments in enumerate(highstar_comments):
    highstar_info[f'comment{i+1}'] = comments
highstar_info = highstar_info[highstar_info['comment1'] != ''].head(500)
highstar_info.to_csv("./highstar_reply.csv", encoding="utf_8_sig", mode='w')