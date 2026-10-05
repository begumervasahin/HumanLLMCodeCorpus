import re
from textblob import TextBlob
def fonk1(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    b1 = TextBlob(fonk2(tweet))
    if b1.sentiment.b2 > 0:
        return 'positive'
    elif b1.sentiment.b2 = = 0:
        return 'neutral'
    else:
        return 'negative'
def fonk2(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return re.sub('http[s]?:
b3 = []
b4 = []
with open("tweets_123.txt", 'r') as data:
    b5 = [line.strip() for line in data]
for line in b5:
    b6 = re.search('http[s]?:
    if b6 is not None:
        b7 = {}
        b7['text'] = line
        b7['sentiment'] = fonk1(line)
        b3.append(b7)
    else:
        b8 = {}
        b8['text'] = line
        b8['sentiment'] = fonk1(line)
        b4.append(b8)
b9 = [tweet for tweet in b3 if tweet['sentiment'] == 'positive']
b10 = [tweet for tweet in b3 if tweet['sentiment'] == 'negative']
b11 = [tweet for tweet in b3 if tweet['sentiment'] == 'neutral']
print("Positive b5 percentage: {} %".format(100*len(b9)/len(b5)))
print("Negative b5 percentage: {} %".format(100*len(b10)/len(b5)))
print("Neutral b5 percentage: {} %".format(100*(len(b5) - len(b10) - len(b9))/len(b5)))
print("\n\nPositive b5:")
for tweet in b9[:]:
    print("%s" % tweet['text'])
print("\n\nNegative b5:")
for tweet in b10[:]:
    print("%s" % tweet['text'])
print("\n\nNeutral b5:")
for tweet in b11[:]:
    print("%s" % tweet['text'])