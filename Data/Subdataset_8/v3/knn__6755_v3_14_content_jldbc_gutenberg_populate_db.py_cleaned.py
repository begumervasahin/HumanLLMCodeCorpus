from sklearn.feature_extraction.text import TfidfVectorizer
import os
from pymongo import MongoClient
client = MongoClient()
db = client.bookdb
posts = db.posts
def load_documents(directory):
    documents = []
    for book_file in os.listdir(directory):
        if not book_file.startswith('.'):
            with open(os.path.join(directory, book_file), 'rb') as f:
                content = f.read().decode('utf-8', errors='replace')
                documents.append(content)
    return documents
def extract_title_and_author(content):
    title, author = None, None
    for line in content.splitlines():
        if line.startswith("Title: "):
            title = line[7:].strip()
        elif line.startswith("Author: "):
            author = line[8:].strip()
        if title and author:
            break
    return title, author
def build_database(tfidf_matrix, feature_names, documents_info):
    database = {}
    for i, doc_info in enumerate(documents_info):
        doc = tfidf_matrix[i].toarray()[0]
        phrase_scores = [(index, score) for index, score in enumerate(doc) if score > 0]
        sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1], reverse=True)
        word_dict = {feature_names[index]: score for index, score in sorted_phrase_scores}
        title, author = doc_info
        database[(title, author)] = word_dict
    return database
def save_to_mongodb(database):
    for info, word_dict in database.items():
        title, author = info
        try:
            post = {"title": title, "author": author, **word_dict}
            post_id = posts.insert_one(post).inserted_id
        except Exception as e:
            print(f"Failed to insert: {title}, {author}. Error: {e}")
def main():
    docs_dir = "/path/to/documents"
    documents = load_documents(docs_dir)
    tfidf = TfidfVectorizer(max_df=0.9,
                            ngram_range=(1, 1),
                            stop_words='english',
                            strip_accents='unicode',
                            analyzer='word')
    tfidf_matrix = tfidf.fit_transform(documents)
    feature_names = tfidf.get_feature_names()
    documents_info = [extract_title_and_author(content) for content in documents]
    database = build_database(tfidf_matrix, feature_names, documents_info)
    save_to_mongodb(database)
if __name__ == '__main__':
    main()