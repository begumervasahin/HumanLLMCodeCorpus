import tweepy
import argparse
b1 = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
b2 = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
b3 = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
b4 = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
b5 = tweepy.OAuthHandler(b1, b2)
b5.set_access_token(b3, b4)
b6 = tweepy.API(b5)
def fonk1(screen_name):
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
def fonk2():
    b7 = fonk1("emmanuelmuthui")
    b11 = '{:<30} {:<30} {}'.format("Tweet ID", "Date Posted", "Tweet")
    print(b11)
    print('-' * len(b11))
    for key in b7:
        print('{:<30} {:<30} {}'.format(str(key), str(b7[key][1]), b7[key][0]))
def fonk3():
    b7 = fonk1("emmanuelmuthui")
    b12 = {}
    for key in b7:
        b13 = b7[key][0].split()
        for word in b13:
            if word.lower() in b14:
                continue
            b12[word] = b12.get(word, 0) + 1
    for word, freq in b12.items():
        print(f"{word}: {freq}")
b14 = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'it', 'you', 'that', 'on', 'for', 'with', 'as', 'this', 'was', 'are', 'but', 'be'}
b15 = argparse.ArgumentParser(description='Process some integers.')
b15.add_argument('integers', b16 = 'N', type=int, nargs='+', help='an integer for the accumulator')
b15.add_argument('--sum', b17 = 'accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
b18 = b15.parse_args()
print(b18.accumulate(b18.integers))