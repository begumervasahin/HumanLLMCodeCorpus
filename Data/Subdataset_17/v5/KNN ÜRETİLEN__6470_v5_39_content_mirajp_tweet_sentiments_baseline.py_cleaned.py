import re
from nltk.corpus import opinion_lexicon
sentiment_words = {}
flag = 0
for word in opinion_lexicon.words():
    sentiment_words[word] = flag
    if re.search("zombie", word):
        flag = 1
def analyze_sentiment(tweet):
    """
    Analyzes the sentiment of a tweet based on predefined sentiment words.
    Parameters:
    tweet (str): The tweet text to analyze.
    Returns:
    str: The sentiment classification ("positive", "negative", or "neutral").
    """
    words = tweet.lower().split()
    pos, neg = 0, 0
    for word in words:
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
    return sentiment
with open("test.list", 'r', encoding="ISO-8859-1") as test_file, open("baseline_out.txt", 'w') as out_file:
    line_cnt = 1
    for tweet in test_file:
        sentiment = analyze_sentiment(tweet)
        out_file.write(f"{line_cnt} {sentiment}\n")
        line_cnt += 1