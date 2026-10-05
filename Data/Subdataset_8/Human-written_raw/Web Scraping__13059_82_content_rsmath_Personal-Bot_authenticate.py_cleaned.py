
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helpers import commands
from links import SCHOOL, CONST_EMAILS, BLOGS, SOCIAL_MEDIA
class Websites:
    def __init__(self):
        self.url = 'https:
        self.path_to_chromedriver = "/Users/ramanshsharma/Downloads/chromedriver"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.file = pd.read_csv('secrets.csv')
        self.driver = None
        self.media_to_func = {
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
    def sign_in(self, url=None):
        if url is not None:
            self.url = url
        media = link_to_media(self.url)
        self.driver = webdriver.Chrome(self.path_to_chromedriver,
                                       chrome_options=self.chrome_options)
        if media == 'mail0' or media == 'mail1' or media == 'mail2':
            self.media_to_func[media](num=int(media[-1]))
        elif media == 'school' or media == 'sciencesurvey':
            self.media_to_func[media](spec=media)
        elif media == 'xkcd' or media == 'blog':
            self.media_to_func[media](spec=media)
        else:
            self.media_to_func[media]()
    def get_school(self, spec=None):
        if spec == 'school' or spec is None:
            self.url = SCHOOL[0]
        elif spec == 'sciencesurvey':
            self.url = SCHOOL[1]
        self.driver.get(self.url)
    def get_linkedin(self):
        self.driver.get(self.url)
        time.sleep(2)
        give_username = self.driver.find_element_by_id('login-email')
        give_username.send_keys(self.file.iloc[4, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_id('login-password')
        time.sleep(2)
        give_password.send_keys(self.file.iloc[4, 2])
        time.sleep(2)
        give_password.send_keys(Keys.RETURN)
    def get_twitter(self):
        self.driver.get(self.url)
        time.sleep(2)
        click_login = self.driver.find_element_by_link_text('Log in')
        click_login.click()
        time.sleep(1)
        give_username = self.driver.find_element_by_class_name('email-input')
        give_username.send_keys(self.file.iloc[0, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_name('session[password]')
        give_password.send_keys(self.file.iloc[0, 2])
        time.sleep(2)
        give_password.send_keys(Keys.RETURN)
    def get_instagram(self):
        self.driver.get(self.url)
        time.sleep(2)
        log_in = self.driver.find_element_by_link_text('Log in')
        log_in.click()
        time.sleep(2)
        email_enter = self.driver.find_element_by_class_name('_2hvTZ')
        email_enter.send_keys(self.file.iloc[2, 1])
        time.sleep(2)
        password_area = self.driver.find_elements_by_class_name('_2hvTZ')[1]
        password_area.send_keys(self.file.iloc[2, 2])
        time.sleep(2)
        password_area.send_keys(Keys.RETURN)
    def get_github(self):
        self.driver.get(self.url)
        time.sleep(2)
        sign_in_button = self.driver.find_element_by_link_text('Sign in')
        sign_in_button.click()
        sign_in_button = self.driver.find_element_by_id('login_field')
        time.sleep(2)
        sign_in_button.send_keys(self.file.iloc[1, 1])
        time.sleep(2)
        sign_in_button = self.driver.find_element_by_id('password')
        time.sleep(2)
        sign_in_button.send_keys(self.file.iloc[1, 2])
        time.sleep(2)
        sign_in_button.send_keys(Keys.RETURN)
    def get_kaggle(self):
        self.driver.get(self.url)
        time.sleep(2)
        click_login = self.driver.find_element_by_class_name('button--small')
        click_login.click()
        give_username = self.driver.find_element_by_id('username-input-text')
        give_username.send_keys(self.file.iloc[4, 1])
        time.sleep(2)
        give_password = self.driver.find_element_by_id('password-input-text')
        give_password.send_keys(self.file.iloc[4, 2])
        time.sleep(2)
        click_sign_in = self.driver.find_element_by_link_text('Sign in')
        click_sign_in.click()
    def get_mail(self, num=None):
        if num is None:
            self.url = CONST_EMAILS[0]
            email, password = self.file.iloc[5, 1], self.file.iloc[5, 2]
            mail_action(self.driver, self.url, email, password)
            email, password = self.file.iloc[6, 1], self.file.iloc[6, 2]
            time.sleep(2)
            self.url = CONST_EMAILS[1]
            self.driver.execute_script(f'window.open({self.url}, "_blank");')
            mail_action(self.driver, self.url, email, password)
            email, password = self.file.iloc[7, 1], self.file.iloc[7, 2]
            time.sleep(2)
            self.url = CONST_EMAILS[2]
            self.driver.execute_script(f'window.open({self.url}, "_blank");')
            mail_action(self.driver, self.url, email, password)
        else:
            self.url = CONST_EMAILS[num]
            email = self.file.iloc[num + 5, 1]
            password = self.file.iloc[num + 5, 2]
        mail_action(self.driver, self.url, email, password)
    def get_xkcd(self, spec):
        if spec == 'xkcd':
            self.url = BLOGS[0]
        elif spec == 'blog':
            self.url = BLOGS[1]
        self.driver.get(self.url)
def link_to_media(link):
    return [item[0] for item in commands.items() if link == item[1]][0]
def mail_action(driver, url, email, password):
    driver.get(url)
    time.sleep(2)
    email_input = driver.find_element_by_id('identifierId')
    email_input.send_keys(email)
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)
    password_input = driver.find_element_by_class_name('whsOnd')
    password_input.send_keys(password)
    time.sleep(2)
    password_input.send_keys(Keys.RETURN)
if __name__ == '__main__':
    website = Websites()
    website.sign_in(SOCIAL_MEDIA[0])