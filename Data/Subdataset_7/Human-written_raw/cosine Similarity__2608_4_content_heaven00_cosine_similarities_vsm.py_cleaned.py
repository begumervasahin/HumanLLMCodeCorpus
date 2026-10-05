
import pandas as pd
from sklearn.b7.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def fonk1(b6, b7, b8):
    b1 = []
    for tweet in b6:
        b2 = {tweet:[]}
        b3 = b7.transform([tweet])
        b4 = linear_kernel(b3, b8).flatten()
        b5 = b4.argsort()[:-5:-1]
        for b11 in b5:
            b2[tweet].append((b6[b11], b4[b11]))
        b1.append(b2)
    return b1
def fonk2():
    b6 = list(open('b6.txt', 'r+'))
    b7 = TfidfVectorizer(analyzer="word")
    b8 = b7.fit_transform(b6)
    b9 = fonk1(b6, b7, b8)
    b10 = {'tweet_one':[], 'tweet_two':[], 'cosine_relation':[]}
    for item in b9:
        for key in item.keys():
            for processed_data in item[key]:
                if key != processed_data[0]:
                    b10['tweet_one'].append(key)
                    b10['tweet_two'].append(processed_data[0])
                    b10['cosine_relation'].append(processed_data[1])
    pd.DataFrame(b10).to_csv('tweet_cosine_similarities.csv', b11 = False)
if b12 = = "__main__":
    fonk2()