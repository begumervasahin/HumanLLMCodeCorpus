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
def process_tweets(tweets):
    tweets_with_url = []
    tweets_without_url = []
    for tweet in tweets:
        if re.search(r'http[s]?:
            tweet_data = {
                'text': tweet,
                'sentiment': get_tweet_sentiment(tweet)
            }
            tweets_with_url.append(tweet_data)
        else:
            tweet_data = {
                'text': tweet,
                'sentiment': get_tweet_sentiment(tweet)
            }
            tweets_without_url.append(tweet_data)
    return tweets_with_url, tweets_without_url
def calculate_sentiment_percentages(tweets, positive_tweets, negative_tweets):
    total_tweets = len(tweets)
    positive_percentage = 100 * len(positive_tweets) / total_tweets
    negative_percentage = 100 * len(negative_tweets) / total_tweets
    neutral_percentage = 100 * (total_tweets - len(positive_tweets) - len(negative_tweets)) / total_tweets
    print("Positive tweets percentage: {:.2f} %".format(positive_percentage))
    print("Negative tweets percentage: {:.2f} %".format(negative_percentage))
    print("Neutral tweets percentage: {:.2f} %".format(neutral_percentage))
def print_tweets(tweets, sentiment_type):
    print("\n\n{} tweets:".format(sentiment_type.capitalize()))
    for tweet in tweets:
        print(tweet['text'])
with open("tweets_123.txt", 'r') as file:
    tweets = [line.strip() for line in file]
tweets_with_url, tweets_without_url = process_tweets(tweets)
positive_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'positive']
negative_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'negative']
neutral_tweets = [tweet for tweet in tweets_with_url if tweet['sentiment'] == 'neutral']
calculate_sentiment_percentages(tweets, positive_tweets, negative_tweets)
print_tweets(positive_tweets, 'positive')
print_tweets(negative_tweets, 'negative')
print_tweets(neutral_tweets, 'neutral')