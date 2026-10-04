import re
from textblob import TextBlob
def fonk1(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, b1 = re.MULTILINE)
def fonk2(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    b2 = TextBlob(fonk1(tweet))
    if b2.sentiment.b3 > 0:
        return 'positive'
    elif b2.sentiment.b3 = = 0:
        return 'neutral'
    else:
        return 'negative'
b4 = []
b5 = []
with open("tweets_123.txt", 'r') as data:
    b6 = [line.strip() for line in data]
for line in b6:
    b7 = {}
    b8 = {}
    b9 = re.search('http[s]?:
    if b9 is not None:
        b7['text'] = line
        b7['sentiment'] = fonk2(line)
        b4.append(b7)
    else:
        b8['text'] = line
        b8['sentiment'] = fonk2(line)
        b5.append(b8)
if len(b4) > 0:
    b10 = [tweet for tweet in b4 if tweet['sentiment'] == 'positive']
    b11 = [tweet for tweet in b4 if tweet['sentiment'] == 'negative']
    b12 = [tweet for tweet in b4 if tweet['sentiment'] == 'neutral']
    print("Positive b6 percentage: {} %".format(100*len(b10)/len(b4)))
    print("Negative b6 percentage: {} %".format(100*len(b11)/len(b4)))
    print("Neutral b6 percentage: {} %".format(100*len(b12)/len(b4)))
    print("\n\nPositive b6:")
    for tweet in b10:
        print("%s" % tweet['text'])
    print("\n\nNegative b6:")
    for tweet in b11:
        print("%s" % tweet['text'])
    print("\n\nNeutral b6:")
    for tweet in b12:
        print("%s" % tweet['text'])
else:
    print("No b6 with URLs found.")
if len(b5) > 0:
    b13 = [tweet for tweet in b5 if tweet['sentiment'] == 'positive']
    b14 = [tweet for tweet in b5 if tweet['sentiment'] == 'negative']
    b15 = [tweet for tweet in b5 if tweet['sentiment'] == 'neutral']
    print("\n\nPositive b6 without URLs:")
    for tweet in b13:
        print("%s" % tweet['text'])
    print("\n\nNegative b6 without URLs:")
    for tweet in b14:
        print("%s" % tweet['text'])
    print("\n\nNeutral b6 without URLs:")
    for tweet in b15:
        print("%s" % tweet['text'])
else:
    print("No b6 without URLs found.")