import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
def configure_firefox_profile(proxy_host, proxy_port):
    profile = FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy_host)
    profile.set_preference("network.proxy.http_port", proxy_port)
    profile.update_preferences()
    return profile
MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5
PROXY_HOST = "200.37.54.10"
PROXY_PORT = 57040
driver = webdriver.Firefox(firefox_profile=configure_firefox_profile(PROXY_HOST, PROXY_PORT))
for page_num in range(1, MAX_PAGE_NUM + 1):
    formatted_page_num = str(page_num).zfill(MAX_PAGE_DIG)
    url = f"http:
    driver.get(url)
    page_contents = driver.find_elements_by_xpath('
    with open("idmail.csv", "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        for content in page_contents:
            csv_writer.writerow([content.text])
            time.sleep(1)
    print(f"Finished scraping page {page_num}")
driver.quit()
print("All pages scraped successfully.")