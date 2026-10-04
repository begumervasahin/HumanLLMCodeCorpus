import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
word_username = "your_username"
word_password = "your_password"
chrome_driver_path = "C:\\Users\\.....\\chromedriver.exe"
keywords = ["keyword1", "keyword2", "keyword3"]
youtube_search_url = "https:
driver = webdriver.Chrome(executable_path=chrome_driver_path)
def wordpress_login():
    driver.get('https:
    time.sleep(3)
    user_field = driver.find_element_by_xpath("
    user_field.send_keys(word_username)
    time.sleep(2)
    pass_field = driver.find_element_by_xpath("
    pass_field.send_keys(word_password)
    pass_field.send_keys(Keys.ENTER)
    time.sleep(8)
def create_new_post():
    driver.find_element_by_xpath("
    time.sleep(3)
def search_youtube(keyword):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    search_url = youtube_search_url + keyword + "&sp=EgIQAQ%253D%253D"
    driver.get(search_url)
    time.sleep(5)
    videos = driver.find_elements_by_xpath(
        '
    )
    return videos[:10]
def add_videos_to_post(keyword, videos):
    driver.switch_to.window(driver.window_handles[0])
    title_field = driver.find_element_by_xpath('
    content_field = driver.find_element_by_xpath('
    title_field.send_keys(f"[TOP 10] videos {keyword}")
    time.sleep(2)
    for index, video in enumerate(videos):
        video_title = video.get_attribute("title")
        video_url = video.get_attribute("href")
        content_field.send_keys(Keys.ENTER)
        content_field.send_keys(f"{index + 1}. {video_title}")
        content_field.send_keys(Keys.ENTER)
        content_field.send_keys(video_url)
        content_field.send_keys(Keys.ENTER)
        time.sleep(1)
    content_field.send_keys(Keys.CONTROL, "s")
    time.sleep(2)
wordpress_login()
for keyword in keywords:
    create_new_post()
    videos = search_youtube(keyword)
    add_videos_to_post(keyword, videos)
    time.sleep(10)
driver.quit()