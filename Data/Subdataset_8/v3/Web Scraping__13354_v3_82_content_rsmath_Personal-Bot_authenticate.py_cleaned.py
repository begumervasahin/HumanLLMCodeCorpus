import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def get_media_from_link(link):
    for media, url in commands.items():
        if link == url:
            return media
def enter_credentials(driver, email, password):
    email_input = driver.find_element_by_id('identifierId')
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)
    password_input = driver.find_element_by_class_name('whsOnd')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
SCHOOL_URLS = ['school_url', 'sciencesurvey_url']
EMAIL_URLS = ['email_url_1', 'email_url_2', 'email_url_3']
BLOG_URLS = ['xkcd_url', 'blog_url']
SOCIAL_MEDIA_URLS = ['social_media_url']
commands = {
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
class Websites:
    def __init__(self):
        self.starting_url = 'https:
        self.path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.credentials = pd.read_csv('secrets.csv')
        self.driver = None
        self.media_to_function = {
            'twitter': self.sign_in_twitter,
            'instagram': self.sign_in_instagram,
            'github': self.sign_in_github,
            'linkedin': self.sign_in_linkedin,
            'kaggle': self.sign_in_kaggle,
            'mail': self.sign_in_mail,
            'mail0': self.sign_in_mail,
            'mail1': self.sign_in_mail,
            'mail2': self.sign_in_mail,
            'xkcd': self.sign_in_blog,
            'blog': self.sign_in_blog,
            'school': self.sign_in_school,
            'sciencesurvey': self.sign_in_school
        }
    def sign_in(self, url=None):
        if url:
            self.starting_url = url
        media = get_media_from_link(self.starting_url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver, chrome_options=self.chrome_options)
        if media.startswith('mail'):
            self.sign_in_mail(int(media[-1]))
        elif media in ['school', 'sciencesurvey', 'xkcd', 'blog']:
            self.media_to_function[media](media)
        else:
            self.media_to_function[media]()
    def sign_in_school(self, spec=None):
        if not spec or spec == 'school':
            self.starting_url = SCHOOL_URLS[0]
        elif spec == 'sciencesurvey':
            self.starting_url = SCHOOL_URLS[1]
        self.driver.get(self.starting_url)
    def sign_in_linkedin(self):
        self.driver.get(self.starting_url)
        email = self.credentials.iloc[4, 1]
        password = self.credentials.iloc[4, 2]
        enter_credentials(self.driver, email, password)
    def sign_in_twitter(self):
        self.driver.get(self.starting_url)
        self.driver.find_element_by_link_text('Log in').click()
        email = self.credentials.iloc[0, 1]
        password = self.credentials.iloc[0, 2]
        enter_credentials(self.driver, email, password)
    def sign_in_instagram(self):
        self.driver.get(self.starting_url)
        self.driver.find_element_by_link_text('Log in').click()
        email = self.credentials.iloc[2, 1]
        password = self.credentials.iloc[2, 2]
        enter_credentials(self.driver, email, password)
    def sign_in_github(self):
        self.driver.get(self.starting_url)
        self.driver.find_element_by_link_text('Sign in').click()
        email = self.credentials.iloc[1, 1]
        password = self.credentials.iloc[1, 2]
        enter_credentials(self.driver, email, password)
    def sign_in_kaggle(self):
        self.driver.get(self.starting_url)
        self.driver.find_element_by_class_name('button--small').click()
        email = self.credentials.iloc[4, 1]
        password = self.credentials.iloc[4, 2]
        enter_credentials(self.driver, email, password)
    def sign_in_mail(self, num=None):
        if num is None:
            for i in range(3):
                email = self.credentials.iloc[5 + i, 1]
                password = self.credentials.iloc[5 + i, 2]
                self.driver.get(EMAIL_URLS[i])
                enter_credentials(self.driver, email, password)
        else:
            email = self.credentials.iloc[num + 5, 1]
            password = self.credentials.iloc[num + 5, 2]
            self.driver.get(EMAIL_URLS[num])
            enter_credentials(self.driver, email, password)
    def sign_in_blog(self, spec):
        if spec == 'xkcd':
            self.starting_url = BLOG_URLS[0]
        elif spec == 'blog':
            self.starting_url = BLOG_URLS[1]
        self.driver.get(self.starting_url)
if __name__ == '__main__':
    website = Websites()
    website.sign_in(SOCIAL_MEDIA_URLS[0])