import re
from textblob import TextBlob
def fonk1(tweet):
    b1 = fonk2(tweet)
    b2 = TextBlob(b1)
    if b2.sentiment.b3 > 0:
        return 'positive'
    elif b2.sentiment.b3 = = 0:
        return 'neutral'
    else:
        return 'negative'
def fonk2(tweet):
    b1 = re.sub('http[s]?:
    return b1
b4 = []
b5 = []
with open("tweets_123.txt", 'r') as file:
    b6 = [line.strip() for line in file]
for tweet in b6:
    b7 = re.search('http[s]?:
    b8 = {'text': tweet, 'sentiment': fonk1(tweet)}
    if b7:
        b4.append(b8)
    else:
        b5.append(b8)
b9 = [tweet for tweet in b4 if tweet['sentiment'] == 'positive']
b10 = [tweet for tweet in b4 if tweet['sentiment'] == 'negative']
b11 = [tweet for tweet in b4 if tweet['sentiment'] == 'neutral']
print(f"Positive b6 percentage: {100 * len(b9) / len(b6):.2f} %")
print(f"Negative b6 percentage: {100 * len(b10) / len(b6):.2f} %")
print(f"Neutral b6 percentage: {100 * (len(b11)) / len(b6):.2f} %")
def fonk3(label, b6):
    print(f"\n\n{label} b6:")
    for tweet in b6[:5]:
        print(f"- {tweet['text']}")
fonk3("Positive", b9)
fonk3("Negative", b10)
fonk3("Neutral", b11)