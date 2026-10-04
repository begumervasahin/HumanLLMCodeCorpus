import tweepy
import argparse
b1 = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
b2 = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
b3 = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
b4 = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
def fonk1():
    b5 = tweepy.OAuthHandler(b1, b2)
    b5.set_access_token(b3, b4)
    return tweepy.API(b5)
b6 = fonk1()
def fonk2(screen_name):
    b7 = {}
    b8 = []
    b9 = b6.user_timeline(screen_name=screen_name, count=200)
    b8.extend(b9)
    if not b8:
        b7[0] = ("No tweet so far", "00/00/00")
        return b7
    b10 = b8[-1].id - 1
    while b9:
        b9 = b6.user_timeline(screen_name=screen_name, count=200, max_id=b10)
        b8.extend(b9)
        b10 = b8[-1].id - 1
    for tweet in b8:
        b7[tweet.id] = (tweet.text, tweet.created_at)
    return b7
def fonk3(screen_name):
    b7 = fonk2(screen_name)
    b11 = '{:<30} {:<30} {}'.format("Tweet ID", "Date Posted", "Tweet")
    print(b11)
    print('-' * len(b11))
    for tweet_id, tweet_info in b7.items():
        print('{:<30} {:<30} {}'.format(str(tweet_id), str(tweet_info[1]), tweet_info[0]))
def fonk4(screen_name):
    b7 = fonk2(screen_name)
    b12 = {}
    for tweet_id, tweet_info in b7.items():
        b13 = tweet_info[0].split()
        for word in b13:
            b14 = word.lower()
            if b14 in b15:
                continue
            b12[b14] = b12.get(b14, 0) + 1
    for word, freq in b12.items():
        print(f"{word}: {freq}")
b15 = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'it', 'you', 'that', 'on', 'for', 'with', 'as', 'this', 'was', 'are', 'but', 'be'}
def fonk5():
    b16 = argparse.ArgumentParser(description='Process some integers.')
    b16.add_argument('integers', b17 = 'N', type=int, nargs='+', help='an integer for the accumulator')
    b16.add_argument('--sum', b18 = 'accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
    return b16.parse_args()
if b19 = = "__main__":
    b20 = fonk5()
    print(b20.accumulate(b20.integers))