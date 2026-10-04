import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(df, text_column):
    return df[text_column].tolist()
def fonk3(b13, b1 = 'english'):
    b2 = CountVectorizer(b1=b1)
    b3 = b2.fit_transform(b13)
    b4 = TfidfTransformer(norm="l2")
    b4.fit(b3)
    b5 = b4.transform(b3)
    return b5
def fonk4(b5, b6 = 0):
    b7 = cosine_similarity(b5[b6:b6 + 1], b5)
    return b7[0]
def fonk5(df, b14):
    b8 = pd.DataFrame(b14, columns=['Cos_Sim'])
    b9 = pd.concat([df, b8], axis=1)
    b10 = b9.sort_values(by='Cos_Sim', ascending=False)
    return b10
if b11 = = '__main__':
    b12 = fonk1('article_data.csv')
    b13 = fonk2(b12, text_column='content')
    b5 = fonk3(b13, b1='english')
    b14 = fonk4(b5, b6=0)
    b15 = fonk5(b12, b14)
    print(b15.head(6))