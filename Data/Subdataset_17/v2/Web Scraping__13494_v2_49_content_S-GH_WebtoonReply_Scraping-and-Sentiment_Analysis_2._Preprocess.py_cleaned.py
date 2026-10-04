import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
csv = pd.read_csv(info_path)
csv2 = pd.read_csv(reply_path)
if 'Unnamed: 0' in csv2.columns:
    csv2.drop(columns=['Unnamed: 0'], inplace=True)
def extract_comments(titleId_list, nom_list, reply_df):
    comments = [[] for _ in range(10)]
    for titleId, nom in zip(titleId_list, nom_list):
        filtered_df = reply_df[(reply_df['titleId'] == titleId) & (reply_df['nom'] == nom)]
        for i in range(1, 11):
            try:
                comments[i - 1].append(str(filtered_df[f'comment{i}'].values[0]))
            except IndexError:
                comments[i - 1].append('')
    return comments
lowstar_csv = csv.sort_values(by='star_point').head(1000).drop_duplicates(["titleId", "nom"], keep='first')
titleId_lowlst = lowstar_csv['titleId'].tolist()
nom_lowlst = lowstar_csv['nom'].tolist()
low_comments = extract_comments(titleId_lowlst, nom_lowlst, csv2)
for i in range(10):
    lowstar_csv[f'comment{i+1}'] = low_comments[i]
lowstar_csv = lowstar_csv[lowstar_csv['comment1'] != ''].head(500)
lowstar_csv.to_csv("./lowstar_reply.csv", encoding="utf_8_sig", index=False)
highstar_csv = csv[csv['star_point'] == 9.99].sample(n=1000)
if 'Unnamed: 0' in highstar_csv.columns:
    highstar_csv.drop(columns=['Unnamed: 0'], inplace=True)
highstar_csv = highstar_csv.drop_duplicates(["titleId", "nom"], keep='first')
titleId_highlst = highstar_csv['titleId'].tolist()
nom_highlst = highstar_csv['nom'].tolist()
high_comments = extract_comments(titleId_highlst, nom_highlst, csv2)
for i in range(10):
    highstar_csv[f'comment{i+1}'] = high_comments[i]
highstar_csv = highstar_csv[highstar_csv['comment1'] != ''].head(500)
highstar_csv.to_csv("./highstar_reply.csv", encoding="utf_8_sig", index=False)
print("Processing complete. CSV files have been saved.")