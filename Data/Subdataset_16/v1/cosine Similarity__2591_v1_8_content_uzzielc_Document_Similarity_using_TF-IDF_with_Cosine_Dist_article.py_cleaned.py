import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(df, text_column):
    return df[text_column].tolist()
def fonk3(df, b1 = 0, text_column='content', stop_words='english'):
    b2 = fonk2(df, text_column)
    b3 = b2[b1]
    b4 = CountVectorizer(stop_words=stop_words)
    b5 = b4.fit_transform(b2)
    b6 = TfidfTransformer(norm="l2")
    b6.fit(b5)
    b7 = b6.transform(b5)
    b8 = cosine_similarity(b7[b1:b1 + 1], b7)
    b9 = b8[0]
    b10 = pd.DataFrame(b9, columns=['Cos_Sim'])
    b11 = pd.concat([df, b10], axis=1)
    b12 = b11.sort_values(by='Cos_Sim', ascending=False)
    return b12
if b13 = = '__main__':
    b14 = fonk1('article_data.csv')
    b15 = fonk3(b14, b1=0, text_column='content', stop_words='english')
    print(b15.head(6))