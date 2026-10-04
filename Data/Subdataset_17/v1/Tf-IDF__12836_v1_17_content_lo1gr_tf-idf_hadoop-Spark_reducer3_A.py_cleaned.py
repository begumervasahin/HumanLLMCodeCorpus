import sys
from math import log10
def main():
    prev_word = None
    count = 1
    dic = {}
    temp_arr = []
    D = 10.0
    tfidf = 0
    for line in sys.stdin:
        line = line.strip()
        word, s = line.split('\t', 1)
        filename, n, N, c = s.split(' ', 3)
        n = float(n)
        N = float(N)
        c = int(c)
        if prev_word == word:
            count += c
        else:
            if prev_word is not None:
                counts = f'{n} {N} {count}'
                dic[prev_word] = counts
                strings = f'{prev_word} {filename}'
                temp_arr.append(strings)
            count = c
            prev_word = word
    counts = f'{n} {N} {count}'
    dic[prev_word] = counts
    strings = f'{prev_word} {filename}'
    temp_arr.append(strings)
    for i in temp_arr:
        word, filename = i.split(' ', 1)
        if word in dic:
            n, N, m = dic[word].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(D / m)
            print(f'{i}\t{tfidf}')
if __name__ == "__main__":
    main()
import sys
from math import log10
def main():
    prev_word = None
    count = 1
    dic = {}
    temp_arr = []
    D = 10.0
    tfidf = 0
    for line in sys.stdin:
        line = line.strip()
        word, s = line.split('\t', 1)
        filename, n, N, c = s.split(' ', 3)
        n = float(n)
        N = float(N)
        c = int(c)
        if prev_word == word:
            count += c
        else:
            if prev_word is not None:
                counts = f'{n} {N} {count}'
                dic[prev_word] = counts
                strings = f'{prev_word} {filename}'
                temp_arr.append(strings)
            count = c
            prev_word = word
    counts = f'{n} {N} {count}'
    dic[prev_word] = counts
    strings = f'{prev_word} {filename}'
    temp_arr.append(strings)
    for i in temp_arr:
        word, filename = i.split(' ', 1)
        if word in dic:
            n, N, m = dic[word].split(' ', 2)
            n = float(n)
            N = float(N)
            m = float(m)
            tfidf = (n / N) * log10(D / m)
            print(f'{i}\t{tfidf}')
if __name__ == "__main__":
    main()