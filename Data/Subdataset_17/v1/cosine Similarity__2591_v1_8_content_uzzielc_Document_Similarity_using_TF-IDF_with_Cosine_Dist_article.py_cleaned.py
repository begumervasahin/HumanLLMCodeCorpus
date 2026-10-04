import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
def load_data(file_path):
    return pd.read_csv(file_path)
def preprocess_texts(df, text_column):
    return df[text_column].tolist()
def compute_cosine_similarity(df, target_index=0, text_column='content', stop_words='english'):
    texts = preprocess_texts(df, text_column)
    target_text = texts[target_index]
    vectorizer = CountVectorizer(stop_words=stop_words)
    freq_term_matrix = vectorizer.fit_transform(texts)
    tfidf_transformer = TfidfTransformer(norm="l2")
    tfidf_transformer.fit(freq_term_matrix)
    tf_idf_matrix = tfidf_transformer.transform(freq_term_matrix)
    cos_sim_matrix = cosine_similarity(tf_idf_matrix[target_index:target_index + 1], tf_idf_matrix)
    cos_sim_scores = cos_sim_matrix[0]
    cos_sim_df = pd.DataFrame(cos_sim_scores, columns=['Cos_Sim'])
    df_with_cos_sim = pd.concat([df, cos_sim_df], axis=1)
    df_sorted = df_with_cos_sim.sort_values(by='Cos_Sim', ascending=False)
    return df_sorted
if __name__ == '__main__':
    df_articles = load_data('article_data.csv')
    df_result = compute_cosine_similarity(df_articles, target_index=0, text_column='content', stop_words='english')
    print(df_result.head(6))