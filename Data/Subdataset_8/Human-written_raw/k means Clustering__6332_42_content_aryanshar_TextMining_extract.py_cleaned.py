import re
from textblob import TextBlob
def get_tweet_sentiment(tweet):
	'''
	Utility function to classify sentiment of passed tweet
	using textblob's sentiment method
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
with open("tweets 123.txt", 'r') as data:
	tweets = [line.strip() for line in data]
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
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
	ntweets = [tweet for tweet in tweets_url_yes if tweet_with_url['sentiment'] == 'negative']
	neuttweets = [tweet for tweet in tweets_url_yes if tweet_with_url['sentiment'] == 'neutral']
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
	print("\n\nPositive tweets:")
	for tweet in ptweets[:]:
		print("%s" % tweet['text'])
	print("\n\nNegative tweets:")
	for tweet in ntweets[:]:
		print("%s" % tweet['text'])
	print("\n\nNeutral tweets:")
	for tweet in neuttweets[:]:
		print("%s" % tweet['text'])