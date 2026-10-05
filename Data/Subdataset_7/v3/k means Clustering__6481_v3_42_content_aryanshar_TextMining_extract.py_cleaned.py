import re
from textblob import TextBlob
def fonk1(b6):
    b1 = fonk2(b6)
    b2 = TextBlob(b1)
    b3 = b2.sentiment.b3
    if b3 > 0:
        return 'positive'
    elif b3 = = 0:
        return 'neutral'
    else:
        return 'negative'
def fonk2(b6):
    b1 = re.sub(r'http[s]?:
    return b1.strip()
b4 = []
b5 = []
with open("tweets_123.txt", 'r') as file:
    for line in file:
        b6 = line.strip()
        b7 = re.search(r'http[s]?:
        b8 = {'text': b6, 'sentiment': fonk1(b6)}
        if b7:
            b4.append(b8)
        else:
            b5.append(b8)
b9 = [b6 for b6 in b4 if b6['sentiment'] == 'positive']
b10 = [b6 for b6 in b4 if b6['sentiment'] == 'negative']
b11 = [b6 for b6 in b4 if b6['sentiment'] == 'neutral']
b12 = len(b4)
print(f"Positive tweets percentage: {100 * len(b9) / b12:.2f} %")
print(f"Negative tweets percentage: {100 * len(b10) / b12:.2f} %")
print(f"Neutral tweets percentage: {100 * len(b11) / b12:.2f} %")
def fonk3(label, tweets):
    print(f"\n\n{label} tweets:")
    for b6 in tweets[:5]:
        print(f"- {b6['text']}")
fonk3("Positive", b9)
fonk3("Negative", b10)
fonk3("Neutral", b11)