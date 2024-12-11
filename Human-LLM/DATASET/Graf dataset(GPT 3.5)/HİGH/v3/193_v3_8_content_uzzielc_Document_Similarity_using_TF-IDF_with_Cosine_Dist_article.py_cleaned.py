import numpy as np
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def fonk1(file_path):
    return pd.read_csv(file_path)
def fonk2(texts):
    nltk.download('punkt')
    return [nltk.word_tokenize(article) for article in texts]
def fonk3(texts, b5):
    b1 = CountVectorizer(stop_words='english')
    b1.fit_transform([b5])
    b2 = b1.transform(texts)
    b3 = TfidfTransformer(norm="l2")
    b3.fit(b2)
    return b3.transform(b2)
def fonk4(b7):
    return cosine_similarity(b7[0:1], b7)
def fonk5():
    b4 = fonk1('article_data.csv')
    b5 = b4.content.iloc[0]
    b6 = fonk2(b4.content)
    b7 = fonk3(b6, b5)
    b8 = fonk4(b7)
    b9 = pd.DataFrame(b8[0], columns=['Cosine_Similarity'])
    b10 = pd.concat([b4, b9], axis=1)
    b11 = b10.sort_values(by='Cosine_Similarity', ascending=False)
    print(b11.head(6))
if b12 = = "__main__":
    fonk5()