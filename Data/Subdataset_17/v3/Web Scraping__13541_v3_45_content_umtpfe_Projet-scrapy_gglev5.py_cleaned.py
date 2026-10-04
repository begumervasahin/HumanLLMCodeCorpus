from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
def initialize_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver
def extract_search_results(driver):
    results = []
    elements = driver.find_elements(By.XPATH, '
    for element in elements:
        try:
            title = element.find_element(By.TAG_NAME, "h3").text
            link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            results.append((title, link))
        except Exception as e:
            print(f"An error occurred while processing an element: {e}")
    return results
def click_next_button(driver):
    next_buttons = driver.find_elements(By.XPATH, '
    if next_buttons:
        next_buttons[0].click()
        time.sleep(2)
        return True
    return False
def scrape_google_search(query):
    driver = initialize_driver()
    url = f"http:
    driver.get(url)
    all_results = []
    try:
        while True:
            results = extract_search_results(driver)
            all_results.extend(results)
            if not click_next_button(driver):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    return all_results
if __name__ == "__main__":
    query = "chanel"
    results = scrape_google_search(query)
    for title, link in results:
        print(f"Title: {title}\nLink: {link}\n")