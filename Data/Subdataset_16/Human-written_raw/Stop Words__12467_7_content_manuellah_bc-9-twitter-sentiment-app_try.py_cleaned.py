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
def fonk1(screen_name):
    b7 = dict()
    b8 = list()
    b9 = b6.user_timeline(screen_name = screen_name,count=200)
    b8.extend(b9)
    if not b8:
        b7[0] = "No tweet so far","00/00/00"
        return b7
    b10 = b8[-1].id - 1
    while b9:
        b9 = b6.user_timeline(screen_name = screen_name, count=200, max_id=b10)
        b8.extend(b9)
        b10 = b8[-1].id - 1
    for tweet in b8:
        b7[tweet.id] = (tweet.text,tweet.created_at)
    return b7
def fonk2():
    b11 = fonk1("emmanuelmuthui")
    b12 = '{} {} {}'.format("tweeter id".ljust(30),"Date Posted".ljust(30) ,"The Tweet")
    print(b12)
    for key in b11:
        print('{} {} {}'.format(str(key).ljust(30), str(b11[key][1]).ljust(30) , b11[key][0]))
def fonk3():
    b11 = fonk1("emmanuelmuthui")
    b13 = list()
    b14 = dict()
    for key in b11:
        b15 = str(b11[key][0]).split()
        for word in b15:
            if word in stop_words:
                continue
            elif word not in list(b14):
                b14[word] = 1
            b14[word] += 1
b16 = argparse.ArgumentParser(description='Process some integers.')
b16.add_argument('integers', b17 = 'N', type=int, nargs='+',
                    b18 = 'an integer for the accumulator')
b16.add_argument('--sum', b19 = 'accumulate', action='store_const',
                    b20 = sum, default=max,
                    b18 = 'sum the integers (default: find the max)')
b21 = b16.parse_args()
print(b21.accumulate(b21.integers))