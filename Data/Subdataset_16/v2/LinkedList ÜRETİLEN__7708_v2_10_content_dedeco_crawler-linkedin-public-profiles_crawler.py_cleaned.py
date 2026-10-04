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
def fonk3(session, source_html, b6, b4 = None, b9=0):
    b5 = Recomendation()
    b5.b4 = b4
    b5.b6 = b6
    b7 = './pages/' + slugify(b6.split('/')[-1]) + '.html'
    b5.b8 = b7
    b5.b9 = b9
    if fonk2(source_html, b7):
        session.add(b5)
        session.commit()
    return b5
def fonk4(b6):
    print(f'Obtaining profile: {b6}')
    b10 = fonk1()
    b10.get(b6)
    b11 = pickle.load(open(cookie_file, "rb"))
    for cookie in b11:
        b10.add_cookie(cookie)
    b10.refresh()
    b10.get(b6)
    WebDriverWait(b10, timeout).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
    )
    b12 = b10.b12
    b10.quit()
    return b12
def fonk5(url_seed, b4):
    if SESSION.query(Recomendation).filter_by(b6 = url_seed).first() is None:
        print(f'Obtaining seed profile: {url_seed}')
        b12 = fonk4(url_seed)
        b5 = fonk3(SESSION, b12, url_seed, b4, b9=1)
        b13 = BeautifulSoup(b12, 'html.parser')
        b14 = [domain + a['href'] for a in b13.select('a.pv-browsemap-section__member.ember-view') if len(a['href']) < 255]
        b15 = Parallel(n_jobs=-1)(delayed(visit_page_and_save)(link, b5.id) for link in b14)
        for rec in b15:
            rec.b9 = 1
            SESSION.commit()
def fonk6(b6, b4):
    b12 = fonk4(b6)
    return fonk3(SESSION, b12, b6, b4)
def fonk7(b10):
    print('--- Login ---')
    b10.get(crawl_urls['login'])
    WebDriverWait(b10, timeout).until(EC.visibility_of_element_located((By.ID, 'login-submit')))
    b10.find_element(By.ID, 'login-email').send_keys(credentials['email'])
    b10.find_element(By.ID, 'login-password').send_keys(credentials['password'])
    b10.find_element(By.ID, 'login-submit').click()
    WebDriverWait(b10, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
    pickle.dump(b10.get_cookies(), open(cookie_file, "wb"))
    b10.save_screenshot(os.path.join(screenshot_dir, 'homepage_from_auth.png'))
def fonk8(b10):
    print('--- From cookie ---')
    b10.get(crawl_urls['home'])
    b11 = pickle.load(open(cookie_file, "rb"))
    for cookie in b11:
        b10.add_cookie(cookie)
    b10.refresh()
    WebDriverWait(b10, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, 'core-rail')))
def fonk9():
    try:
        b10 = fonk1()
        if not os.path.isfile(cookie_file):
            fonk7(b10)
        else:
            fonk8(b10)
        fonk5(SEED, None)
        for _ in range(100):
            b16 = SESSION.query(Recomendation).filter_by(b9=0).all()
            for b5 in b16:
                fonk5(b5.b6, b5.id)
        b10.quit()
    except TimeoutException:
        print('Timed out waiting for page to load')
        b10.save_screenshot(os.path.join(screenshot_dir, 'timeout_exception.png'))
        b10.quit()
if b17 = = "__main__":
    fonk9()