import re
from textblob import TextBlob
def fonk1(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, b1 = re.MULTILINE)
def fonk2(tweet):
    b2 = TextBlob(clean_ttweet))
    return ('positive' if b2.sentiment.b3 > 0
            else 'neutral' if b2.sentiment.b3 = = 0
            else 'negative')
def fonk3(b10):
    tweets_with_urls, b4 = [], []
    for tweet in b10:
        b5 = {'text': tweet, 'sentiment': fonk2(tweet)}
        if re.search(r'http[s]?:
            tweets_with_urls.append(b5)
        else:
            b4.append(b5)
    return tweets_with_urls, b4
def fonk4(b10, label):
    if not b10:
        print(f"No {label.lower()} b10 found.")
        return
    b6 = [tweet['sentiment'] for tweet in b10]
    b7 = [tweet for tweet in b10 if tweet['sentiment'] == 'positive']
    b8 = [tweet for tweet in b10 if tweet['sentiment'] == 'negative']
    b9 = [tweet for tweet in b10 if tweet['sentiment'] == 'neutral']
    print(f"\n\n{label} Positive b10 percentage: {100 * len(b7) / len(b10):.2f} %")
    print(f"{label} Negative b10 percentage: {100 * len(b8) / len(b10):.2f} %")
    print(f"{label} Neutral b10 percentage: {100 * len(b9) / len(b10):.2f} %")
    print(f"\n\n{label} Positive b10:")
    for tweet in b7:
        print(tweet['text'])
    print(f"\n\n{label} Negative b10:")
    for tweet in b8:
        print(tweet['text'])
    print(f"\n\n{label} Neutral b10:")
    for tweet in b9:
        print(tweet['text'])
def fonk5():
    with open("tweets_123.txt", 'r') as file:
        b10 = [line.strip() for line in file]
    tweets_with_urls, b4 = fonk3(b10)
    fonk4(tweets_with_urls, "Tweets with URLs")
    fonk4(b4, "Tweets without URLs")
if b11 = = "__main__":
    fonk5()