import tweepy
import progressbar
from colorama import init, Fore
from config import *
init()
class class1:
    '''
    This class class2 frequent tweets of a particular Twitter user, analyzes the tweets,
    and returns the most frequently used words with their frequencies.
    '''
    b1 = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    b1.b2 = True
    b1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    b3 = tweepy.API(b1)
    def fonk1(self, b5, b4 = 3200):
        '''
        Initializes the class1 object with the b5 and maximum number of tweets to fetch.
        '''
        self.b5 = b5
        self.b4 = b4
    def fonk2(self):
        '''
        Fetches data from Twitter for the specified user and stores it in a dictionary.
        '''
        try:
            b6 = {}
            b7 = []
            print()
            while len(b7) < self.b4:
                b8 = min(self.b4 - len(b7), 200)
                b9 = class1.b3.user_timeline(self.b5, b8=b8)
                if not b9:
                    break
                b7.extend(b9)
                b10 = b7[-1].id - 1
                for tweet in b9:
                    b6[tweet.id] = (tweet.text, tweet.created_at)
            return b6
        except tweepy.error.TweepError as e:
            print(Fore.RED + "Error fetching tweets. Please double-check the Twitter handle and try again.")
    def fonk3(self):
        '''
        Displays fetched tweets.
        '''
        b11 = self.fonk2()
        b12 = f'{Fore.BLUE}\nTWITTER ID'.ljust(30) + f'{Fore.BLUE}DATE POSTED'.ljust(30) + f'{Fore.BLUE}THE TWEET\n\n' + "==" * 70
        print(b12)
        try:
            for key, (tweet_text, created_at) in b11.items():
                print(f'{Fore.YELLOW}{str(key).ljust(30)}{Fore.GREEN}{str(created_at).ljust(30)}{Fore.RED}{tweet_text}')
        except TypeError:
            print(Fore.RED + "No tweets available for this Twitter handle.")
    def fonk4(self):
        '''
        Analyses the fetched tweets and returns the most frequent words (excluding stop words).
        '''
        b11 = self.fonk2()
        b13 = {}
        for key in b11:
            b14 = str(b11[key][0]).lower().split()
            for word in b14:
                if word in stop_words:
                    continue
                b13[word] = b13.get(word, 0) + 1
        b15 = sorted(b13.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f'{Fore.BLUE}\n\nCOMMON TWEETED WORD'.ljust(30) + f'{Fore.BLUE}THE FREQUENCY\n'.ljust(30) + '\n\n' + "==" * 70 + '\n\n')
        for word, freq in b15:
            print(f' {Fore.YELLOW}{word.ljust(30)}{Fore.GREEN}{str(freq).ljust(30)}')
