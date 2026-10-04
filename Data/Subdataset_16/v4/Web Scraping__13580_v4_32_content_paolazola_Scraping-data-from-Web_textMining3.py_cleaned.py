
import time
import pandas as pd
from selenium import webdriver
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
            except Exception:
                print("Failed to click UFIPagerLink")
        for link in driver.find_elements_by_class_name("see_more_link"):
            try:
                link.click()
                print("Clicked see_more_link")
            except Exception:
                print("Failed to click see_more_link")
        b2 = driver.execute_script("return document.body.scrollHeight")
        print(f"New scroll height: {b2}")
        if b2 = = b1:
            break
        b1 = b2
    b3 = driver.find_elements_by_xpath("
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    for idx, post in enumerate(b3):
        try:
            b10 = post.find_element_by_css_selector("abbr._5ptz").get_attribute("title")
            b5.append(b10)
            b4.append(idx)
        except:
            b5.append('N/A')
            b4.append(idx)
        try:
            b11 = post.find_element_by_css_selector('div._5pbx.userContent._3576').text
            b6.append(b11)
        except:
            b6.append('none')
        try:
            b12 = post.find_elements_by_css_selector("a._3rwx._42ft")[0].text
            b7.append(b12)
        except IndexError:
            b7.append('none')
        try:
            b13 = post.find_elements_by_css_selector("a._3dlf")[0].text.split('\n')[0]
            b8.append(b13)
        except IndexError:
            b8.append('none')
        try:
            b14 = post.find_elements_by_css_selector("a._3hg-._42ft")[0].text
            b9.append(b14)
        except IndexError:
            b9.append('none')
    b15 = pd.DataFrame({
        'user': name,
        'date': b5,
        'post': b6,
        'post_id': b4,
        'b8': b8,
        'b7': b7,
        'comments': b9
    })
    return b15