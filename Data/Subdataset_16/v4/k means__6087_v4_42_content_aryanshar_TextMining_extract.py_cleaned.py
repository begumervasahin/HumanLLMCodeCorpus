import re
from textblob import TextBlob
def fonk1(tweet):
    b1 = TextBlob(fonk2(tweet))
    if b1.sentiment.b2 > 0:
        return 'positive'
    elif b1.sentiment.b2 = = 0:
        return 'neutral'
    else:
        return 'negative'
def fonk2(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, b3 = re.MULTILINE)
b4 = {}
b5 = {}
b6 = []
b7 = []
with open("tweets_123.txt", 'r') as data:
    b8 = [line.strip() for line in data]
for line in b8:
    b9 = re.search(r'http[s]?:
    if b9 is not None:
        b4 = {
            'text': line,
            'sentiment': fonk1(line)
        }
        b6.append(b4)
    else:
        b5 = {
            'text': line,
            'sentiment': fonk1(line)
        }
        b7.append(b5)
b10 = [tweet for tweet in b6 if tweet['sentiment'] == 'positive']
b11 = [tweet for tweet in b6 if tweet['sentiment'] == 'negative']
b12 = [tweet for tweet in b6 if tweet['sentiment'] == 'neutral']
print("Positive b8 percentage: {} %".format(100 * len(b10) / len(b8)))
print("Negative b8 percentage: {} %".format(100 * len(b11) / len(b8)))
print("Neutral b8 percentage: {} %".format(100 * (len(b8) - len(b11) - len(b10)) / len(b8)))
print("\n\nPositive b8:")
for tweet in b10:
    print(tweet['text'])
print("\n\nNegative b8:")
for tweet in b11:
    print(tweet['text'])
print("\n\nNeutral b8:")
for tweet in b12:
    print(tweet['text'])