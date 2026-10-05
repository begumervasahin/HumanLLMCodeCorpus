import re
from textblob import TextBlob
def analyze_tweet_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)
    analysis = TextBlob(cleaned_tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'
def clean_tweet(tweet):
    cleaned_tweet = re.sub(r'http[s]?:
    return cleaned_tweet.strip()
tweets_with_urls = []
tweets_without_urls = []
with open("tweets_123.txt", 'r') as file:
    for line in file:
        tweet = line.strip()
        contains_url = re.search(r'http[s]?:
        tweet_data = {'text': tweet, 'sentiment': analyze_tweet_sentiment(tweet)}
        if contains_url:
            tweets_with_urls.append(tweet_data)
        else:
            tweets_without_urls.append(tweet_data)
positive_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'positive']
negative_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'negative']
neutral_tweets = [tweet for tweet in tweets_with_urls if tweet['sentiment'] == 'neutral']
total_tweets = len(tweets_with_urls)
print(f"Positive tweets percentage: {100 * len(positive_tweets) / total_tweets:.2f} %")
print(f"Negative tweets percentage: {100 * len(negative_tweets) / total_tweets:.2f} %")
print(f"Neutral tweets percentage: {100 * len(neutral_tweets) / total_tweets:.2f} %")
def print_tweet_examples(label, tweets):
    print(f"\n\n{label} tweets:")
    for tweet in tweets[:5]:
        print(f"- {tweet['text']}")
print_tweet_examples("Positive", positive_tweets)
print_tweet_examples("Negative", negative_tweets)
print_tweet_examples("Neutral", neutral_tweets)