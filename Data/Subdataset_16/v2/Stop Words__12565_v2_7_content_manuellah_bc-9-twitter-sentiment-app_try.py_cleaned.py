import tweepy
import argparse
b1 = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
b2 = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
b3 = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
b4 = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
b5 = tweepy.OAuthHandler(b1, b2)
b5.set_access_token(b3, b4)
b6 = tweepy.API(b5)
def fonk1(b21):
    b7 = {}
    b8 = []
    b9 = b6.user_timeline(b21=b21, count=200)
    b8.extend(b9)
    if not b8:
        b7[0] = ("No tweets so far", "00/00/00")
        return b7
    b10 = b8[-1].id - 1
    while b9:
        b9 = b6.user_timeline(b21=b21, count=200, max_id=b10)
        b8.extend(b9)
        b10 = b8[-1].id - 1
    for tweet in b8:
        b7[tweet.id] = (tweet.text, tweet.created_at)
    return b7
def fonk2(b21):
    b7 = fonk1(b21)
    b11 = '{:<30} {:<30} {}'.format("Tweet ID", "Date Posted", "Tweet Text")
    print(b11)
    print('-' * len(b11))
    for tweet_id, (text, created_at) in b7.items():
        print('{:<30} {:<30} {}'.format(tweet_id, created_at, text))
def fonk3(b21):
    b7 = fonk1(b21)
    b12 = {}
    b13 = set()
    for tweet_id, (text, created_at) in b7.items():
        b14 = text.split()
        for word in b14:
            if word in b13:
                continue
            if word not in b12:
                b12[word] = 1
            else:
                b12[word] += 1
    for word, count in b12.items():
        print(f"{word}: {count}")
def fonk4():
    b15 = argparse.ArgumentParser(description='Process some integers.')
    b15.add_argument('integers', b16 = 'N', type=int, nargs='+',
                        b17 = 'An integer for the accumulator')
    b15.add_argument('--sum', b18 = 'accumulate', action='store_const',
                        b19 = sum, default=max,
                        b17 = 'Sum the integers (default: find the max)')
    b20 = b15.parse_args()
    print(b20.accumulate(b20.integers))
    b21 = "emmanuelmuthui"
    fonk2(b21)
    fonk3(b21)
if b22 = = "__main__":
    fonk4()