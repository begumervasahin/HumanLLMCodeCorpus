import numpy as np
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def load_article_data(file_path):
    return pd.read_csv(file_path)
def tokenize_and_preprocess(texts):
    nltk.download('punkt')
    return [nltk.word_tokenize(article) for article in texts]
def compute_tf_idf_matrix(texts, target_text):
    vectorizer = CountVectorizer(stop_words='english')
    vectorizer.fit_transform([target_text])
    frequency_term_matrix = vectorizer.transform(texts)
    tfidf_transformer = TfidfTransformer(norm="l2")
    tfidf_transformer.fit(frequency_term_matrix)
    return tfidf_transformer.transform(frequency_term_matrix)
def compute_cosine_similarity(tf_idf_matrix):
    return cosine_similarity(tf_idf_matrix[0:1], tf_idf_matrix)
def main():
    df_articles = load_article_data('article_data.csv')
    target_text = df_articles.content.iloc[0]
    tokenized_texts = tokenize_and_preprocess(df_articles.content)
    tf_idf_matrix = compute_tf_idf_matrix(tokenized_texts, target_text)
    cosine_similarities = compute_cosine_similarity(tf_idf_matrix)
    cos_sim_df = pd.DataFrame(cosine_similarities[0], columns=['Cosine_Similarity'])
    df_final = pd.concat([df_articles, cos_sim_df], axis=1)
    df_final_sorted = df_final.sort_values(by='Cosine_Similarity', ascending=False)
    print(df_final_sorted.head(6))
if __name__ == "__main__":
    main()