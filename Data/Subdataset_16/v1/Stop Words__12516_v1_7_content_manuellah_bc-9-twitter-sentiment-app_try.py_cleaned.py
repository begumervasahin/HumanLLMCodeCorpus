import tweepy
import csv
import argparse
b1 = 'EzfVwFMj3IzAUXMzvXLX9gHaF'
b2 = "Y1Gnr2oklcYGFbTryr3yDiiXgIWKAmPUVyouyr4NbRg8wmsjMT"
b3 = "588855017-vZ5eQksRsgei2Jc2Wfev22DY2yWdk748ds7EiHFb"
b4 = "dJvDBNYHxhDO67I1B61bsd7P7S1j1PCkee4LI7fLjVW2b"
b5 = tweepy.OAuthHandler(b1, b2)
b5.set_access_token(b3, b4)
b6 = tweepy.API(b5)
def fonk1(b22):
    b7 = {}
    b8 = []
    b9 = b6.user_timeline(b22=b22, count=200)
    b8.extend(b9)
    if not b8:
        b7[0] = ("No tweet so far", "00/00/00")
        return b7
    b10 = b8[-1].id - 1
    while b9:
        b9 = b6.user_timeline(b22=b22, count=200, max_id=b10)
        b8.extend(b9)
        b10 = b8[-1].id - 1
    for tweet in b8:
        b7[tweet.id] = (tweet.text, tweet.created_at)
    return b7
def fonk2(b22):
    b11 = fonk1(b22)
    b12 = '{:<30} {:<30} {}'.format("Tweeter ID", "Date Posted", "The Tweet")
    print(b12)
    for key in b11:
        print('{:<30} {:<30} {}'.format(str(key), str(b11[key][1]), b11[key][0]))
def fonk3(b22):
    b11 = fonk1(b22)
    b13 = {}
    b14 = set()
    for key in b11:
        b15 = str(b11[key][0]).split()
        for word in b15:
            if word in b14:
                continue
            if word not in b13:
                b13[word] = 1
            else:
                b13[word] += 1
    for word, count in b13.items():
        print(f"{word}: {count}")
def fonk4():
    b16 = argparse.ArgumentParser(description='Process some integers.')
    b16.add_argument('integers', b17 = 'N', type=int, nargs='+',
                        b18 = 'an integer for the accumulator')
    b16.add_argument('--sum', b19 = 'accumulate', action='store_const',
                        b20 = sum, default=max,
                        b18 = 'sum the integers (default: find the max)')
    b21 = b16.parse_args()
    print(b21.accumulate(b21.integers))
    b22 = "emmanuelmuthui"
    fonk2(b22)
    fonk3(b22)
if b23 = = "__main__":
    fonk4()