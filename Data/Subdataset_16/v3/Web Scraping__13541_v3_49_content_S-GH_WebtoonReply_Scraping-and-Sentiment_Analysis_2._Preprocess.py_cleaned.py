import pandas as pd
b1 = 'path/to/weebtoon_star_info.b3'
b2 = 'path/to/weebtoon_reply_info.b3'
b3 = pd.read_csv(b1)
b4 = pd.read_csv(b2)
b4.drop(b5 = ['Unnamed: 0'], inplace=True, errors='ignore')
def fonk1(b10, b11, reply_df):
    b6 = [[] for _ in range(10)]
    for titleId, nom in zip(b10, b11):
        b7 = reply_df[(reply_df['titleId'] == titleId) & (reply_df['nom'] == nom)]
        for i in range(1, 11):
            try:
                b6[i - 1].append(str(b7[f'comment{i}'].values[0]))
            except IndexError:
                b6[i - 1].append('')
    return b6
def fonk2(b9, star_points, file_name, b8 = False):
    if b8:
        b9 = b9[b9['star_point'] == star_points].sample(n=1000)
    else:
        b9 = b9.sort_values(by='star_point').head(1000)
    b9 = b9.drop_duplicates(["titleId", "nom"], keep='first')
    b10 = b9['titleId'].tolist()
    b11 = b9['nom'].tolist()
    b6 = fonk1(b10, b11, b4)
    for i in range(10):
        b9[f'comment{i+1}'] = b6[i]
    b9 = b9[b9['comment1'] != ''].head(500)
    b9.to_csv(file_name, b12 = "utf_8_sig", index=False)
fonk2(b3, None, "./lowstar_reply.b3")
fonk2(b3, 9.99, "./highstar_reply.b3", b8 = True)
print("Processing complete. CSV files have been saved.")