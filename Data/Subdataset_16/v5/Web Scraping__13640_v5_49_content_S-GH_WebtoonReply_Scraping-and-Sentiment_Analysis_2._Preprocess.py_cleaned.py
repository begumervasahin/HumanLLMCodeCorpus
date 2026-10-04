import pandas as pd
def fonk1(b12, b13):
    b1 = pd.read_csv(b12)
    b2 = pd.read_csv(b13).drop(columns=['Unnamed: 0'])
    return b1, b2
def fonk2(b1):
    b3 = b1.sort_values(by='star_point')
    b4 = b3.head(1000).drop_duplicates(subset=["titleId", "nom"])
    return b4
def fonk3(b1):
    b5 = b1[b1['star_point'] == 9.99].sample(n=1000).drop(columns=['Unnamed: 0'])
    b5 = b5.drop_duplicates(subset=["titleId", "nom"])
    return b5
def fonk4(b10, b2):
    b6 = b10['titleId'].tolist()
    b7 = b10['nom'].tolist()
    b8 = [[] for _ in range(10)]
    for title_id, nom in zip(b6, b7):
        b9 = b2[(b2['titleId'] == title_id) & (b2['nom'] == nom)]
        for i in range(10):
            try:
                b8[i].append(str(b9[f'comment{i+1}'].values[0]))
            except IndexError:
                b8[i].append('')
    for i in range(10):
        b10[f'comment{i+1}'] = b8[i]
    b10 = b10[b10['comment1'] != '']
    return b10.head(500)
def fonk5(b10, file_path):
    b10.to_csv(file_path, b11 = "utf_8_sig", mode='w')
def fonk6():
    b12 = 'path/to/weebtoon_star_info.csv'
    b13 = 'path/to/weebtoon_reply_info.csv'
    b1, b2 = fonk1(b12, b13)
    b4 = fonk2(b1)
    print(b4)
    b4 = fonk4(b4, b2)
    print(b4)
    fonk5(b4, "./lowstar_reply.csv")
    b5 = fonk3(b1)
    b5 = fonk4(b5, b2)
    print(b5)
    fonk5(b5, "./highstar_reply.csv")
if b14 = = "__main__":
    fonk6()