
import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import (
    timeout, dir_path, crawl_urls, credentials,
    cookie_file, screenshot_dir, domain, SEED
)
from database import Recomendation, SESSION
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from slugify import slugify
b1 = os.path.join(dir_path, 'chromedriver')
b2 = webdriver.ChromeOptions()
b2.add_argument('--incognito')
def fonk1():
    b3 = webdriver.Chrome(
        b4 = b1,
        b5 = b2
    )
    return b3
def fonk2(html_str, filename):
    with open(filename, "w") as html_file:
        html_file.write(html_str)
    return True
def fonk3(session, source_html, b8, b6 = None, b11=0):
    b7 = Recomendation()
    b7.b6 = b6
    b7.b8 = b8
    b9 = './pages/' + slugify(b8.split('/')[4]) + '.html'
    b7.b10 = b9
    b7.b11 = b11
    if fonk2(source_html, b9):
        session.add(b7)
        session.commit()
    return b7
def fonk4(b8):
    print('Obtaining profile:', b8)
    b3 = fonk1()
    b3.get(b8)
    b12 = pickle.load(open(cookie_file, "rb"))
    for cookie in b12:
        b3.add_cookie(cookie)
    b3.refresh()
    b3.get(b8)
    WebDriverWait(b3, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
    )
    b13 = b3.b13
    b3.quit()
    return b13
def fonk5(url_seed, b6):
    b14 = SESSION.query(Recomendation).filter_by(b8=url_seed).first()
    if not b14 or b14.b11 = = 0:
        print('Obtaining seed profile:', url_seed)
        b13 = fonk4(url_seed)
        b7 = fonk3(SESSION, b13, url_seed, b6=b6, b11=1)
        b15 = BeautifulSoup(b13, 'html.parser')
        b16 = b15.find('b16', class_='pv-profile-section__section-info section-info browsemap mt4')
        b17 = [domain + a['href'] for a in b16.find_all('a', class_='pv-browsemap-section__member ember-view') if len(a['href']) < 255]
        b18 = []
        b19 = Parallel(n_jobs=-1)(delayed(visit_page)(link) for link in b17)
        for b13, link in zip(b19, b17):
            b20 = fonk3(SESSION, b13, link, b6=b7.id)
            b18.append(b20)
        for b7 in b18:
            b7.b11 = 1
            SESSION.commit()
def fonk6():
    try:
        b3 = fonk1()
        if not os.path.isfile(cookie_file):
            print('--- Login ---')
            b3.get(crawl_urls['login'])
            WebDriverWait(b3, timeout).until(
                EC.visibility_of_element_located((By.ID, 'login-submit'))
            )
            b3.find_element(By.ID, 'login-email').send_keys(credentials['email'])
            b3.find_element(By.ID, 'login-password').send_keys(credentials['password'])
            b3.find_element(By.ID, 'login-submit').click()
            WebDriverWait(b3, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail'))
            )
            pickle.dump(b3.get_cookies(), open(cookie_file, "wb"))
            b3.save_screenshot(os.path.join(screenshot_dir, 'homepage_from_auth.png'))
        else:
            print('--- From cookie ---')
            b3.get(crawl_urls['home'])
            b12 = pickle.load(open(cookie_file, "rb"))
            for cookie in b12:
                b3.add_cookie(cookie)
            b3.refresh()
            WebDriverWait(b3, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail'))
            )
        fonk5(SEED, None)
        for _ in range(100):
            b21 = SESSION.query(Recomendation).filter_by(b11=0).all()
            for b7 in b21:
                fonk5(b7.b8, b7.id)
        b3.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b3.save_screenshot(os.path.join(screenshot_dir, 'timeout_exception.png'))
        b3.quit()
if b22 = = "__main__":
    fonk6()