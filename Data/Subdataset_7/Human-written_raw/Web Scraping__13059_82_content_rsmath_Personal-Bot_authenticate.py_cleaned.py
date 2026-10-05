
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import commands
from links import SCHOOL, CONST_EMAILS, BLOGS, SOCIAL_MEDIA
class class1:
    def fonk1(self):
        self.b1 = 'https:
        self.b2 = "/Users/ramanshsharma/Downloads/chromedriver"
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
    def fonk2(self, b1 = None):
        if b1 is not None:
            self.b1 = b1
        b7 = fonk11(self.b1)
        self.b5 = webdriver.Chrome(self.b2,
                                       b3 = self.b3)
        if b7 = = 'mail0' or b7 == 'mail1' or b7 == 'mail2':
            self.b6[b7](b8 = int(b7[-1]))
        elif b7 = = 'school' or b7 == 'sciencesurvey':
            self.b6[b7](b9 = b7)
        elif b7 = = 'xkcd' or b7 == 'blog':
            self.b6[b7](b9 = b7)
        else:
            self.b6[b7]()
    def fonk3(self, b9 = None):
        if b9 = = 'school' or b9 is None:
            self.b1 = SCHOOL[0]
        elif b9 = = 'sciencesurvey':
            self.b1 = SCHOOL[1]
        self.b5.get(self.b1)
    def fonk4(self):
        self.b5.get(self.b1)
        time.sleep(2)
        b10 = self.b5.find_element_by_id('login-b19')
        b10.send_keys(self.b4.iloc[4, 1])
        time.sleep(2)
        b11 = self.b5.find_element_by_id('login-b18')
        time.sleep(2)
        b11.send_keys(self.b4.iloc[4, 2])
        time.sleep(2)
        b11.send_keys(Keys.RETURN)
    def fonk5(self):
        self.b5.get(self.b1)
        time.sleep(2)
        b12 = self.b5.find_element_by_link_text('Log in')
        b12.click()
        time.sleep(1)
        b10 = self.b5.find_element_by_class_name('b19-input')
        b10.send_keys(self.b4.iloc[0, 1])
        time.sleep(2)
        b11 = self.b5.find_element_by_name('session[b18]')
        b11.send_keys(self.b4.iloc[0, 2])
        time.sleep(2)
        b11.send_keys(Keys.RETURN)
    def fonk6(self):
        self.b5.get(self.b1)
        time.sleep(2)
        b13 = self.b5.find_element_by_link_text('Log in')
        b13.click()
        time.sleep(2)
        b14 = self.b5.find_element_by_class_name('_2hvTZ')
        b14.send_keys(self.b4.iloc[2, 1])
        time.sleep(2)
        b15 = self.b5.find_elements_by_class_name('_2hvTZ')[1]
        b15.send_keys(self.b4.iloc[2, 2])
        time.sleep(2)
        b15.send_keys(Keys.RETURN)
    def fonk7(self):
        self.b5.get(self.b1)
        time.sleep(2)
        b16 = self.b5.find_element_by_link_text('Sign in')
        b16.click()
        b16 = self.b5.find_element_by_id('login_field')
        time.sleep(2)
        b16.send_keys(self.b4.iloc[1, 1])
        time.sleep(2)
        b16 = self.b5.find_element_by_id('b18')
        time.sleep(2)
        b16.send_keys(self.b4.iloc[1, 2])
        time.sleep(2)
        b16.send_keys(Keys.RETURN)
    def fonk8(self):
        self.b5.get(self.b1)
        time.sleep(2)
        b12 = self.b5.find_element_by_class_name('button--small')
        b12.click()
        b10 = self.b5.find_element_by_id('username-input-text')
        b10.send_keys(self.b4.iloc[4, 1])
        time.sleep(2)
        b11 = self.b5.find_element_by_id('b18-input-text')
        b11.send_keys(self.b4.iloc[4, 2])
        time.sleep(2)
        b17 = self.b5.find_element_by_link_text('Sign in')
        b17.click()
    def fonk9(self, b8 = None):
        if b8 is None:
            self.b1 = CONST_EMAILS[0]
            b19, b18 = self.b4.iloc[5, 1], self.b4.iloc[5, 2]
            fonk12(self.b5, self.b1, b19, b18)
            b19, b18 = self.b4.iloc[6, 1], self.b4.iloc[6, 2]
            time.sleep(2)
            self.b1 = CONST_EMAILS[1]
            self.b5.execute_script(f'window.open({self.b1}, "_blank");')
            fonk12(self.b5, self.b1, b19, b18)
            b19, b18 = self.b4.iloc[7, 1], self.b4.iloc[7, 2]
            time.sleep(2)
            self.b1 = CONST_EMAILS[2]
            self.b5.execute_script(f'window.open({self.b1}, "_blank");')
            fonk12(self.b5, self.b1, b19, b18)
        else:
            self.b1 = CONST_EMAILS[b8]
            b19 = self.b4.iloc[b8 + 5, 1]
            b18 = self.b4.iloc[b8 + 5, 2]
        fonk12(self.b5, self.b1, b19, b18)
    def fonk10(self, b9):
        if b9 = = 'xkcd':
            self.b1 = BLOGS[0]
        elif b9 = = 'blog':
            self.b1 = BLOGS[1]
        self.b5.get(self.b1)
def fonk11(b20):
    return [item[0] for item in commands.items() if b20 = = item[1]][0]
def fonk12(b5, b1, b19, b18):
    b5.get(b1)
    time.sleep(2)
    b21 = b5.find_element_by_id('identifierId')
    b21.send_keys(b19)
    b21.send_keys(Keys.RETURN)
    time.sleep(2)
    b22 = b5.find_element_by_class_name('whsOnd')
    b22.send_keys(b18)
    time.sleep(2)
    b22.send_keys(Keys.RETURN)
if b23 = = '__main__':
    b24 = class1()
    b24.fonk2(SOCIAL_MEDIA[0])