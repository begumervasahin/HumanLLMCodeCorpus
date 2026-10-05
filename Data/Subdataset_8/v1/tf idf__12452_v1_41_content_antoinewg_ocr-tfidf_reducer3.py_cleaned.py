import sys
import math
def get_tfidf(word_count, word_per_doc, n_doc, N=2):
    return (word_count / float(word_per_doc)) * math.log(N / n_doc)
prev_word = None
prev_doc_id = None
prev_wordcount = None
prev_wordperdoc = None
n_doc = 1
for line in sys.stdin:
    line = line.strip()
    word, rest = line.split("\t")
    doc_id, wordcount, wordperdoc = rest.split(",")
    wordcount = int(wordcount)
    wordperdoc = int(wordperdoc)
    if prev_word == word:
        n_doc += 1
    else:
        if prev_word is not None:
            prev_tfidf = get_tfidf(prev_wordcount, prev_wordperdoc, n_doc)
            print("(%s,%s)\t%s" % (prev_word, prev_doc_id, prev_tfidf))
        n_doc = 1
    prev_word = word
    prev_doc_id = doc_id
    prev_wordcount = wordcount
    prev_wordperdoc = wordperdoc
if prev_word is not None:
    prev_tfidf = get_tfidf(prev_wordcount, prev_wordperdoc, n_doc)
    print("(%s,%s)\t%s" % (prev_word, prev_doc_id, prev_tfidf))