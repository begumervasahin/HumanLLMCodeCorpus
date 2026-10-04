
import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
def FB_scraper(base_url, path_browser_driver, driver, name):
    driver.get(base_url)
    pause_duration = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Initial scroll height: {last_height}")
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_duration)
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
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f"New scroll height: {new_height}")
        if new_height == last_height:
            break
        last_height = new_height
    posts = driver.find_elements_by_xpath("
    data = {
        'post_id': [],
        'user': [],
        'date': [],
        'post': [],
        'likes': [],
        'shares': [],
        'comments': []
    }
    for idx, post in enumerate(posts):
        data['post_id'].append(idx)
        data['user'].append(name)
        try:
            timestamp = post.find_element_by_css_selector("abbr._5ptz").get_attribute("title")
            data['date'].append(timestamp)
        except NoSuchElementException:
            data['date'].append('N/A')
        try:
            post_content = post.find_element_by_css_selector('div._5pbx.userContent._3576').text
            data['post'].append(post_content)
        except NoSuchElementException:
            data['post'].append('none')
        try:
            share_text = post.find_elements_by_css_selector("a._3rwx._42ft")[0].text
            data['shares'].append(share_text)
        except (NoSuchElementException, IndexError):
            data['shares'].append('none')
        try:
            like_text = post.find_elements_by_css_selector("a._3dlf")[0].text.split('\n')[0]
            data['likes'].append(like_text)
        except (NoSuchElementException, IndexError):
            data['likes'].append('none')
        try:
            comment_text = post.find_elements_by_css_selector("a._3hg-._42ft")[0].text
            data['comments'].append(comment_text)
        except (NoSuchElementException, IndexError):
            data['comments'].append('none')
    fb_page = pd.DataFrame(data)
    return fb_page