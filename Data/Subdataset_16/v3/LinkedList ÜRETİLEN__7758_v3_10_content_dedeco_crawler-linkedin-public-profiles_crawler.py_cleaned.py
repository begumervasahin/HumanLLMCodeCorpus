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
    return webdriver.Chrome(b3 = b1, options=b2)
def fonk2(html_str, filename):
    with open(filename, "w") as html_file:
        html_file.write(html_str)
    return True
def fonk3(session, source_html, b6, b4 = None, b8=0):
    b5 = Recomendation(
        b4 = b4,
        b6 = b6,
        b7 = f'./pages/{slugify(b6.split("/")[-1])}.html',
        b8 = b8
    )
    if fonk2(source_html, b5.b7):
        session.add(b5)
        session.commit()
    return b5
def fonk4(b6):
    print(f'Obtaining profile: {b6}')
    b9 = fonk1()
    b9.get(b6)
    b10 = pickle.load(open(cookie_file, "rb"))
    for cookie in b10:
        b9.add_cookie(cookie)
    b9.refresh()
    b9.get(b6)
    WebDriverWait(b9, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
    )
    b11 = b9.b11
    b9.quit()
    return b11
def fonk5(url_seed, b4):
    if not SESSION.query(Recomendation).filter_by(b6 = url_seed).first():
        print(f'Obtaining seed profile: {url_seed}')
        b11 = fonk4(url_seed)
        b5 = fonk3(SESSION, b11, url_seed, b4, b8=1)
        b12 = BeautifulSoup(b11, 'html.parser')
        b13 = [
            domain + a['href']
            for a in b12.select('a.pv-browsemap-section__member.ember-view')
            if len(a['href']) < 255
        ]
        b14 = Parallel(n_jobs=-1)(
            delayed(visit_page_and_save)(link, b5.id) for link in b13
        )
        for rec in b14:
            rec.b8 = 1
            SESSION.commit()
def fonk6(b6, b4):
    b11 = fonk4(b6)
    return fonk3(SESSION, b11, b6, b4)
def fonk7(b9):
    print('--- Login ---')
    b9.get(crawl_urls['login'])
    WebDriverWait(b9, timeout).until(EC.visibility_of_element_located((By.ID, 'login-submit')))
    b9.find_element(By.ID, 'login-email').send_keys(credentials['email'])
    b9.find_element(By.ID, 'login-password').send_keys(credentials['password'])
    b9.find_element(By.ID, 'login-submit').click()
    WebDriverWait(b9, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
    pickle.dump(b9.get_cookies(), open(cookie_file, "wb"))
    b9.save_screenshot(os.path.join(screenshot_dir, 'homepage_from_auth.png'))
def fonk8(b9):
    print('--- From cookie ---')
    b9.get(crawl_urls['home'])
    b10 = pickle.load(open(cookie_file, "rb"))
    for cookie in b10:
        b9.add_cookie(cookie)
    b9.refresh()
    WebDriverWait(b9, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
def fonk9():
    try:
        b9 = fonk1()
        if not os.path.isfile(cookie_file):
            fonk7(b9)
        else:
            fonk8(b9)
        fonk5(SEED, None)
        for _ in range(100):
            b15 = SESSION.query(Recomendation).filter_by(b8=0).all()
            for b5 in b15:
                fonk5(b5.b6, b5.id)
        b9.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b9.save_screenshot(os.path.join(screenshot_dir, 'timeout_exception.png'))
        b9.quit()
if b16 = = "__main__":
    fonk9()