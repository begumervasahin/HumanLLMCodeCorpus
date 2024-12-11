import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = "/home/nikita/Downloads/sample-b2.csv"
b2 = pd.read_csv(b1)
b3 = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
b4 = b3.fit_transform(b2['description'])
b5 = linear_kernel(b4, b4)
b6 = {}
for idx, row in b2.iterrows():
    b7 = b5[idx].argsort()[:-1][::-1]
    b8 = [(b5[idx][i], b2.loc[i, 'id']) for i in b7 if i != idx]
    b6[row['id']] = b8
print('Recommendation process completed!')
def fonk1(b11):
    return b2.loc[b2['id'] == b11, 'description'].iloc[0].split(' - ')[0]
def fonk2(b11, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to '{fonk1(b11)}'...")
    print("-------")
    b9 = b6.get(b11, [])
    for idx, (similarity_score, similar_item_id) in enumerate(b9[:num_recommendations], b10 = 1):
        print(f"{idx}. {fonk1(similar_item_id)} (score: {similarity_score:.4f})")
fonk2(b11 = 11, num_recommendations=5)