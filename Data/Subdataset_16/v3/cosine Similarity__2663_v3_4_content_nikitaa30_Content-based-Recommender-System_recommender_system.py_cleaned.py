import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def fonk1(path):
    return pd.read_csv(path)
def fonk2(b7, column):
    b1 = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    return b1.fit_transform(b7[column]), b1
def fonk3(tfidf_matrix):
    return linear_kernel(tfidf_matrix, tfidf_matrix)
def fonk4(b7, b9):
    b2 = {}
    for idx, row in b7.iterrows():
        b3 = b9[idx].argsort()[:-100:-1]
        b4 = [(b9[idx][i], b7['id'][i]) for i in b3]
        b2[row['id']] = b4[1:]
    return b2
def fonk5(b7, b11):
    return b7.loc[b7['id'] == b11]['description'].values[0]
def fonk6(b7, b2, b11, num_recommendations):
    print(f"Recommending {num_recommendations} products similar to '{fonk5(b7, b11)}'...")
    print("-------")
    b5 = b2[b11][:num_recommendations]
    for score, recommended_item_id in b5:
        print(f"Recommended: '{fonk5(b7, recommended_item_id)}' (score: {score:.4f})")
def fonk7():
    b6 = "/home/nikita/Downloads/sample-b7.csv"
    b7 = fonk1(b6)
    tfidf_matrix, b8 = fonk2(b7, 'description')
    b9 = fonk3(tfidf_matrix)
    b10 = fonk4(b7, b9)
    print('Processing complete!')
    fonk6(b7, b10, b11 = 11, num_recommendations=5)
if b12 = = "__main__":
    fonk7()