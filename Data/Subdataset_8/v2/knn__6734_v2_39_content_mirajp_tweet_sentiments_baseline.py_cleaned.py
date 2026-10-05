import re
from nltk.corpus import opinion_lexicon
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
sentiment_words = {}
flag = False
for word in opinion_lexicon.words():
    if not flag:
        sentiment_words[word] = 0
        if re.search("zombie", word):
            flag = True
    else:
        sentiment_words[word] = 1
with open("test.list", 'r') as test_file, open("baseline_out.txt", 'w') as out_file:
    for line_cnt, tweet in enumerate(test_file, start=1):
        words = tweet.split()
        neg = sum(1 for word in words if sentiment_words.get(word.lower(), -1) == 0)
        pos = sum(1 for word in words if sentiment_words.get(word.lower(), -1) == 1)
        if pos > neg:
            out_file.write(f"{line_cnt} positive\n")
        elif pos < neg:
            out_file.write(f"{line_cnt} negative\n")
        else:
            out_file.write(f"{line_cnt} neutral\n")