import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
def read_documents(docs_dir):
    documents = []
    for book in os.listdir(docs_dir):
        if not book.startswith('.'):
            with open(os.path.join(docs_dir, book), 'rb') as f:
                content = f.read().decode('utf-8', errors='replace')
                documents.append(content)
    return documents
def extract_title_author(content):
    lines = content.splitlines()
    title = next((line[7:] for line in lines[:80] if line.startswith("Title: ")), None)
    author = next((line[8:] for line in lines[:80] if line.startswith("Author: ")), None)
    return title, author
def build_database(tfidf_matrix, feature_names, title_author_store):
    database = {}
    for i in range(tfidf_matrix.shape[0]):
        doc = tfidf_matrix[i].toarray()[0]
        phrase_scores = [(index, score) for index, score in enumerate(doc) if score > 0]
        sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1], reverse=True)
        local_word_dict = {feature_names[pair[0]]: pair[1] for pair in sorted_phrase_scores}
        database[title_author_store[i]] = local_word_dict
    return database
def insert_into_mongodb(database):
    client = MongoClient()
    db = client.bookdb
    posts = db.posts
    for (title, author), word_dict in database.items():
        try:
            post = {"title_id_0011": title, "author_id_0011": author}
            post.update(word_dict)
            post_id = posts.insert_one(post).inserted_id
        except Exception as e:
            print(f"{title}, {author} failed: {e}")
def main():
    docs_dir = "/Users/jamesledoux/Documents/Drew2"
    documents = read_documents(docs_dir)
    tfidf = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode', analyzer='word')
    tfidf_matrix = tfidf.fit_transform(documents)
    feature_names = tfidf.get_feature_names_out()
    title_author_store = [extract_title_author(content) for content in documents]
    database = build_database(tfidf_matrix, feature_names, title_author_store)
    insert_into_mongodb(database)
    print("Data insertion complete.")
if __name__ == "__main__":
    main()