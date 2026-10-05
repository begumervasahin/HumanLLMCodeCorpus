from operator import itemgetter
import sys
from math import log10, sqrt
prev_word = None
count = 1
word = None
dic = {}
temp_arr = []
D = 10.0
tfidf=0
for line in sys.stdin:
    line = line.strip()
    word, s = line.split('\t', 1)
    filename, n, N, c = s.split(' ', 3)
    if prev_word == word:
        count += int(c)
    else:
        if prev_word != None:
            counts = n + ' ' + N + ' ' + str(count)
            dic[prev_word] = counts
            strings = prev_word + ' ' + filename
            temp_arr.append(strings)
        count = 1
        prev_word = word
counts = n + ' ' + N + ' ' + str(count)
dic[prev_word] = counts
strings = prev_word + ' ' + filename
temp_arr.append(strings)
for i in temp_arr:
    word, filename = i.split(' ', 1)
    for w in dic:
        if word == w:
            n, N, m = dic[w].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(D / m)
            print '%s\t%s' % (i, tfidf)