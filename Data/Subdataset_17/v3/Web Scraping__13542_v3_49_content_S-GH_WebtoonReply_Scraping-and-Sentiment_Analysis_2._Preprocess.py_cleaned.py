import pandas as pd
info_path = 'path/to/weebtoon_star_info.csv'
reply_path = 'path/to/weebtoon_reply_info.csv'
csv = pd.read_csv(info_path)
csv2 = pd.read_csv(reply_path)
csv2.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
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
def process_and_save_csv(df, star_points, file_name, is_high=False):
    if is_high:
        df = df[df['star_point'] == star_points].sample(n=1000)
    else:
        df = df.sort_values(by='star_point').head(1000)
    df = df.drop_duplicates(["titleId", "nom"], keep='first')
    titleId_list = df['titleId'].tolist()
    nom_list = df['nom'].tolist()
    comments = extract_comments(titleId_list, nom_list, csv2)
    for i in range(10):
        df[f'comment{i+1}'] = comments[i]
    df = df[df['comment1'] != ''].head(500)
    df.to_csv(file_name, encoding="utf_8_sig", index=False)
process_and_save_csv(csv, None, "./lowstar_reply.csv")
process_and_save_csv(csv, 9.99, "./highstar_reply.csv", is_high=True)
print("Processing complete. CSV files have been saved.")