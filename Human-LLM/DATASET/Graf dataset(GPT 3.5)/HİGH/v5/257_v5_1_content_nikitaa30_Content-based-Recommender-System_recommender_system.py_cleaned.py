import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2():
    return TfidfVectorizer(b1 = 'word', ngram_range=(1, 3), min_df=0, stop_words='english')
def fonk3(b9):
    return linear_kernel(b9, b9)
def fonk4(b7, b10):
    b2 = {}
    for idx, row in b7.iterrows():
        b3 = b10[idx].argsort()[:-100:-1]
        b4 = [(b10[idx][i], b7['id'][i]) for i in b3]
        b2[row['id']] = b4[1:]
    return b2
def fonk5(b7, b11):
    return b7.loc[b7['id'] == b11]['description'].tolist()[0].split(' - ')[0]
def fonk6(b11, num_recommendations, b7, b2):
    print("Recommending {} products similar to {}...".format(num_recommendations, fonk5(b7, b11)))
    print("-------")
    b5 = b2[b11][:num_recommendations]
    for rec in b5:
        print("Recommended: {} (score:{})".format(fonk5(b7, rec[1]), rec[0]))
def fonk7():
    b6 = "/home/nikita/Downloads/sample-b7.csv"
    b7 = fonk1(b6)
    b8 = fonk2()
    b9 = b8.fit_transform(b7['description'])
    b10 = fonk3(b9)
    b2 = fonk4(b7, b10)
    print('Recommendation system setup is complete!\n')
    fonk6(b11 = 11, num_recommendations=5, b7=b7, b2=b2)
if b12 = = "__main__":
    fonk7()