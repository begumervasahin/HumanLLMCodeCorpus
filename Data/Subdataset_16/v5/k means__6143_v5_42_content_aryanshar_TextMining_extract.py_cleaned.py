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
def fonk3(b11):
    b4 = []
    b5 = []
    for tweet in b11:
        if re.search(r'http[s]?:
            b6 = {
                'text': tweet,
                'sentiment': fonk1(tweet)
            }
            b4.append(b6)
        else:
            b6 = {
                'text': tweet,
                'sentiment': fonk1(tweet)
            }
            b5.append(b6)
    return b4, b5
def fonk4(b11, b12, b13):
    b7 = len(b11)
    b8 = 100 * len(b12) / b7
    b9 = 100 * len(b13) / b7
    b10 = 100 * (b7 - len(b12) - len(b13)) / b7
    print("Positive b11 percentage: {:.2f} %".format(b8))
    print("Negative b11 percentage: {:.2f} %".format(b9))
    print("Neutral b11 percentage: {:.2f} %".format(b10))
def fonk5(b11, sentiment_type):
    print("\n\n{} b11:".format(sentiment_type.capitalize()))
    for tweet in b11:
        print(tweet['text'])
with open("tweets_123.txt", 'r') as file:
    b11 = [line.strip() for line in file]
b4, b5 = fonk3(b11)
b12 = [tweet for tweet in b4 if tweet['sentiment'] == 'positive']
b13 = [tweet for tweet in b4 if tweet['sentiment'] == 'negative']
b14 = [tweet for tweet in b4 if tweet['sentiment'] == 'neutral']
fonk4(b11, b12, b13)
fonk5(b12, 'positive')
fonk5(b13, 'negative')
fonk5(b14, 'neutral')