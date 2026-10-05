import re
from textblob import TextBlob
def get_tweet_sentiment(tweet):
    '''
    Classify sentiment of a tweet using TextBlob's sentiment analysis
    '''
    analysis = TextBlob(clean_tweet(tweet))
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'
def clean_tweet(tweet):
    '''
    Clean tweet text by removing links and special characters
    '''
    return tweet
tweets_with_url = []
tweets_without_url = []
with open("tweets 123.txt", 'r') as data_file:
    tweets = [line.strip() for line in data_file]
for tweet in tweets:
    urls = re.search('http[s]?:
    if urls:
        tweets_with_url.append({'text': tweet, 'sentiment': get_tweet_sentiment(tweet)})
    else:
        tweets_without_url.append({'text': tweet, 'sentiment': get_tweet_sentiment(tweet)})
total_tweets = len(tweets)
positive_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'positive']
negative_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'negative']
neutral_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'neutral']
positive_percentage = len(positive_tweets) / total_tweets * 100
negative_percentage = len(negative_tweets) / total_tweets * 100
neutral_percentage = len(neutral_tweets) / total_tweets * 100
print("Positive tweets percentage: {:.2f} %".format(positive_percentage))
print("Negative tweets percentage: {:.2f} %".format(negative_percentage))
print("Neutral tweets percentage: {:.2f} %".format(neutral_percentage))
print("\n\nPositive tweets:")
for tweet in positive_tweets:
    print(tweet['text'])
print("\n\nNegative tweets:")
for tweet in negative_tweets:
    print(tweet['text'])
print("\n\nNeutral tweets:")
for tweet in neutral_tweets:
    print(tweet['text'])