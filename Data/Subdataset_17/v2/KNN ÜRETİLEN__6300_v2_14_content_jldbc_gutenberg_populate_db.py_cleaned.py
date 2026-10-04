from sklearn.feature_extraction.text import TfidfVectorizer
import os
import numpy as np
from pymongo import MongoClient
client = MongoClient()
db = client.bookdb
posts = db.posts
docs_dir = "/Users/jamesledoux/Documents/Drew2"
documents = []
for book in os.listdir(docs_dir):
    if not book.startswith('.'):
        book_path = os.path.join(docs_dir, book)
        with open(book_path, 'rb') as file:
            content = file.read().decode('utf-8', errors='replace')
            documents.append(content)
tfidf = TfidfVectorizer(max_df=0.9, ngram_range=(1, 1), stop_words='english', strip_accents='unicode')
tfidf_matrix = tfidf.fit_transform(documents)
feature_names = tfidf.get_feature_names_out()
title_author_store = []
for book in os.listdir(docs_dir):
    if not book.startswith('.'):
        book_path = os.path.join(docs_dir, book)
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
database = {}
for i in range(tfidf_matrix.shape[0]):
    doc_vector = tfidf_matrix[i].toarray()[0]
    phrase_scores = [(index, score) for index, score in enumerate(doc_vector) if score > 0]
    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1], reverse=True)
    word_scores = {feature_names[index]: score for index, score in sorted_phrase_scores}
    database[title_author_store[i]] = word_scores
for title, author in database.keys():
    try:
        post = {"title": title, "author": author}
        post.update(database[(title, author)])
        posts.insert_one(post)
    except Exception as e:
        print(f"Failed to insert {title}, {author}: {e}")
print("Data successfully inserted into MongoDB")