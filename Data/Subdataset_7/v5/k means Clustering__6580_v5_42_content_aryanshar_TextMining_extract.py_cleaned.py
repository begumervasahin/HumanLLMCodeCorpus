import re
from textblob import TextBlob
def fonk1(tweet):
    '''
    Classify sentiment of a tweet using TextBlob's sentiment b1
    '''
    b1 = TextBlob(fonk2(tweet))
    b2 = b1.sentiment.b2
    if b2 > 0:
        return 'positive'
    elif b2 = = 0:
        return 'neutral'
    else:
        return 'negative'
def fonk2(tweet):
    '''
    Clean tweet text by removing links and special characters
    '''
    return tweet
b3 = []
b4 = []
with open("b5 123.txt", 'r') as data_file:
    b5 = [line.strip() for line in data_file]
for tweet in b5:
    b6 = re.search('http[s]?:
    if b6:
        b3.append({'text': tweet, 'sentiment': fonk1(tweet)})
    else:
        b4.append({'text': tweet, 'sentiment': fonk1(tweet)})
b7 = len(b5)
b8 = [tweet for tweet in b3 if tweet['sentiment'] == 'positive']
b9 = [tweet for tweet in b3 if tweet['sentiment'] == 'negative']
b10 = [tweet for tweet in b3 if tweet['sentiment'] == 'neutral']
b11 = len(b8) / b7 * 100
b12 = len(b9) / b7 * 100
b13 = len(b10) / b7 * 100
print("Positive b5 percentage: {:.2f} %".format(b11))
print("Negative b5 percentage: {:.2f} %".format(b12))
print("Neutral b5 percentage: {:.2f} %".format(b13))
print("\n\nPositive b5:")
for tweet in b8:
    print(tweet['text'])
print("\n\nNegative b5:")
for tweet in b9:
    print(tweet['text'])
print("\n\nNeutral b5:")
for tweet in b10:
    print(tweet['text'])