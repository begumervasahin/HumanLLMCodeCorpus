import sys
import math
def calculate_tfidf(word_count, word_per_doc, total_docs):
    tf = word_count / word_per_doc
    idf = math.log(total_docs / float(1))
    return tf * idf
previous_word = None
previous_doc_id = None
previous_word_count = None
previous_word_per_doc = None
total_documents = 1
for line in sys.stdin:
    line = line.strip()
    word, rest = line.split("\t")
    doc_id, word_count, word_per_doc = rest.split(",")
    word_count = int(word_count)
    word_per_doc = int(word_per_doc)
    if previous_word == word:
        total_documents = 2
        tfidf = calculate_tfidf(previous_word_count, previous_word_per_doc, total_documents)
        print("(%s,%s)\t%s" % (previous_word, previous_doc_id, tfidf))
    else:
        if previous_word is not None:
            tfidf = calculate_tfidf(previous_word_count, previous_word_per_doc, total_documents)
            print("(%s,%s)\t%s" % (previous_word, previous_doc_id, tfidf))
    previous_word = word
    previous_doc_id = doc_id
    previous_word_count = word_count
    previous_word_per_doc = word_per_doc
    total_documents = 1
tfidf = calculate_tfidf(previous_word_count, previous_word_per_doc, total_documents)
print("(%s,%s)\t%s" % (previous_word, previous_doc_id, tfidf))