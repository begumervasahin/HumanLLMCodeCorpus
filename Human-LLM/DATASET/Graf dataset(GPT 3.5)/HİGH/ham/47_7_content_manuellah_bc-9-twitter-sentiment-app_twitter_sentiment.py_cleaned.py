import tweepy, progressbar
from config import *
from colorama import *
init()
class class1(object):
    '''
    This class class2 fetch a particular tweeter user's frequent tweets, analyse the tweets and return the most used used words with their frequency
    '''
    b1 = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    b1.b2 = True
    b1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    b3 = tweepy.API(b1)
    def fonk1(self, b5, b4 = 3200):
        '''
        initialises the b5 whose data is to be fetched(tweets)
        '''
        self.b5 = b5
        self.b6 = b4
    def fonk2(self ):
        '''
        This method fetchs data from twitter for a specific user and stores it in a json file
        '''
        try:
            b7 = dict()
            b8 = list()
            b9 = progressbar.ProgressBar(max_value = self.b6)
            print()
            if self.b6 <= 200:
                b10 = class1.b3.user_timeline(self.b5, count = self.b6)
                b8.extend(b10)
                if not b8:
                    b7[0] = "No tweet so far","00/00/00"
                    return b7
            else:
                b10 = class1.b3.user_timeline(self.b5, count=200)
                b8.extend(b10)
                self.b6 -= 200
                b11 = b8[-1].id - 1
                while b10:
                    if self.b6 <= 200:
                        b10 = class1.b3.user_timeline(self.b5, count = self.b6)
                        b8.extend(b10)
                    else:
                        b10 = class1.b3.user_timeline(self.b5, count = 200, max_id = b11)
                        b8.extend(b10)
                        b11 = b8[-1].id - 1
                        self.b6 -= 200
            for tweet in b8:
                    b7[tweet.id] = (tweet.text, tweet.created_at)
            return b7
        except tweepy.error.TweepError as e:
            print( Fore.RED + "No such twitter handle or is a private account and you a not following him/her, Please do recheck the spelling and write it again")
    def fonk3(self):
        b12 = self.fonk2()
        b13 = '{} {} {} {}'.format(Fore.BLUE + "\nTWITTER ID".ljust(30) ,Fore.BLUE + "DATE POSTED".ljust(30) ,Fore.BLUE + "THE TWEET\n\n", "=="*70)
        print(b13)
        try:
            for key in b12:
                print('{} {} {}'.format(Fore.YELLOW + str(key).ljust(30) , Fore.GREEN + str(b12[key][1]).ljust(30) , Fore.RED + b12[key][0]))
        except TypeError as e:
            print( Fore.RED + "No tweets for this particular twitter handle")
    def fonk4(self):
        '''
        This method takes the json file created in fetch data method and analyses the most frequent tweets words for that  user eliminating the stop words.
        Return a with dictictionary where word is a key and the frequency is the value)
        '''
        b12 = self.fonk2()
        b14 = dict()
        for key in b12:
            b15 = str(b12[key][0]).lower().split()
            for word in b15:
                if word in stop_words:
                    continue
                elif word not in list(b14):
                    b14[word] = 1
                else:
                    b14[word] += 1
        b16 = [(b14[key], key) for key in b14]
        b16.sort()
        b16 = b16[::-1]
        b16 = b16[:10]
        print('{} {} {} {} {} {}'.format(Fore.BLUE + "\n\n","COMMON TWEETED WORD".ljust(30), Fore.BLUE + "THE FREQUENCY\n".ljust(30), '\n\n', "=="*70 , "\n\n"))
        for freq, word in b16:
            print(' {} {}'.format(Fore.YELLOW + word.ljust(30), Fore.GREEN + str(freq).ljust(30)))