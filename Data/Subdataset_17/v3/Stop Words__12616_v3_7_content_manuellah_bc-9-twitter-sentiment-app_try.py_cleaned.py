import tweepy
import argparse
API_KEY = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
API_SECRET_KEY = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
ACCESS_TOKEN = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
ACCESS_TOKEN_SECRET = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
def fetch_all_tweets(screen_name):
    tweet_dict = {}
    all_tweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    all_tweets.extend(new_tweets)
    if not all_tweets:
        tweet_dict[0] = ("No tweets so far", "00/00/00")
        return tweet_dict
    oldest = all_tweets[-1].id - 1
    while new_tweets:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
    for tweet in all_tweets:
        tweet_dict[tweet.id] = (tweet.text, tweet.created_at)
    return tweet_dict
def display_tweets(screen_name):
    tweet_dict = fetch_all_tweets(screen_name)
    header = '{:<30} {:<30} {}'.format("Tweet ID", "Date Posted", "Tweet Text")
    print(header)
    print('-' * len(header))
    for tweet_id, (text, created_at) in tweet_dict.items():
        print('{:<30} {:<30} {}'.format(tweet_id, created_at, text))
def analyze_word_frequency(screen_name):
    tweet_dict = fetch_all_tweets(screen_name)
    word_frequency = {}
    stop_words = set()
    for tweet_id, (text, created_at) in tweet_dict.items():
        words = text.split()
        for word in words:
            if word in stop_words:
                continue
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='An integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='Sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    screen_name = "emmanuelmuthui"
    display_tweets(screen_name)
    analyze_word_frequency(screen_name)
if __name__ == "__main__":
    main()