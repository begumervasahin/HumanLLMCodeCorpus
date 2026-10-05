import re
from nltk.corpus import opinion_lexicon
opinion_words = set(opinion_lexicon.words())
sentiment_words = {}
start_adding = False
for word in opinion_words:
    if not start_adding:
        sentiment_words[word] = 0
        if re.search("zombie", word):
            start_adding = True
    else:
        sentiment_words[word] = 1
with open("test.list", 'r') as test_file, open("baseline_out.txt", 'w') as out_file:
    for line_cnt, tweet in enumerate(test_file, start=1):
        words = tweet.split()
        neg_count = sum(1 for word in words if sentiment_words.get(word.lower(), -1) == 0)
        pos_count = sum(1 for word in words if sentiment_words.get(word.lower(), -1) == 1)
        if pos_count > neg_count:
            out_file.write(f"{line_cnt} positive\n")
        elif pos_count < neg_count:
            out_file.write(f"{line_cnt} negative\n")
        else:
            out_file.write(f"{line_cnt} neutral\n")