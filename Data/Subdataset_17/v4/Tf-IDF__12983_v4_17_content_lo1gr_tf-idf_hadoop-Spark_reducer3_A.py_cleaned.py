from operator import itemgetter
import sys
from math import log10
prev_word = None
count = 1
word = None
word_counts = {}
temp_list = []
D = 10.0
for line in sys.stdin:
    line = line.strip()
    word, s = line.split('\t', 1)
    filename, n, N, c = s.split(' ', 3)
    if prev_word == word:
        count += int(c)
    else:
        if prev_word is not None:
            counts = f"{n} {N} {count}"
            word_counts[prev_word] = counts
            temp_list.append(f"{prev_word} {filename}")
        count = 1
        prev_word = word
counts = f"{n} {N} {count}"
word_counts[prev_word] = counts
temp_list.append(f"{prev_word} {filename}")
for item in temp_list:
    word, filename = item.split(' ', 1)
    if word in word_counts:
        n, N, m = word_counts[word].split(' ', 2)
        n = float(n)
        N = float(N)
        m = float(m)
        tfidf = (n / N) * log10(D / m)
        print(f'{item}\t{tfidf}')