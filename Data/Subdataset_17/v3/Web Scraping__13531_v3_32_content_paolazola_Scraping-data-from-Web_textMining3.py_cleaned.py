import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def configure_driver(path_browser_driver):
    options = Options()
    options.add_argument("--disable-notifications")
    service = Service(path_browser_driver)
    driver = webdriver.Chrome(service=service, options=options)
    return driver
def scroll_and_load_content(driver, pause, scroll_count=5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Initial page height: {last_height}")
    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        click_elements(driver, By.CLASS_NAME, "UFIPagerLink", pause)
        click_elements(driver, By.CLASS_NAME, "see_more_link", pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f"New page height: {new_height}")
        if new_height == last_height:
            break
        last_height = new_height
def click_elements(driver, by, value, pause):
    try:
        WebDriverWait(driver, pause).until(
            EC.presence_of_element_located((by, value))
        )
        elements = driver.find_elements(by, value)
        for element in elements:
            try:
                element.click()
                print(f"Clicked on: {element}")
            except Exception as e:
                print(f"Error clicking {value}: {e}")
    except Exception as e:
        print(f"Error waiting for {value}: {e}")
def extract_post_details(posts):
    id_post, times, contenuto, condivisioni, likes, nr_comments = [], [], [], [], [], []
    for p, post in enumerate(posts):
        id_post.append(p)
        times.append(get_post_attribute(post, By.CSS_SELECTOR, "abbr._5ptz", "title", 'none'))
        contenuto.append(get_post_text(post, By.CSS_SELECTOR, 'div._5pbx.userContent._3576', 'none'))
        condivisioni.append(get_post_text(post, By.CSS_SELECTOR, "a._3rwx._42ft", 'none'))
        likes.append(get_post_text(post, By.CSS_SELECTOR, "a._3dlf", 'none').split('\n')[0])
        nr_comments.append(get_post_text(post, By.CSS_SELECTOR, "a._3hg-._42ft", 'none'))
    return id_post, times, contenuto, condivisioni, likes, nr_comments
def get_post_attribute(post, by, value, attribute, default):
    try:
        return post.find_element(by, value).get_attribute(attribute)
    except Exception as e:
        print(f"Error getting attribute {attribute} for {value}: {e}")
        return default
def get_post_text(post, by, value, default):
    try:
        return post.find_element(by, value).text
    except Exception as e:
        print(f"Error getting text for {value}: {e}")
        return default
def FB_scraper(base_url, path_browser_driver, name):
    driver = configure_driver(path_browser_driver)
    driver.get(base_url)
    pause = 5
    scroll_and_load_content(driver, pause)
    posts = driver.find_elements(By.XPATH, "
    id_post, times, contenuto, condivisioni, likes, nr_comments = extract_post_details(posts)
    min_length = min(len(times), len(contenuto), len(condivisioni), len(likes), len(nr_comments))
    times = times[:min_length]
    contenuto = contenuto[:min_length]
    condivisioni = condivisioni[:min_length]
    likes = likes[:min_length]
    nr_comments = nr_comments[:min_length]
    fb_page = pd.DataFrame({
        'utente': name,
        'data': times,
        'post': contenuto,
        'id post': id_post[:min_length],
        'likes': likes,
        'share': condivisioni,
        'comments number': nr_comments
    })
    driver.quit()
    return fb_page
if __name__ == "__main__":
    base_url = 'https:
    path_browser_driver = 'path_to_your_chromedriver'
    name = 'Your Name'
    fb_data = FB_scraper(base_url, path_browser_driver, name)
    print(fb_data)