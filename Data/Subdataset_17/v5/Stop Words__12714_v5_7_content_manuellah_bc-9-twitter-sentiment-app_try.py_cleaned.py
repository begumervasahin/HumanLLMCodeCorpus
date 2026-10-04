import tweepy
import argparse
API_KEYS = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
API_SECRET = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
ACCESS_TOKEN = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
ACCESS_TOKEN_SECRET = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)
api = authenticate_twitter()
def get_all_tweets(screen_name):
    tweets_dict = {}
    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    all_tweets.extend(new_tweets)
    if not all_tweets:
        tweets_dict[0] = ("No tweet so far", "00/00/00")
        return tweets_dict
    oldest = all_tweets[-1].id - 1
    while new_tweets:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
    for tweet in all_tweets:
        tweets_dict[tweet.id] = (tweet.text, tweet.created_at)
    return tweets_dict
def display_tweets(screen_name):
    tweets_dict = get_all_tweets(screen_name)
    header = '{:<30} {:<30} {}'.format("Tweet ID", "Date Posted", "Tweet")
    print(header)
    print('-' * len(header))
    for tweet_id, tweet_info in tweets_dict.items():
        print('{:<30} {:<30} {}'.format(str(tweet_id), str(tweet_info[1]), tweet_info[0]))
def frequency_analyzer(screen_name):
    tweets_dict = get_all_tweets(screen_name)
    freq_dict = {}
    for tweet_id, tweet_info in tweets_dict.items():
        tweet_words = tweet_info[0].split()
        for word in tweet_words:
            word_lower = word.lower()
            if word_lower in stop_words:
                continue
            freq_dict[word_lower] = freq_dict.get(word_lower, 0) + 1
    for word, freq in freq_dict.items():
        print(f"{word}: {freq}")
stop_words = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'it', 'you', 'that', 'on', 'for', 'with', 'as', 'this', 'was', 'are', 'but', 'be'}
def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    return parser.parse_args()
if __name__ == "__main__":
    args = parse_arguments()
    print(args.accumulate(args.integers))