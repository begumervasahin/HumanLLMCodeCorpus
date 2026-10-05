from operator import itemgetter
import sys
from math import log10
prev_word = None
count = 1
doc_word_count = {}
temp_arr = []
corpus_size = 10.0
for line in sys.stdin:
    line = line.strip()
    word, details = line.split('\t', 1)
    filename, word_count, doc_word_total, word_freq = details.split(' ', 3)
    if prev_word == word:
        count += int(word_freq)
    else:
        if prev_word is not None:
            counts = word_count + ' ' + doc_word_total + ' ' + str(count)
            doc_word_count[prev_word] = counts
            pair = prev_word + ' ' + filename
            temp_arr.append(pair)
        count = 1
        prev_word = word
counts = word_count + ' ' + doc_word_total + ' ' + str(count)
doc_word_count[prev_word] = counts
pair = prev_word + ' ' + filename
temp_arr.append(pair)
for pair in temp_arr:
    word, filename = pair.split(' ', 1)
    for w in doc_word_count:
        if word == w:
            n, N, m = doc_word_count[w].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(corpus_size / m)
            print('%s\t%s' % (pair, tfidf))