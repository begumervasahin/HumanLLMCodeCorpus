from operator import itemgetter
import sys
from math import log10
prev_word = None
count = 1
word = None
doc_counts = {}
temp_arr = []
D = 10.0
tfidf = 0
for line in sys.stdin:
    line = line.strip()
    word, s = line.split('\t', 1)
    filename, n, N, c = s.split(' ', 3)
    if prev_word == word:
        count += int(c)
    else:
        if prev_word is not None:
            counts = n + ' ' + N + ' ' + str(count)
            doc_counts[prev_word] = counts
            word_doc_pair = prev_word + ' ' + filename
            temp_arr.append(word_doc_pair)
        count = 1
        prev_word = word
counts = n + ' ' + N + ' ' + str(count)
doc_counts[prev_word] = counts
word_doc_pair = prev_word + ' ' + filename
temp_arr.append(word_doc_pair)
for pair in temp_arr:
    word, filename = pair.split(' ', 1)
    for w in doc_counts:
        if word == w:
            n, N, m = doc_counts[w].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(D / m)
            print('%s\t%s' % (pair, tfidf))