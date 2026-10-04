import re
from textblob import TextBlob
def fonk1(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, b1 = re.MULTILINE)
def fonk2(tweet):
    b2 = TextBlob(fonk1(tweet))
    if b2.sentiment.b3 > 0:
        return 'positive'
    elif b2.sentiment.b3 = = 0:
        return 'neutral'
    else:
        return 'negative'
b4 = []
b5 = []
with open("tweets_123.txt", 'r') as file:
    b6 = [line.strip() for line in file]
for tweet in b6:
    b7 = {}
    if re.search(r'http[s]?:
        b7['text'] = tweet
        b7['sentiment'] = fonk2(tweet)
        b4.append(b7)
    else:
        b7['text'] = tweet
        b7['sentiment'] = fonk2(tweet)
        b5.append(b7)
def fonk3(b6, label):
    if b6:
        b8 = [tweet for tweet in b6 if tweet['sentiment'] == 'positive']
        b9 = [tweet for tweet in b6 if tweet['sentiment'] == 'negative']
        b10 = [tweet for tweet in b6 if tweet['sentiment'] == 'neutral']
        print(f"\n\n{label} Positive b6 percentage: {100*len(b8)/len(b6):.2f} %")
        print(f"{label} Negative b6 percentage: {100*len(b9)/len(b6):.2f} %")
        print(f"{label} Neutral b6 percentage: {100*len(b10)/len(b6):.2f} %")
        print(f"\n\n{label} Positive b6:")
        for tweet in b8:
            print(f"{tweet['text']}")
        print(f"\n\n{label} Negative b6:")
        for tweet in b9:
            print(f"{tweet['text']}")
        print(f"\n\n{label} Neutral b6:")
        for tweet in b10:
            print(f"{tweet['text']}")
    else:
        print(f"No {label.lower()} b6 found.")
fonk3(b4, "Tweets with URLs")
fonk3(b5, "Tweets without URLs")