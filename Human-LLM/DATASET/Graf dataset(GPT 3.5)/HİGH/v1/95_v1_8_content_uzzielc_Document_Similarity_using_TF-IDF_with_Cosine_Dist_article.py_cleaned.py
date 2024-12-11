import numpy as np
import pandas as pd
import nltk
import string
from sklearn.feature_extraction.b3 import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
b1 = pd.read_csv('article_data.csv')
b2 = b1.content.iloc[0]
nltk.download('punkt')
b3 = []
for indx in range(len(b1)):
    b3.append(b1.content.iloc[indx])
b4 = CountVectorizer(stop_words='english')
b4.fit_transform([b2])
b5 = b4.transform(b3)
b6 = TfidfTransformer(norm="l2")
b6.fit(b5)
b7 = b6.transform(b5)
b8 = cosine_similarity(b7[0:1], b7)
b9 = pd.DataFrame(b8[0], columns=['Cos_Sim'])
b10 = pd.concat([b1, b9], axis=1)
b10 = b10.sort_values(by='Cos_Sim', ascending=False)
print(b10.head(6))