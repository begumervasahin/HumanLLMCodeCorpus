import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = "/home/nikita/Downloads/sample-data.csv"
b2 = pd.read_csv(b1)
b3 = TfidfVectorizer(
    b4 = 'word',
    b5 = (1, 3),
    b6 = 0,
    b7 = 'english'
)
b8 = b3.fit_transform(b2['b13'])
b9 = linear_kernel(b8, b8)
b10 = {}
for idx, row in b2.iterrows():
    b11 = b9[idx].argsort()[:-100:-1]
    b12 = [
        (b9[idx][i], b2['id'][i])
        for i in b11
    ]
    b10[row['id']] = b12[1:]
print('done!')
def fonk1(b15):
    b13 = b2.loc[b2['id'] == b15, 'b13'].values[0]
    return b13.split(' - ')[0]
def fonk2(b15, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to {fonk1(b15)}...")
    print("-------")
    b14 = b10[b15][:num_recommendations]
    for score, recommended_item_id in b14:
        print(f"Recommended: {fonk1(recommended_item_id)} (score: {score})")
fonk2(b15 = 11, num_recommendations=5)