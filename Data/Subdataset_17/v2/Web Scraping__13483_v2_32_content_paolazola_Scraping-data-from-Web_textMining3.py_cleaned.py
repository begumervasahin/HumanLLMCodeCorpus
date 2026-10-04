import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def FB_scraper(base_url, path_browser_driver, name):
    options = Options()
    options.add_argument("--disable-notifications")
    service = Service(path_browser_driver)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)
    pause = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Initial page height: {last_height}")
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        try:
            WebDriverWait(driver, pause).until(
                EC.presence_of_element_located((By.CLASS_NAME, "UFIPagerLink"))
            )
        except Exception as e:
            print(f"Error waiting for UFIPagerLink: {e}")
        for i in driver.find_elements(By.CLASS_NAME, "UFIPagerLink"):
            try:
                i.click()
                print(f"Clicked on: {i}")
            except Exception as e:
                print(f"Error clicking UFIPagerLink: {e}")
        try:
            WebDriverWait(driver, pause).until(
                EC.presence_of_element_located((By.CLASS_NAME, "see_more_link"))
            )
        except Exception as e:
            print(f"Error waiting for see_more_link: {e}")
        for j in driver.find_elements(By.CLASS_NAME, "see_more_link"):
            try:
                j.click()
                print(f"Clicked on: {j}")
            except Exception as e:
                print(f"Error clicking see_more_link: {e}")
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f"New page height: {new_height}")
        if new_height == last_height:
            break
        last_height = new_height
    posts = driver.find_elements(By.XPATH, "
    id_post, times, contenuto, condivisioni, likes, nr_comments = [], [], [], [], [], []
    for p in range(len(posts)):
        try:
            data = posts[p].find_element(By.CSS_SELECTOR, "abbr._5ptz").get_attribute("title")
            times.append(data)
            id_post.append(p)
        except Exception as e:
            print(f"Error getting post date: {e}")
            times.append('none')
            id_post.append(p)
        try:
            contenuti = posts[p].find_element(By.CSS_SELECTOR, 'div._5pbx.userContent._3576').text
            contenuto.append(contenuti)
        except Exception as e:
            print(f"Error getting post content: {e}")
            contenuto.append('none')
        try:
            share = posts[p].find_elements(By.CSS_SELECTOR, "a._3rwx._42ft")
            condivisioni.append(share[0].text)
        except IndexError as e:
            print(f"Error getting post shares: {e}")
            condivisioni.append('none')
        try:
            like = posts[p].find_elements(By.CSS_SELECTOR, "a._3dlf")
            likes.append(like[0].text.split('\n')[0])
        except IndexError as e:
            print(f"Error getting post likes: {e}")
            likes.append('none')
        try:
            nrComm = posts[p].find_elements(By.CSS_SELECTOR, "a._3hg-._42ft")
            nr_comments.append(nrComm[0].text)
        except IndexError as e:
            print(f"Error getting post comments: {e}")
            nr_comments.append('none')
    if len(times) != len(contenuto) and len(times) != len(condivisioni):
        diff = len(contenuto) - len(times)
        contenuto = contenuto[diff:]
        condivisioni = condivisioni[diff:]
        posts = posts[diff:]
        likes = likes[diff:]
        nr_comments = nr_comments[diff:]
    fb_page = pd.DataFrame({
        'utente': name,
        'data': times,
        'post': contenuto,
        'id post': id_post,
        'likes': likes,
        'share': condivisioni,
        'comments number': nr_comments
    })
    driver.quit()
    return fb_page
base_url = 'https:
path_browser_driver = 'path_to_your_chromedriver'
name = 'Your Name'
fb_data = FB_scraper(base_url, path_browser_driver, name)
print(fb_data)