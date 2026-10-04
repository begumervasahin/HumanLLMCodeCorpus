import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
df_articles = pd.read_csv('article_data.csv')
target_text = df_articles.content.iloc[0]
texts = df_articles.content.tolist()
vectorizer = CountVectorizer(stop_words='english')
vectorizer.fit_transform([target_text])
freq_term_matrix = vectorizer.transform(texts)
tfidf_transformer = TfidfTransformer(norm="l2")
tfidf_transformer.fit(freq_term_matrix)
tf_idf_matrix = tfidf_transformer.transform(freq_term_matrix)
cosine_similarities = cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix)
cos_sim_df = pd.DataFrame(cosine_similarities[0], columns=['Cos_Sim'])
df_final = pd.concat([df_articles, cos_sim_df], axis=1)
df_final_sorted = df_final.sort_values(by='Cos_Sim', ascending=False)
print(df_final_sorted.head(6))