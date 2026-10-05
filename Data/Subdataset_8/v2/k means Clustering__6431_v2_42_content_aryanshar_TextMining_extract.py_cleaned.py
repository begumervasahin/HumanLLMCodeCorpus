import re
from textblob import TextBlob
def analyze_tweet_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
def clean_tweet(tweet):
    cleaned_tweet = re.sub('http[s]?:
    return cleaned_tweet
tweets_with_urls = []
tweets_without_urls = []
with open("tweets_123.txt", 'r') as file:
    tweets = [line.strip() for line in file]
for tweet in tweets:
    contains_url = re.search('http[s]?:
    tweet_data = {'text': tweet, 'sentiment': analyze_tweet_sentiment(tweet)}
    if contains_url:
        tweets_with_urls.append(tweet_data)
    else:
        tweets_without_urls.append(tweet_data)
positive_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'positive']
negative_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'negative']
neutral_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'neutral']
print(f"Positive tweets percentage: {100 * len(positive_tweets) / len(tweets):.2f} %")
print(f"Negative tweets percentage: {100 * len(negative_tweets) / len(tweets):.2f} %")
print(f"Neutral tweets percentage: {100 * (len(neutral_tweets)) / len(tweets):.2f} %")
def print_tweet_examples(label, tweets):
    print(f"\n\n{label} tweets:")
    for tweet in tweets[:5]:
        print(f"- {tweet['text']}")
print_tweet_examples("Positive", positive_tweets)
print_tweet_examples("Negative", negative_tweets)
print_tweet_examples("Neutral", neutral_tweets)