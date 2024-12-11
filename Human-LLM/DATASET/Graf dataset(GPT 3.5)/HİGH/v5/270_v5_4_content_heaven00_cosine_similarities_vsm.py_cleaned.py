import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def fonk1(b6, b7, tdm):
    b1 = []
    for tweet in b6:
        b2 = []
        b3 = b7.transform([tweet])
        b4 = linear_kernel(b3, tdm).flatten()
        b5 = b4.argsort()[:-5:-1]
        for b12 in b5:
            b2.append((b6[b12], b4[b12]))
        b1.append({tweet: b2})
    return b1
def fonk2():
    with open('b6.txt', 'r') as file:
        b6 = file.readlines()
    b7 = TfidfVectorizer(analyzer="word")
    b8 = b7.fit_transform(b6)
    b9 = fonk1(b6, b7, b8)
    b10 = {'tweet_one': [], 'tweet_two': [], 'cosine_similarity': []}
    for tweet_map in b9:
        for tweet, b2 in tweet_map.items():
            for related_tweet, cosine_similarity in b2:
                if tweet != related_tweet:
                    b10['tweet_one'].append(tweet)
                    b10['tweet_two'].append(related_tweet)
                    b10['cosine_similarity'].append(cosine_similarity)
    b11 = pd.DataFrame(b10)
    b11.to_csv('tweet_cosine_similarities.csv', b12 = False)
if b13 = = "__main__":
    fonk2()