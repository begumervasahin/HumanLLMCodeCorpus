import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import timeout, dir_path, crawl_urls, credentials, cookie_file, screenshot_dir, domain, SEED
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
def fonk3(SESSION, source_html, b8, b6 = None, b10=0):
    b7 = Recomendation()
    b7.b6 = b6
    b7.b8 = b8
    b9 = './pages/' + slugify(b8.split('/')[-1]) + '.html'
    b7.b9 = b9
    b7.b10 = b10
    if fonk2(source_html, b9):
        SESSION.add(b7)
        SESSION.commit()
    return b7
def fonk4(b8):
    print('Obtendo o perfil:', b8)
    b3 = fonk1()
    b3.get(b8)
    b11 = pickle.load(open(cookie_file, "rb"))
    for cookie in b11:
        b3.add_cookie(cookie)
    b3.refresh()
    b3.get(b8)
    WebDriverWait(b3, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
    )
    b12 = b3.b12
    b3.quit()
    return b12
def fonk5(url_seed, b6):
    b13 = SESSION.query(Recomendation).filter_by(b8=url_seed).first()
    if not b13 or b13.b10 = = 0:
        print('Obtendo o perfil seed:', url_seed)
        b12 = fonk4(url_seed)
        b7 = fonk3(SESSION, b12, url_seed, b6=b6, b10=1)
        b14 = BeautifulSoup(b12, 'html.parser')
        b15 = b14.find('b15', b17='pv-profile-section__section-info section-info browsemap mt4')
        b16 = []
        for a in b15.find_all('a', b17 = 'pv-browsemap-section__member ember-view'):
            b8 = domain + a['href']
            if len(b8) < 255:
                b16.append(b8)
        b18 = []
        b19 = Parallel(n_jobs=-1)(delayed(visit_page)(link) for link in b16)
        for b12, link in zip(b19, b16):
            b20 = fonk3(SESSION, b12, link, b6=b7.id)
            b18.append(b20)
        for v in b18:
            v.b10 = 1
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
            b3.find_element_by_id('login-email').send_keys(credentials['email'])
            b3.find_element_by_id('login-password').send_keys(credentials['password'])
            b3.find_element_by_id('login-submit').click()
            WebDriverWait(b3, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail'))
            )
            pickle.dump(b3.get_cookies(), open(cookie_file, "wb"))
            b3.save_screenshot(os.path.join(screenshot_dir, 'homepage_from_auth.png'))
        else:
            print('--- From cookie ---')
            b3.get(crawl_urls['home'])
            b11 = pickle.load(open(cookie_file, "rb"))
            for cookie in b11:
                b3.add_cookie(cookie)
            b3.refresh()
            WebDriverWait(b3, timeout).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail'))
            )
        fonk5(SEED, None)
        for i in range(100):
            b21 = SESSION.query(Recomendation).filter_by(b10=0).all()
            for v in b21:
                fonk5(v.b8, v.id)
        b3.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b3.save_screenshot(os.path.join(screenshot_dir, 'timeout_exception.png'))
        b3.quit()
if b22 = = "__main__":
    fonk6()