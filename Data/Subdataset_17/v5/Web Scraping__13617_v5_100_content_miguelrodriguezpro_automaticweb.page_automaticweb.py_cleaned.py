import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
WORDPRESS_USERNAME = "your_username"
WORDPRESS_PASSWORD = "your_password"
CHROME_DRIVER_PATH = "C:\\Users\\.....\\chromedriver.exe"
KEYWORDS = ["keyword1", "keyword2", "keyword3"]
YOUTUBE_SEARCH_URL = "https:
def initialize_driver(chrome_driver_path):
    return webdriver.Chrome(executable_path=chrome_driver_path)
def wordpress_login(driver, username, password):
    driver.get('https:
    time.sleep(3)
    user_field = driver.find_element_by_xpath("
    user_field.send_keys(username)
    time.sleep(2)
    pass_field = driver.find_element_by_xpath("
    pass_field.send_keys(password)
    pass_field.send_keys(Keys.ENTER)
    time.sleep(8)
def create_new_post(driver):
    driver.find_element_by_xpath("
    time.sleep(3)
def search_youtube(driver, keyword):
    driver.switch_to.new_window('tab')
    time.sleep(3)
    search_url = YOUTUBE_SEARCH_URL + keyword + "&sp=EgIQAQ%253D%253D"
    driver.get(search_url)
    time.sleep(5)
    video_elements = driver.find_elements_by_xpath(
        '
    )
    return video_elements[:10]
def add_videos_to_post(driver, keyword, videos):
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
def main():
    driver = initialize_driver(CHROME_DRIVER_PATH)
    try:
        wordpress_login(driver, WORDPRESS_USERNAME, WORDPRESS_PASSWORD)
        for keyword in KEYWORDS:
            create_new_post(driver)
            videos = search_youtube(driver, keyword)
            add_videos_to_post(driver, keyword, videos)
            time.sleep(10)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()