import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from pymongo import MongoClient
def connect_to_mongo():
    client = MongoClient()
    db = client.bookdb
    return db.posts
def read_documents(directory):
    documents = []
    for book in os.listdir(directory):
        if not book.startswith('.'):
            book_path = os.path.join(directory, book)
            with open(book_path, 'rb') as file:
                content = file.read().decode('utf-8', errors='replace')
                documents.append(content)
    return documents
def extract_title_author(directory):
    title_author_store = []
    for book in os.listdir(directory):
        if not book.startswith('.'):
            book_path = os.path.join(directory, book)
            with open(book_path, 'rb') as file:
                content = file.read().decode('utf-8').splitlines()
            title = None
            author = None
            for line in content[:80]:
                if line.startswith("Title: "):
                    title = line[7:].strip()
                elif line.startswith("Author: "):
                    author = line[8:].strip()
            title_author_store.append((title, author))
    return title_author_store
def vectorize_documents(documents):
    tfidf = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode')
    tfidf_matrix = tfidf.fit_transform(documents)
    feature_names = tfidf.get_feature_names_out()
    return tfidf_matrix, feature_names
def build_database(tfidf_matrix, feature_names, title_author_store):
    database = {}
    for i in range(tfidf_matrix.shape[0]):
        doc_vector = tfidf_matrix[i].toarray()[0]
        phrase_scores = [(index, score) for index, score in enumerate(doc_vector) if score > 0]
        sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1], reverse=True)
        word_scores = {feature_names[index]: score for index, score in sorted_phrase_scores}
        database[title_author_store[i]] = word_scores
    return database
def insert_into_mongo(database, posts):
    for (title, author), word_scores in database.items():
        try:
            post = {"title": title, "author": author}
            post.update(word_scores)
            posts.insert_one(post)
        except Exception as e:
            print(f"Failed to insert {title}, {author}: {e}")
if __name__ == "__main__":
    print("Place the documents in the specified directory.")
    docs_dir = "/Users/jamesledoux/Documents/Drew2"
    posts = connect_to_mongo()
    documents = read_documents(docs_dir)
    title_author_store = extract_title_author(docs_dir)
    tfidf_matrix, feature_names = vectorize_documents(documents)
    database = build_database(tfidf_matrix, feature_names, title_author_store)
    insert_into_mongo(database, posts)
    print("Data successfully inserted into MongoDB")