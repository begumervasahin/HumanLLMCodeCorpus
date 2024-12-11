import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("/home/nikita/Downloads/sample-data.csv")
b2 = TfidfVectorizer(
    b3 = 'word',
    b4 = (1, 3),
    b5 = 0,
    b6 = 'english'
)
b7 = b2.fit_transform(b1['description'])
b8 = linear_kernel(b7, b7)
b9 = {}
for idx, row in b1.iterrows():
    b10 = b8[idx].argsort()[:-100:-1]
    b11 = [(b8[idx][i], b1.loc[i, 'id']) for i in b10]
    b9[row['id']] = b11[1:]
print('Similarity computation done!')
def fonk1(b13):
    return b1.loc[b1['id'] == b13, 'description'].iloc[0].split(' - ')[0]
def fonk2(b13, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to {fonk1(b13)}...")
    print("-------")
    b12 = b9[b13][:num_recommendations]
    for score, rec_item_id in b12:
        print(f"Recommended: {fonk1(rec_item_id)} (score: {score})")
fonk2(b13 = 11, num_recommendations=5)