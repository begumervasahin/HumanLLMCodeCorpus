import sys
from math import log10
D = 10.0
prev_word = None
word_counts = {}
temp_list = []
def process_word(word, count, filename, n, N):
    counts = f"{n} {N} {count}"
    word_counts[word] = counts
    temp_list.append(f"{word} {filename}")
for line in sys.stdin:
    line = line.strip()
    word, details = line.split('\t', 1)
    filename, n, N, c = details.split(' ', 3)
    if prev_word == word:
        count += int(c)
    else:
        if prev_word is not None:
            process_word(prev_word, count, filename, n, N)
        count = int(c)
        prev_word = word
if prev_word is not None:
    process_word(prev_word, count, filename, n, N)
for item in temp_list:
    word, filename = item.split(' ', 1)
    if word in word_counts:
        n, N, m = word_counts[word].split(' ', 2)
        n, N, m = float(n), float(N), float(m)
        tfidf = (n / N) * log10(D / m)
        print(f'{item}\t{tfidf}')