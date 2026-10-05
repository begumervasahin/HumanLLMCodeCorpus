import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def fonk1(b1):
    return [item[0] for item in b8.items() if b1 = = item[1]][0]
def fonk2(b13, b9, b27, b26):
    b13.get(b9)
    time.sleep(2)
    b2 = b13.find_element_by_id('identifierId')
    b2.send_keys(b27)
    b2.send_keys(Keys.RETURN)
    time.sleep(2)
    b3 = b13.find_element_by_class_name('whsOnd')
    b3.send_keys(b26)
    time.sleep(2)
    b3.send_keys(Keys.RETURN)
b4 = ['school_url', 'sciencesurvey_url']
b5 = ['email_url_1', 'email_url_2', 'email_url_3']
b6 = ['xkcd_url', 'blog_url']
b7 = ['social_media_url']
b8 = {
    'twitter': 'twitter_url',
    'instagram': 'instagram_url',
    'github': 'github_url',
    'linkedin': 'linkedin_url',
    'kaggle': 'kaggle_url',
    'mail': 'mail_url',
    'mail0': 'mail0_url',
    'mail1': 'mail1_url',
    'mail2': 'mail2_url',
    'xkcd': 'xkcd_url',
    'blog': 'blog_url',
    'school': 'school_url',
    'sciencesurvey': 'sciencesurvey_url'
}
class class1:
    def fonk3(self):
        self.b9 = 'https:
        self.b10 = "/Users/ramanshsharma/Downloads/chromedriver"
        self.b11 = webdriver.ChromeOptions()
        self.b11.add_experimental_option("detach", True)
        self.b12 = pd.read_csv('secrets.csv')
        self.b13 = None
        self.b14 = {
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
    def fonk4(self, b9 = None):
        if b9 is not None:
            self.b9 = b9
        b15 = fonk1(self.b9)
        self.b13 = webdriver.Chrome(self.b10,
                                       b11 = self.b11)
        if b15 in ['mail0', 'mail1', 'mail2']:
            self.b14['mail'](b16 = int(b15[-1]))
        elif b15 in ['school', 'sciencesurvey', 'xkcd', 'blog']:
            self.b14[b15](b17 = b15)
        else:
            self.b14[b15]()
    def fonk5(self, b17 = None):
        if b17 = = 'school' or b17 is None:
            self.b9 = b4[0]
        elif b17 = = 'sciencesurvey':
            self.b9 = b4[1]
        self.b13.get(self.b9)
    def fonk6(self):
        self.b13.get(self.b9)
        time.sleep(2)
        b18 = self.b13.find_element_by_id('login-b27')
        b18.send_keys(self.b12.iloc[4, 1])
        time.sleep(2)
        b19 = self.b13.find_element_by_id('login-b26')
        time.sleep(2)
        b19.send_keys(self.b12.iloc[4, 2])
        time.sleep(2)
        b19.send_keys(Keys.RETURN)
    def fonk7(self):
        self.b13.get(self.b9)
        time.sleep(2)
        b20 = self.b13.find_element_by_link_text('Log in')
        b20.click()
        time.sleep(1)
        b18 = self.b13.find_element_by_class_name('b27-input')
        b18.send_keys(self.b12.iloc[0, 1])
        time.sleep(2)
        b19 = self.b13.find_element_by_name('session[b26]')
        b19.send_keys(self.b12.iloc[0, 2])
        time.sleep(2)
        b19.send_keys(Keys.RETURN)
    def fonk8(self):
        self.b13.get(self.b9)
        time.sleep(2)
        b21 = self.b13.find_element_by_link_text('Log in')
        b21.click()
        time.sleep(2)
        b22 = self.b13.find_element_by_class_name('_2hvTZ')
        b22.send_keys(self.b12.iloc[2, 1])
        time.sleep(2)
        b23 = self.b13.find_elements_by_class_name('_2hvTZ')[1]
        b23.send_keys(self.b12.iloc[2, 2])
        time.sleep(2)
        b23.send_keys(Keys.RETURN)
    def fonk9(self):
        self.b13.get(self.b9)
        time.sleep(2)
        b24 = self.b13.find_element_by_link_text('Sign in')
        b24.click()
        b24 = self.b13.find_element_by_id('login_field')
        time.sleep(2)
        b24.send_keys(self.b12.iloc[1, 1])
        time.sleep(2)
        b24 = self.b13.find_element_by_id('b26')
        time.sleep(2)
        b24.send_keys(self.b12.iloc[1, 2])
        time.sleep(2)
        b24.send_keys(Keys.RETURN)
    def fonk10(self):
        self.b13.get(self.b9)
        time.sleep(2)
        b20 = self.b13.find_element_by_class_name('button--small')
        b20.click()
        b18 = self.b13.find_element_by_id('username-input-text')
        b18.send_keys(self.b12.iloc[4, 1])
        time.sleep(2)
        b19 = self.b13.find_element_by_id('b26-input-text')
        b19.send_keys(self.b12.iloc[4, 2])
        time.sleep(2)
        b25 = self.b13.find_element_by_link_text('Sign in')
        b25.click()
    def fonk11(self, b16 = None):
        if b16 is None:
            self.b9 = b5[0]
            b27, b26 = self.b12.iloc[5, 1], self.b12.iloc[5, 2]
            fonk2(self.b13, self.b9, b27, b26)
            b27, b26 = self.b12.iloc[6, 1], self.b12.iloc[6, 2]
            time.sleep(2)
            self.b9 = b5
            [1]
            self.b13.execute_script(f'window.open({self.b9}, "_blank");')
            fonk2(self.b13, self.b9, b27, b26)
            b27, b26 = self.b12.iloc[7, 1], self.b12.iloc[7, 2]
            time.sleep(2)
            self.b9 = b5[2]
            self.b13.execute_script(f'window.open({self.b9}, "_blank");')
            fonk2(self.b13, self.b9, b27, b26)
        else:
            self.b9 = b5[b16]
            b27 = self.b12.iloc[b16 + 5, 1]
            b26 = self.b12.iloc[b16 + 5, 2]
            fonk2(self.b13, self.b9, b27, b26)
    def fonk12(self, b17):
        if b17 = = 'xkcd':
            self.b9 = b6[0]
        elif b17 = = 'blog':
            self.b9 = b6[1]
        self.b13.get(self.b9)
if b28 = = '__main__':
    b29 = class1()
    b29.fonk4(b7[0])