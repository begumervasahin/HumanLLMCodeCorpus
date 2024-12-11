import tweepy
import progressbar
from colorama import init, Fore
from config import API_KEYS, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
init()
b1 = []
class class1(object):
    '''
    This class class2 fetch a particular tweeter user's frequent tweets, analyse the tweets and return the most used used words with their frequency
    '''
    b2 = tweepy.OAuthHandler(API_KEYS, API_SECRET)
    b2.b3 = True
    b2.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    b4 = tweepy.API(b2)
    def fonk1(self, b6, b5 = 3200):
        '''
        initialises the b6 whose data is to be fetched(tweets)
        '''
        self.b6 = b6
        self.b7 = b5
    def fonk2(self):
        '''
        This method fetchs data from twitter for a specific user and stores it in a json file
        '''
        try:
            b8 = dict()
            b9 = list()
            b10 = progressbar.ProgressBar(max_value=self.b7)
            print()
            if self.b7 <= 200:
                b11 = class1.b4.user_timeline(self.b6, count=self.b7)
                b9.extend(b11)
                if not b9:
                    b8[0] = "No tweet so far", "00/00/00"
                    return b8
            else:
                b11 = class1.b4.user_timeline(self.b6, count=200)
                b9.extend(b11)
                self.b7 -= 200
                b12 = b9[-1].id - 1
                while b11:
                    if self.b7 <= 200:
                        b11 = class1.b4.user_timeline(self.b6, count=self.b7)
                        b9.extend(b11)
                    else:
                        b11 = class1.b4.user_timeline(self.b6, count=200, max_id=b12)
                        b9.extend(b11)
                        b12 = b9[-1].id - 1
                        self.b7 -= 200
            for tweet in b9:
                b8[tweet.id] = (tweet.text, tweet.created_at)
            return b8
        except tweepy.error.TweepError as e:
            print(Fore.RED + "No such twitter handle or is a private account and you are not following him/her, Please do recheck the spelling and write it again")
    def fonk3(self):
        b13 = self.fonk2()
        b14 = '{} {} {} {}'.format(Fore.BLUE + "\nTWITTER ID".ljust(30), Fore.BLUE + "DATE POSTED".ljust(30),
                                      Fore.BLUE + "THE TWEET\n\n", "==" * 70)
        print(b14)
        try:
            for key in b13:
                print('{} {} {}'.format(Fore.YELLOW + str(key).ljust(30), Fore.GREEN + str(b13[key][1]).ljust(30),
                                         Fore.RED + b13[key][0]))
        except TypeError as e:
            print(Fore.RED + "No tweets for this particular twitter handle")
    def fonk4(self):
        '''
        This method takes the json file created in fetch data method and analyses the most frequent tweets words for that  user eliminating the stop words.
        Return a with dictictionary where word is a key and the frequency is the value)
        '''
        b13 = self.fonk2()
        b15 = dict()
        for key in b13:
            b16 = str(b13[key][0]).lower().split()
            for word in b16:
                if word in b1:
                    continue
                elif word not in list(b15):
                    b15[word] = 1
                else:
                    b15[word] += 1
        b17 = [(b15[key], key) for key in b15]
        b17.sort()
        b17 = b17[::-1]
        b17 = b17[:10]
        print('{} {} {} {} {} {}'.format(Fore.BLUE + "\n\n", "COMMON TWEETED WORD".ljust(30),
                                         Fore.BLUE + "THE FREQUENCY\n".ljust(30), '\n\n', "==" * 70, "\n\n"))
        for freq, word in b17:
            print(' {} {}'.format(Fore.YELLOW + word.ljust(30), Fore.GREEN + str(freq).ljust(30)))
if b18 = = "__main__":
    b6 = input("Enter the Twitter b6: ")
    b19 = class1(b6)
    b19.fonk3()
    b19.fonk4()