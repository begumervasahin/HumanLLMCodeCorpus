import re
from textblob import TextBlob
def fonk1(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using TextBlob's sentiment method
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
    return tweet
b3 = {}
b4 = {}
b5 = []
b6 = []
with open("b7 123.txt", 'r') as data_file:
    b7 = [line.strip() for line in data_file]
for line in b7:
    b8 = re.search('http[s]?:
    if b8 is not None:
        b3['text'] = data
        b3['sentiment'] = fonk1(data)
        b5.append(b3)
    else:
        b4['text'] = line
        b4['sentiment'] = fonk1(line)
        b6.append(b4)
b9 = [tweet for tweet in b5 if b3['sentiment'] == 'positive']
b10 = 100 * len(b9) / len(b7)
b11 = [tweet for tweet in b5 if b3['sentiment'] == 'negative']
b12 = 100 * len(b11) / len(b7)
b13 = [tweet for tweet in b5 if b3['sentiment'] == 'neutral']
b14 = 100 * (len(b7) - len(b11) - len(b9)) / len(b7)
print("Positive b7 percentage: {} %".format(b10))
print("Negative b7 percentage: {} %".format(b12))
print("Neutral b7 percentage: {} %".format(b14))
print("\n\nPositive b7:")
for tweet in b9[:]:
    print("%s" % tweet['text'])
print("\n\nNegative b7:")
for tweet in b11[:]:
    print("%s" % tweet['text'])
print("\n\nNeutral b7:")
for tweet in b13[:]:
    print("%s" % tweet['text'])