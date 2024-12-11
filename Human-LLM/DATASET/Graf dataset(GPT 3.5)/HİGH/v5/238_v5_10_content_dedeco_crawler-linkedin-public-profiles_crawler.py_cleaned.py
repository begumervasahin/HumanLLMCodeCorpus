import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
from slugify import slugify
from config import timeout, dir_path, crawl_urls, credentials, cookie_file, screenshot_dir, domain, SEED
from database import Recomendation, SESSION
b1 = os.path.join(dir_path, 'chromedriver')
b2 = webdriver.ChromeOptions()
b2.add_argument('--incognito')
def fonk1():
    b3 = webdriver.Chrome(executable_path=b1, b2=b2)
    return b3
def fonk2(html_str, filename):
    with open(filename, "w") as html_file:
        html_file.write(html_str)
def fonk3(session, source_html, b6, b4 = None, b9=0):
    b5 = Recomendation()
    b5.b4 = b4
    b5.b6 = b6
    b7 = './pages/' + slugify(b6.split('/')[4]) + '.html'
    b5.b8 = b7
    b5.b9 = b9
    if fonk2(source_html, b7):
        session.add(b5)
        session.commit()
    return b5
def fonk4(b6):
    print('Visiting profile:', b6)
    b3 = fonk1()
    b3.get(b6)
    b10 = pickle.load(open(cookie_file, "rb"))
    for cookie in b10:
        b3.add_cookie(cookie)
    b3.refresh()
    b3.get(b6)
    WebDriverWait(b3, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content')))
    b11 = b3.b11
    b3.quit()
    return b11
def fonk5(url_seed, b4):
    b12 = SESSION.query(Recomendation).filter_by(b6=url_seed).first()
    if not b12 or b12.b9 = = 0:
        print('Processing seed profile:', url_seed)
        b11 = fonk4(url_seed)
        b5 = fonk3(SESSION, b11, url_seed, b4=b4, b9=1)
        b13 = BeautifulSoup(b11, 'html.parser')
        b14 = b13.find('b14', class_='pv-profile-section__section-info section-info browsemap mt4')
        b15 = [domain + a['href'] for a in b14.find_all('a', class_='pv-browsemap-section__member ember-view')]
        b9 = []
        b16 = Parallel(n_jobs=-1)(delayed(visit_page)(link) for link in b15)
        for b11, link in zip(b16, b15):
            b17 = fonk3(SESSION, b11, link, b4=b5.id)
            b9.append(b17)
        for v in b9:
            v.b9 = 1
            SESSION.commit()
def fonk6():
    try:
        b3 = fonk1()
        if not os.path.isfile(cookie_file):
            print('--- Logging in ---')
            b3.get(crawl_urls['login'])
            WebDriverWait(b3, timeout).until(EC.visibility_of_element_located((By.ID, 'login-submit')))
            b3.find_element_by_id('login-email').send_keys(credentials['email'])
            b3.find_element_by_id('login-password').send_keys(credentials['password'])
            b3.find_element_by_id('login-submit').click()
            WebDriverWait(b3, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
            pickle.dump(b3.get_cookies(), open(cookie_file, "wb"))
            b3.save_screenshot(screenshot_dir + 'homepage_from_auth.png')
        else:
            print('--- Using saved cookie ---')
            b3.get(crawl_urls['home'])
            b10 = pickle.load(open(cookie_file, "rb"))
            for cookie in b10:
                b3.add_cookie(cookie)
            b3.refresh()
            WebDriverWait(b3, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
        fonk5(SEED, None)
        for _ in range(100):
            b18 = SESSION.query(Recomendation).filter_by(b9=0).all()
            for v in b18:
                fonk5(v.b6, v.id)
        b3.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b3.save_screenshot(screenshot_dir + 'timeout_exception.png')
        b3.quit()
fonk6()