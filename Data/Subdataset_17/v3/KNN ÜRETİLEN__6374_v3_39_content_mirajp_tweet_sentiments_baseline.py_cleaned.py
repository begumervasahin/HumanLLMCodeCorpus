import sys
import re
import nltk
from nltk.corpus import opinion_lexicon
def load_sentiment_words():
    nltk.download('opinion_lexicon')
    sentiment_words = {}
    flag = 0
    for word in opinion_lexicon.words():
        sentiment_words[word] = flag
        if word == 'zombie':
            flag = 1
    return sentiment_words
def analyze_sentiment(tweet, sentiment_words):
    words = tweet.split()
    pos, neg = 0, 0
    for word in words:
        sentiment = sentiment_words.get(word.lower())
        if sentiment is not None:
            if sentiment == 1:
                pos += 1
            elif sentiment == 0:
                neg += 1
    return pos, neg
def main():
    sentiment_words = load_sentiment_words()
    with open("test.list", 'rb') as test_file, open("baseline_out.txt", 'w') as out_file:
        for line_cnt, tweet in enumerate(test_file, start=1):
            tweet = tweet.decode('ISO-8859-1')
            pos, neg = analyze_sentiment(tweet, sentiment_words)
            if pos > neg:
                sentiment = "positive"
            elif pos < neg:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            out_file.write(f"{line_cnt} {sentiment}\n")
if __name__ == "__main__":
    main()