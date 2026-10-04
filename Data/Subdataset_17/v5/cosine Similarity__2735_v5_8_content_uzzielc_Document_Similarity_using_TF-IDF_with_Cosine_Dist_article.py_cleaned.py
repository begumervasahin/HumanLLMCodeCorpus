import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
def load_data(file_path):
    return pd.read_csv(file_path)
def preprocess_texts(df, text_column):
    return df[text_column].tolist()
def compute_tfidf_matrix(texts, stop_words='english'):
    vectorizer = CountVectorizer(stop_words=stop_words)
    freq_term_matrix = vectorizer.fit_transform(texts)
    tfidf_transformer = TfidfTransformer(norm="l2")
    tf_idf_matrix = tfidf_transformer.fit_transform(freq_term_matrix)
    return tf_idf_matrix, vectorizer
def compute_cosine_similarity(tf_idf_matrix, target_index=0):
    return cosine_similarity(tf_idf_matrix[target_index:target_index + 1], tf_idf_matrix)[0]
def add_cosine_similarity_scores(df, cos_sim_scores):
    cos_sim_df = pd.DataFrame(cos_sim_scores, columns=['Cos_Sim'])
    return pd.concat([df, cos_sim_df], axis=1)
def sort_by_cosine_similarity(df):
    return df.sort_values(by='Cos_Sim', ascending=False)
if __name__ == '__main__':
    df_articles = load_data('article_data.csv')
    texts = preprocess_texts(df_articles, 'content')
    tf_idf_matrix, vectorizer = compute_tfidf_matrix(texts, stop_words='english')
    cosine_similarities = compute_cosine_similarity(tf_idf_matrix, target_index=0)
    df_with_scores = add_cosine_similarity_scores(df_articles, cosine_similarities)
    df_final_sorted = sort_by_cosine_similarity(df_with_scores)
    print(df_final_sorted.head(6))