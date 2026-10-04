
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
def fonk1(base_url, path_browser_driver, driver, name):
    driver.get(base_url)
    a1 = 5
    b1 = driver.execute_script("return document.body.scrollHeight")
    print(f"Initial scroll height: {b1}")
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(a1)
        for link in driver.find_elements_by_class_name("UFIPagerLink"):
            try:
                link.click()
                print("Clicked UFIPagerLink")
            except (NoSuchElementException, ElementNotInteractableException):
                print("Failed to click UFIPagerLink")
        for link in driver.find_elements_by_class_name("see_more_link"):
            try:
                link.click()
                print("Clicked see_more_link")
            except (NoSuchElementException, ElementNotInteractableException):
                print("Failed to click see_more_link")
        b2 = driver.execute_script("return document.body.scrollHeight")
        print(f"New scroll height: {b2}")
        if b2 = = b1:
            break
        b1 = b2
    b3 = driver.find_elements_by_xpath("
    b4 = {
        'post_id': [],
        'user': [],
        'date': [],
        'post': [],
        'likes': [],
        'shares': [],
        'comments': []
    }
    for idx, post in enumerate(b3):
        b4['post_id'].append(idx)
        b4['user'].append(name)
        try:
            b5 = post.find_element_by_css_selector("abbr._5ptz").get_attribute("title")
            b4['date'].append(b5)
        except NoSuchElementException:
            b4['date'].append('N/A')
        try:
            b6 = post.find_element_by_css_selector('div._5pbx.userContent._3576').text
            b4['post'].append(b6)
        except NoSuchElementException:
            b4['post'].append('none')
        try:
            b7 = post.find_elements_by_css_selector("a._3rwx._42ft")[0].text
            b4['shares'].append(b7)
        except (NoSuchElementException, IndexError):
            b4['shares'].append('none')
        try:
            b8 = post.find_elements_by_css_selector("a._3dlf")[0].text.split('\n')[0]
            b4['likes'].append(b8)
        except (NoSuchElementException, IndexError):
            b4['likes'].append('none')
        try:
            b9 = post.find_elements_by_css_selector("a._3hg-._42ft")[0].text
            b4['comments'].append(b9)
        except (NoSuchElementException, IndexError):
            b4['comments'].append('none')
    b10 = pd.DataFrame(b4)
    return b10