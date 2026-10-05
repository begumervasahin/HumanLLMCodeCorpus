import tweepy
import progressbar
from colorama import init, Fore
from config import API_KEYS, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
init()
b1 = []
class class1:
    '''
    This class class2 a particular Twitter user's frequent tweets, analyzes the tweets, and returns the most used words with their frequency.
    '''
    b2 = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    b2.b3 = True
    b2.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    b4 = tweepy.API(b2)
    def fonk1(self, b6, b5 = 3200):
        '''
        Initializes the b6 whose data is to be fetched (tweets).
        '''
        self.b6 = b6
        self.b7 = b5
    def fonk2(self):
        '''
        Fetches data from Twitter for a specific user and stores it in a dictionary.
        '''
        try:
            b8 = {}
            b9 = []
            if self.b7 <= 200:
                b10 = class1.b4.user_timeline(self.b6, count=self.b7)
            else:
                b10 = class1.b4.user_timeline(self.b6, count=200)
            b9.extend(b10)
            self.b7 -= 200
            while len(b10) > 0 and self.b7 > 0:
                if self.b7 <= 200:
                    b10 = class1.b4.user_timeline(self.b6, count=self.b7)
                else:
                    b10 = class1.b4.user_timeline(self.b6, count=200, max_id=b9[-1].id - 1)
                b9.extend(b10)
                self.b7 -= 200
            for tweet in b9:
                b8[tweet.id] = (tweet.text, tweet.created_at)
            return b8
        except tweepy.error.TweepError as e:
            print(Fore.RED + "Error occurred: {}".format(e))
    def fonk3(self):
        '''
        Displays fetched tweets.
        '''
        b11 = self.fonk2()
        b12 = '{} {} {} {}'.format(Fore.BLUE + "\nTWITTER ID".ljust(30), Fore.BLUE + "DATE POSTED".ljust(30),
                                      Fore.BLUE + "THE TWEET\n\n", "==" * 70)
        print(b12)
        try:
            for key, (text, created_at) in b11.items():
                print('{} {} {}'.format(Fore.YELLOW + str(key).ljust(30), Fore.GREEN + str(created_at).ljust(30),
                                         Fore.RED + text))
        except TypeError as e:
            print(Fore.RED + "No tweets for this particular Twitter handle")
    def fonk4(self):
        '''
        Analyses the fetched tweet data and returns the most frequently used words, excluding stop words.
        '''
        b11 = self.fonk2()
        b13 = {}
        for key in b11:
            b14 = str(b11[key][0]).lower().split()
            for word in b14:
                if word in b1:
                    continue
                elif word not in b13:
                    b13[word] = 1
                else:
                    b13[word] += 1
        b15 = sorted(b13.items(), key=lambda x: x[1], reverse=True)[:10]
        print('{} {} {} {} {} {}'.format(Fore.BLUE + "\n\n", "COMMON TWEETED WORD".ljust(30),
                                         Fore.BLUE + "THE FREQUENCY\n".ljust(30), '\n\n', "==" * 70, "\n\n"))
        for word, freq in b15:
            print(' {} {}'.format(Fore.YELLOW + word.ljust(30), Fore.GREEN + str(freq).ljust(30)))
if b16 = = "__main__":
    b6 = input("Enter the Twitter b6: ")
    b17 = class1(b6)
    b17.fonk3()
    b17.fonk4()