
import os
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import timeout, dir_path, crawl_urls, credentials, cookie_file, screenshot_dir, domain, SEED
from database import Recomendation, SESSION, Recomendation
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
def fonk2():
    def fonk3(html_str, filename):
        b6 = open(filename,"w")
        b6.write(html_str)
        b6.close()
        return True
    def fonk4(SESSION, source_html, b9, b7 = None, b11=0):
        b8 = Recomendation()
        b8.b7 = b7
        b8.b9 = b9
        b10 = './pages/' + slugify(b9.split('/')[4]) +'.html'
        b8.b10 = b10
        b8.b11 = b11
        if fonk3(source_html, b10):
            SESSION.add(b8)
            SESSION.commit()
        return b8
    def fonk5(b9):
        print('Obtendo o perfil:',b9)
        b3 = fonk1()
        b3.get(b9)
        b12 = pickle.load(open(cookie_file, "rb"))
        for cookie in b12:
            b3.add_cookie(cookie)
        b3.refresh()
        b3.get(b9)
        WebDriverWait(b3, timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
        )
        b13 = b3.b13
        b3.quit()
        return b13
    def fonk6(url_seed, b7):
        b14 = SESSION.query(Recomendation).filter_by(b9=url_seed).first()
        if not b14 or b14.b11 = =0:
            print('Obtendo o perfil seed :',url_seed)
            b13 = fonk5(url_seed)
            b8 = fonk4(SESSION, b13, url_seed,  b7=b7, b11=1)
            b15 = BeautifulSoup(b13, 'html.parser')
            b16 = b15.find('b16', b18= 'pv-profile-section__section-info section-info browsemap mt4')
            b17 = []
            for a in b16.find_all('a', b18 = 'pv-browsemap-section__member ember-view'):
                b9 = domain + a['href']
                if len(b9) < 255:
                    b17.append(b9)
            b19 = []
            b20 = Parallel(n_jobs=-1)(delayed(visit_page)(link) for link in b17)
            for b13, link in zip(b20, b17):
                b21 = fonk4(SESSION, b13, link, b7=b8.id)
                b19.append(b21)
            for v in b19:
                v.a1 = 1
                SESSION.commit()
    try:
        b3 = fonk1()
        if (not os.path.isfile(cookie_file)):
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
            pickle.dump(b3.get_cookies() , open(cookie_file,"wb"))
            b3.save_screenshot(screenshot_dir + 'homepage_from_auth.png')
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
        fonk6(SEED, None)
        for i in range(100):
            b22 = SESSION.query(Recomendation).filter_by(b11=0).all()
            for v in b22:
                fonk6(v.b9, v.id)
        b3.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b3.save_screenshot(screenshot_dir + 'timeout_exception.png')
        b3.quit()
fonk2()