import pandas as pd
def fonk1():
    b1 = 'path/to/weebtoon_star_info.csv'
    b2 = 'path/to/weebtoon_reply_info.csv'
    b3 = pd.read_csv(b1)
    b4 = pd.read_csv(b2)
    b4.drop(b5 = ['Unnamed: 0'], inplace=True)
    b6 = [[] for _ in range(10)]
    b7 = fonk2(b3, b4, 1000, 9.99)
    fonk3(b7, "./lowstar_reply.csv")
    b8 = fonk2(b3, b4, 1000, 9.99)
    fonk3(b8, "./highstar_reply.csv")
def fonk2(b3, b4, num_webtoons, star_threshold):
    b9 = b3.sort_values(by='star_point', axis=0)
    b10 = b9[:num_webtoons].drop_duplicates(["titleId", "nom"], keep='first')
    b11 = list(b10['titleId'])
    b12 = list(b10['nom'])
    b6 = [[] for _ in range(10)]
    for i in range(len(b11)):
        b13 = b4[b4['titleId'].isin([f'{b11[i]}'])]
        b14 = b13[b13['nom'].isin([f'{b12[i]}'])]
        for j in range(1, 11):
            try:
                b6[j - 1].append(str(b14[f'comment{j}'].values[0]))
            except:
                b6[j - 1].append('')
                pass
    for i in range(10):
        b10[f'comment{i+1}'] = b6[i]
    b15 = b10[b10['comment1']==''].index
    b10 = b10.drop(b15)
    b10 = b10[:500 - len(b10)]
    return b10
def fonk3(dataframe, filename):
    dataframe.to_csv(filename, b16 = "utf_8_sig", mode='w', index=False)
if b17 = = "__main__":
    fonk1()