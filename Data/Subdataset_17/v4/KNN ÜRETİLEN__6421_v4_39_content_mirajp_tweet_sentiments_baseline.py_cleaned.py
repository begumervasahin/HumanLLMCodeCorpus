import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
sentiment_words = {}
flag = 0
for word in opinion_lexicon.words():
    sentiment_words[word] = flag
    if re.search("zombie", word):
        flag = 1
with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
    line_cnt = 1
    for tweet in test_file:
        words = tweet.split()
        pos, neg = 0, 0
        for word in words:
            word = word.lower()
            if word in sentiment_words:
                if sentiment_words[word] == 1:
                    pos += 1
                elif sentiment_words[word] == 0:
                    neg += 1
        if pos > neg:
            sentiment = "positive"
        elif pos < neg:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        out_file.write(f"{line_cnt} {sentiment}\n")
        line_cnt += 1