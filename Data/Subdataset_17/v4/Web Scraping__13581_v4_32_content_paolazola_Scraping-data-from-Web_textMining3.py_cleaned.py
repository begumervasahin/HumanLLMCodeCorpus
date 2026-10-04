
import time
import pandas as pd
from selenium import webdriver
def FB_scraper(base_url, path_browser_driver, driver, name):
    driver.get(base_url)
    pause = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Initial scroll height: {last_height}")
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        for link in driver.find_elements_by_class_name("UFIPagerLink"):
            try:
                link.click()
                print("Clicked UFIPagerLink")
            except Exception:
                print("Failed to click UFIPagerLink")
        for link in driver.find_elements_by_class_name("see_more_link"):
            try:
                link.click()
                print("Clicked see_more_link")
            except Exception:
                print("Failed to click see_more_link")
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f"New scroll height: {new_height}")
        if new_height == last_height:
            break
        last_height = new_height
    posts = driver.find_elements_by_xpath("
    id_post = []
    times = []
    content = []
    shares = []
    likes = []
    num_comments = []
    for idx, post in enumerate(posts):
        try:
            timestamp = post.find_element_by_css_selector("abbr._5ptz").get_attribute("title")
            times.append(timestamp)
            id_post.append(idx)
        except:
            times.append('N/A')
            id_post.append(idx)
        try:
            post_content = post.find_element_by_css_selector('div._5pbx.userContent._3576').text
            content.append(post_content)
        except:
            content.append('none')
        try:
            share_text = post.find_elements_by_css_selector("a._3rwx._42ft")[0].text
            shares.append(share_text)
        except IndexError:
            shares.append('none')
        try:
            like_text = post.find_elements_by_css_selector("a._3dlf")[0].text.split('\n')[0]
            likes.append(like_text)
        except IndexError:
            likes.append('none')
        try:
            comment_text = post.find_elements_by_css_selector("a._3hg-._42ft")[0].text
            num_comments.append(comment_text)
        except IndexError:
            num_comments.append('none')
    fb_page = pd.DataFrame({
        'user': name,
        'date': times,
        'post': content,
        'post_id': id_post,
        'likes': likes,
        'shares': shares,
        'comments': num_comments
    })
    return fb_page