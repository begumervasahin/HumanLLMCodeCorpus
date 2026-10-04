import re
from textblob import TextBlob
def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
def clean_tweet(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
tweet_with_url = {}
tweet_without_url = {}
tweets_url_yes = []
tweets_url_no = []
with open("tweets_123.txt", 'r') as data:
    tweets = [line.strip() for line in data]
for line in tweets:
    urls = re.search(r'http[s]?:
    if urls is not None:
        tweet_with_url = {
            'text': line,
            'sentiment': get_tweet_sentiment(line)
        }
        tweets_url_yes.append(tweet_with_url)
    else:
        tweet_without_url = {
            'text': line,
            'sentiment': get_tweet_sentiment(line)
        }
        tweets_url_no.append(tweet_without_url)
ptweets = [tweet for tweet in tweets_url_yes if tweet['sentiment'] == 'positive']
ntweets = [tweet for tweet in tweets_url_yes if tweet['sentiment'] == 'negative']
neuttweets = [tweet for tweet in tweets_url_yes if tweet['sentiment'] == 'neutral']
print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
print("Neutral tweets percentage: {} %".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)))
print("\n\nPositive tweets:")
for tweet in ptweets:
    print(tweet['text'])
print("\n\nNegative tweets:")
for tweet in ntweets:
    print(tweet['text'])
print("\n\nNeutral tweets:")
for tweet in neuttweets:
    print(tweet['text'])