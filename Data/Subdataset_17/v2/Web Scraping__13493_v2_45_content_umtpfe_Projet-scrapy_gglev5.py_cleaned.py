from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
def initialize_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver
def scrape_google_search(query):
    driver = initialize_driver()
    url = f"http:
    driver.get(url)
    results = []
    try:
        while True:
            elements = driver.find_elements(By.XPATH, '
            for element in elements:
                try:
                    title = element.find_element(By.TAG_NAME, "h3").text
                    link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    results.append((title, link))
                except Exception as inner_e:
                    print(f"An error occurred while processing an element: {inner_e}")
            next_button = driver.find_elements(By.XPATH, '
            if next_button:
                next_button[0].click()
                time.sleep(2)
            else:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    return results
if __name__ == "__main__":
    query = "chanel"
    results = scrape_google_search(query)
    for title, link in results:
        print(f"Title: {title}\nLink: {link}\n")