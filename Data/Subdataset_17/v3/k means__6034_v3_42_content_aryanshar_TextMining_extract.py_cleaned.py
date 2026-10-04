import re
from textblob import TextBlob
def clean_tweet(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_ttweet))
    return ('positive' if analysis.sentiment.polarity > 0
            else 'neutral' if analysis.sentiment.polarity == 0
            else 'negative')
def categorize_tweets(tweets):
    tweets_with_urls, tweets_without_urls = [], []
    for tweet in tweets:
        tweet_data = {'text': tweet, 'sentiment': get_tweet_sentiment(tweet)}
        if re.search(r'http[s]?:
            tweets_with_urls.append(tweet_data)
        else:
            tweets_without_urls.append(tweet_data)
    return tweets_with_urls, tweets_without_urls
def print_sentiment_analysis(tweets, label):
    if not tweets:
        print(f"No {label.lower()} tweets found.")
        return
    sentiments = [tweet['sentiment'] for tweet in tweets]
    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutral_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    print(f"\n\n{label} Positive tweets percentage: {100 * len(positive_tweets) / len(tweets):.2f} %")
    print(f"{label} Negative tweets percentage: {100 * len(negative_tweets) / len(tweets):.2f} %")
    print(f"{label} Neutral tweets percentage: {100 * len(neutral_tweets) / len(tweets):.2f} %")
    print(f"\n\n{label} Positive tweets:")
    for tweet in positive_tweets:
        print(tweet['text'])
    print(f"\n\n{label} Negative tweets:")
    for tweet in negative_tweets:
        print(tweet['text'])
    print(f"\n\n{label} Neutral tweets:")
    for tweet in neutral_tweets:
        print(tweet['text'])
def main():
    with open("tweets_123.txt", 'r') as file:
        tweets = [line.strip() for line in file]
    tweets_with_urls, tweets_without_urls = categorize_tweets(tweets)
    print_sentiment_analysis(tweets_with_urls, "Tweets with URLs")
    print_sentiment_analysis(tweets_without_urls, "Tweets without URLs")
if __name__ == "__main__":
    main()