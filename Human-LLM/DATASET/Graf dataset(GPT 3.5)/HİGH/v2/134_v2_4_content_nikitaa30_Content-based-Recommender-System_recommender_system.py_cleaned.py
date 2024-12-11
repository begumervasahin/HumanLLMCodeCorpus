import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
b1 = pd.read_csv("/home/nikita/Downloads/sample-data.csv")
b2 = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
b3 = b2.fit_transform(b1['description'])
b4 = linear_kernel(b3, b3)
b5 = {}
for idx, row in b1.iterrows():
    b6 = b4[idx].argsort()[:-100:-1]
    b7 = [(b4[idx][i], b1['id'][i]) for i in b6]
    b5[row['id']] = b7[1:]
print('Similarity computation done!')
def fonk1(b9):
    return b1.loc[b1['id'] == b9]['description'].tolist()[0].split(' - ')[0]
def fonk2(b9, num_recommendations):
    print("Recommending " + str(num_recommendations) + " products similar to " + fonk1(b9) + "...")
    print("-------")
    b8 = b5[b9][:num_recommendations]
    for recommendation in b8:
        print("Recommended: " + fonk1(recommendation[1]) + " (score:" + str(recommendation[0]) + ")")
fonk2(b9 = 11, num_recommendations=5)