import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
wordpress_username = "YOUR_WORDPRESS_USER"
wordpress_password = "YOUR_WORDPRESS_PASSWORD"
keywords = ["example_keyword1", "example_keyword2"]
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
def login_to_wordpress(username, password):
    driver.get('https:
    time.sleep(3)
    user_input = driver.find_element(By.ID, 'user_login')
    user_input.send_keys(username)
    time.sleep(1)
    password_input = driver.find_element(By.ID, 'user_pass')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(8)
def create_new_post(title):
    driver.find_element(By.ID, 'wp-admin-bar-new-content').click()
    time.sleep(3)
    post_title_input = driver.find_element(By.ID, 'post-title-0')
    post_title_input.send_keys(title)
def search_youtube(keyword):
    search_url = f"https:
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(search_url)
    time.sleep(5)
def get_top_videos():
    video_elements = driver.find_elements(By.XPATH, '
    return video_elements[:10]
def add_video_to_post(idx, title, href):
    driver.switch_to.window(driver.window_handles[0])
    body_input = driver.find_element(By.XPATH, '
    body_input.send_keys(Keys.ENTER, Keys.ENTER, f"{idx + 1}. {title}", Keys.ENTER, href, Keys.ENTER, Keys.ENTER)
    time.sleep(2)
    body_input.send_keys(Keys.CONTROL, "s")
    time.sleep(2)
try:
    login_to_wordpress(wordpress_username, wordpress_password)
    for keyword in keywords:
        print("Processing keyword:", keyword)
        create_new_post(f"[TOP 10] videos {keyword}")
        search_youtube(keyword)
        top_videos = get_top_videos()
        for idx, video in enumerate(top_videos):
            title = video.get_attribute("title")
            href = video.get_attribute("href")
            print(f"{idx + 1}. {title}: {href}")
            add_video_to_post(idx, title, href)
            driver.switch_to.window(driver.window_handles[1])
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.XPATH, '
        time.sleep(10)
finally:
    driver.quit()