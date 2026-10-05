import numpy as np
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
b1 = pd.read_csv('article_data.csv')
b2 = b1.content.iloc[0]
nltk.download('punkt')
b3 = [article for article in b1.content]
b4 = CountVectorizer(stop_words='english')
b4.fit_transform([b2])
b5 = b4.transform(b3)
b6 = TfidfTransformer(norm="l2")
b6.fit(b5)
b7 = b6.transform(b5)
b8 = cosine_similarity(b7[0:1], b7)
b9 = pd.DataFrame(b8[0], columns=['Cosine_Similarity'])
b10 = pd.concat([b1, b9], axis=1)
b11 = b10.sort_values(by='Cosine_Similarity', ascending=False)
print(b11.head(6))