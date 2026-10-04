import re
from textblob import TextBlob
def clean_tweet(tweet):
    return re.sub(r'http\S+|www\S+|https\S+', '', tweet, flags=re.MULTILINE)
def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
tweets_url_yes = []
tweets_url_no = []
with open("tweets_123.txt", 'r') as file:
    tweets = [line.strip() for line in file]
for tweet in tweets:
    tweet_data = {}
    if re.search(r'http[s]?:
        tweet_data['text'] = tweet
        tweet_data['sentiment'] = get_tweet_sentiment(tweet)
        tweets_url_yes.append(tweet_data)
    else:
        tweet_data['text'] = tweet
        tweet_data['sentiment'] = get_tweet_sentiment(tweet)
        tweets_url_no.append(tweet_data)
def print_sentiment_analysis(tweets, label):
    if tweets:
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        neuttweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        print(f"\n\n{label} Positive tweets percentage: {100*len(ptweets)/len(tweets):.2f} %")
        print(f"{label} Negative tweets percentage: {100*len(ntweets)/len(tweets):.2f} %")
        print(f"{label} Neutral tweets percentage: {100*len(neuttweets)/len(tweets):.2f} %")
        print(f"\n\n{label} Positive tweets:")
        for tweet in ptweets:
            print(f"{tweet['text']}")
        print(f"\n\n{label} Negative tweets:")
        for tweet in ntweets:
            print(f"{tweet['text']}")
        print(f"\n\n{label} Neutral tweets:")
        for tweet in neuttweets:
            print(f"{tweet['text']}")
    else:
        print(f"No {label.lower()} tweets found.")
print_sentiment_analysis(tweets_url_yes, "Tweets with URLs")
print_sentiment_analysis(tweets_url_no, "Tweets without URLs")