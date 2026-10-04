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
    b7 = b5[idx].argsort()[:-100:-1]
    b8 = [(b5[idx][i], b2['id'][i]) for i in b7]
    b6[row['id']] = b8[1:]
print('Processing complete!')
def fonk1(b10):
    return b2.loc[b2['id'] == b10]['description'].values[0]
def fonk2(b10, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to {fonk1(b10)}...")
    print("-------")
    b9 = b6[b10][:num_recommendations]
    for score, recommended_item_id in b9:
        print(f"Recommended: {fonk1(recommended_item_id)} (score: {score:.4f})")
fonk2(b10 = 11, num_recommendations=5)