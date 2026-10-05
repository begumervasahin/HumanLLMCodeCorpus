import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df_articles = pd.read_csv('article_data.csv')
target_text = df_articles.content.iloc[0]
texts = [article for article in df_articles.content]
vectorizer = CountVectorizer(stop_words='english')
vectorizer.fit_transform([target_text])
frequency_term_matrix = vectorizer.transform(texts)
tfidf_transformer = TfidfTransformer(norm="l2")
tfidf_transformer.fit(frequency_term_matrix)
tf_idf_matrix = tfidf_transformer.transform(frequency_term_matrix)
cos_sim_vec = cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix)
cos_sim_df = pd.DataFrame(cos_sim_vec[0], columns=['Cosine_Similarity'])
df_final = pd.concat([df_articles, cos_sim_df], axis=1)
df_final_sorted = df_final.sort_values(by='Cosine_Similarity', ascending=False)
print(df_final_sorted.head(6))