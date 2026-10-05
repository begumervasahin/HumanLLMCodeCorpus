import sys
from math import log10
prev_word = None
count = 1
word = None
doc_counts = {}
temp_arr = []
D = 10.0
for line in sys.stdin:
    line = line.strip()
    word, rest = line.split('\t', 1)
    filename, n, N, c = rest.split(' ', 3)
    if prev_word == word:
        count += int(c)
    else:
        if prev_word is not None:
            doc_counts[prev_word] = f"{n} {N} {count}"
            temp_arr.append(f"{prev_word} {filename}")
        count = 1
        prev_word = word
if prev_word is not None:
    doc_counts[prev_word] = f"{n} {N} {count}"
    temp_arr.append(f"{prev_word} {filename}")
for pair in temp_arr:
    word, filename = pair.split(' ', 1)
    n, N, m = doc_counts[word].split(' ', 2)
    n, N, m = float(n), float(N), float(m)
    tfidf = (n / N) * log10(D / m)
    print(f"{pair}\t{tfidf}")