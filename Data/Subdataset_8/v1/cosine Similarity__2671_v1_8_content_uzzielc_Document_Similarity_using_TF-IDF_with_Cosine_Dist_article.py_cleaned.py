import numpy as np
import pandas as pd
import nltk
import string
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df_art = pd.read_csv('article_data.csv')
target_text = df_art.content.iloc[0]
nltk.download('punkt')
text = []
for indx in range(len(df_art)):
    text.append(df_art.content.iloc[indx])
vectorizer = CountVectorizer(stop_words='english')
vectorizer.fit_transform([target_text])
freq_term_matrix = vectorizer.transform(text)
tfidf = TfidfTransformer(norm="l2")
tfidf.fit(freq_term_matrix)
tf_idf_matrix = tfidf.transform(freq_term_matrix)
cos_sim_vec = cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix)
cos_sim_df = pd.DataFrame(cos_sim_vec[0], columns=['Cos_Sim'])
df_final = pd.concat([df_art, cos_sim_df], axis=1)
df_final = df_final.sort_values(by='Cos_Sim', ascending=False)
print(df_final.head(6))