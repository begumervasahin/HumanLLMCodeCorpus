import re
from textblob import TextBlob
def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using TextBlob's sentiment method
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return tweet
tweet_with_url = {}
tweet_without_url = {}
tweets_url_yes = []
tweets_url_no = []
with open("tweets 123.txt", 'r') as data_file:
    tweets = [line.strip() for line in data_file]
for line in tweets:
    urls = re.search('http[s]?:
    if urls is not None:
        tweet_with_url['text'] = data
        tweet_with_url['sentiment'] = get_tweet_sentiment(data)
        tweets_url_yes.append(tweet_with_url)
    else:
        tweet_without_url['text'] = line
        tweet_without_url['sentiment'] = get_tweet_sentiment(line)
        tweets_url_no.append(tweet_without_url)
ptweets = [tweet for tweet in tweets_url_yes if tweet_with_url['sentiment'] == 'positive']
positive_percentage = 100 * len(ptweets) / len(tweets)
ntweets = [tweet for tweet in tweets_url_yes if tweet_with_url['sentiment'] == 'negative']
negative_percentage = 100 * len(ntweets) / len(tweets)
neuttweets = [tweet for tweet in tweets_url_yes if tweet_with_url['sentiment'] == 'neutral']
neutral_percentage = 100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets)
print("Positive tweets percentage: {} %".format(positive_percentage))
print("Negative tweets percentage: {} %".format(negative_percentage))
print("Neutral tweets percentage: {} %".format(neutral_percentage))
print("\n\nPositive tweets:")
for tweet in ptweets[:]:
    print("%s" % tweet['text'])
print("\n\nNegative tweets:")
for tweet in ntweets[:]:
    print("%s" % tweet['text'])
print("\n\nNeutral tweets:")
for tweet in neuttweets[:]:
    print("%s" % tweet['text'])