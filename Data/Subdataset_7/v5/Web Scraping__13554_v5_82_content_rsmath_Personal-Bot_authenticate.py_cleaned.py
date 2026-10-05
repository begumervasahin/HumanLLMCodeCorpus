import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import commands
from links import SCHOOL, CONST_EMAILS, BLOGS, SOCIAL_MEDIA
class class1:
    def fonk1(self, b1 = "/Users/ramanshsharma/Downloads/chromedriver"):
        self.b2 = 'https:
        self.b1 = b1
        self.b3 = webdriver.ChromeOptions()
        self.b3.add_experimental_option("detach", True)
        self.b4 = pd.read_csv('secrets.csv')
        self.b5 = None
        self.b6 = {
            'twitter': self.get_twitter,
            'instagram': self.get_instagram,
            'github': self.get_github,
            'linkedin': self.get_linkedin,
            'kaggle': self.get_kaggle,
            'mail': self.get_mail,
            'mail0': self.get_mail,
            'mail1': self.get_mail,
            'mail2': self.get_mail,
            'xkcd': self.get_xkcd,
            'blog': self.get_xkcd,
            'school': self.get_school,
            'sciencesurvey': self.get_school
        }
    def fonk2(self, b2 = None):
        if b2:
            self.b2 = b2
        b7 = fonk11(self.b2)
        self.b5 = webdriver.Chrome(self.b1, b3=self.b3)
        if b7.startswith('mail'):
            self.b6['mail'](int(b7[-1]))
        elif b7 in ['school', 'sciencesurvey', 'xkcd', 'blog']:
            self.b6[b7](b8 = b7)
        else:
            self.b6[b7]()
    def fonk3(self, b8 = None):
        self.b2 = SCHOOL[0] if not b8 or b8 == 'school' else SCHOOL[1]
        self.b5.get(self.b2)
    def fonk4(self):
        self.b5.get(self.b2)
        time.sleep(2)
        b9 = self.b5.find_element_by_id('login-b17')
        b9.send_keys(self.b4.iloc[4, 1])
        time.sleep(2)
        b10 = self.b5.find_element_by_id('login-b16')
        time.sleep(2)
        b10.send_keys(self.b4.iloc[4, 2])
        time.sleep(2)
        b10.send_keys(Keys.RETURN)
    def fonk5(self):
        self.b5.get(self.b2)
        time.sleep(2)
        b11 = self.b5.find_element_by_link_text('Log in')
        b11.click()
        time.sleep(1)
        b9 = self.b5.find_element_by_class_name('b17-input')
        b9.send_keys(self.b4.iloc[0, 1])
        time.sleep(2)
        b10 = self.b5.find_element_by_name('session[b16]')
        b10.send_keys(self.b4.iloc[0, 2])
        time.sleep(2)
        b10.send_keys(Keys.RETURN)
    def fonk6(self):
        self.b5.get(self.b2)
        time.sleep(2)
        b12 = self.b5.find_element_by_link_text('Log in')
        b12.click()
        time.sleep(2)
        b13 = self.b5.find_element_by_class_name('_2hvTZ')
        b13.send_keys(self.b4.iloc[2, 1])
        time.sleep(2)
        b10 = self.b5.find_elements_by_class_name('_2hvTZ')[1]
        b10.send_keys(self.b4.iloc[2, 2])
        time.sleep(2)
        b10.send_keys(Keys.RETURN)
    def fonk7(self):
        self.b5.get(self.b2)
        time.sleep(2)
        b14 = self.b5.find_element_by_link_text('Sign in')
        b14.click()
        time.sleep(2)
        b9 = self.b5.find_element_by_id('login_field')
        time.sleep(2)
        b9.send_keys(self.b4.iloc[1, 1])
        time.sleep(2)
        b10 = self.b5.find_element_by_id('b16')
        time.sleep(2)
        b10.send_keys(self.b4.iloc[1, 2])
        time.sleep(2)
        b10.send_keys(Keys.RETURN)
    def fonk8(self):
        self.b5.get(self.b2)
        time.sleep(2)
        b11 = self.b5.find_element_by_class_name('button--small')
        b11.click()
        b9 = self.b5.find_element_by_id('username-input-text')
        b9.send_keys(self.b4.iloc[4, 1])
        time.sleep(2)
        b10 = self.b5.find_element_by_id('b16-input-text')
        b10.send_keys(self.b4.iloc[4, 2])
        time.sleep(2)
        b14 = self.b5.find_element_by_link_text('Sign in')
        b14.click()
    def fonk9(self, b15 = None):
        if b15 is None:
            for i in range(3):
                self.b2 = CONST_EMAILS[i]
                b17, b16 = self.b4.iloc[i + 5, 1], self.b4.iloc[i + 5, 2]
                fonk12(self.b5, self.b2, b17, b16)
        else:
            self.b2 = CONST_EMAILS[b15]
            b17 = self.b4.iloc[b15 + 5, 1]
            b16 = self.b4.iloc[b15 + 5, 2]
            fonk12(self.b5, self.b2, b17, b16)
    def fonk10(self, b8):
        self.b2 = BLOGS[0] if b8 == 'xkcd' else BLOGS[1]
        self.b5.get(self.b2)
def fonk11(b18):
    return [item[0] for item in commands.items() if b18 = = item[1]][0]
def fonk12(b5, b2, b17, b16):
    b5.get(b2)
    time.sleep(2)
    b19 = b5.find_element_by_id('identifierId')
    b19.send_keys(b17)
    b19.send_keys(Keys.RETURN)
    time.sleep(2)
    b20 = b5.find_element_by_class_name('whsOnd')
    b20.send_keys(b16)
    time.sleep(2)
    b20.send_keys(Keys.RETURN)
if b21 = = '__main__':
    b22 = class1()
    b22.fonk2(SOCIAL_MEDIA[0])