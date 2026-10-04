import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
word_username = "YOUR_WORDPRESS_USER"
word_password = "YOUR_WORDPRESS_PASSWORD"
keywords = ["example_keyword1", "example_keyword2"]
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get('https:
    time.sleep(3)
    user = driver.find_element(By.ID, 'user_login')
    user.send_keys(word_username)
    time.sleep(1)
    passw = driver.find_element(By.ID, 'user_pass')
    passw.send_keys(word_password)
    passw.send_keys(Keys.ENTER)
    time.sleep(8)
    for keyword in keywords:
        print("Processing keyword:", keyword)
        driver.find_element(By.ID, 'wp-admin-bar-new-content').click()
        time.sleep(3)
        post_title = driver.find_element(By.ID, 'post-title-0')
        post_title.send_keys(f"[TOP 10] videos {keyword}")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        search_url = f"https:
        driver.get(search_url)
        time.sleep(5)
        videos = driver.find_elements(By.XPATH, '
        top_videos = videos[:10]
        for idx, video in enumerate(top_videos):
            title = video.get_attribute("title")
            href = video.get_attribute("href")
            print(f"{idx + 1}. {title}: {href}")
            driver.switch_to.window(driver.window_handles[0])
            body = driver.find_element(By.XPATH, '
            body.send_keys(Keys.ENTER, Keys.ENTER, f"{idx + 1}. {title}", Keys.ENTER, href, Keys.ENTER, Keys.ENTER)
            time.sleep(2)
            body.send_keys(Keys.CONTROL, "s")
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
        driver.switch_to.window(driver.window_handles[0])
        body.send_keys(Keys.CONTROL, "s")
        time.sleep(10)
finally:
    driver.quit()