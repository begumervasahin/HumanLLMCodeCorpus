import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(df, text_column):
    return df[text_column].tolist()
def fonk3(b12, b1 = 'english'):
    b2 = CountVectorizer(b1=b1)
    b3 = b2.fit_transform(b12)
    b4 = TfidfTransformer(norm="l2")
    b5 = b4.fit_transform(b3)
    return b5, b2
def fonk4(b5, b6 = 0):
    return cosine_similarity(b5[b6:b6 + 1], b5)[0]
def fonk5(df, cos_sim_scores):
    b7 = pd.DataFrame(cos_sim_scores, columns=['Cos_Sim'])
    return pd.concat([df, b7], b8 = 1)
def fonk6(df):
    return df.sort_values(b9 = 'Cos_Sim', ascending=False)
if b10 = = '__main__':
    b11 = fonk1('article_data.csv')
    b12 = fonk2(b11, 'content')
    b5, b2 = fonk3(b12, b1='english')
    b13 = fonk4(b5, b6=0)
    b14 = fonk5(b11, b13)
    b15 = fonk6(b14)
    print(b15.head(6))