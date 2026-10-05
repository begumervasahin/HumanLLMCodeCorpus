import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
def fonk1(proxy_host, proxy_port):
    b1 = FirefoxProfile()
    b1.set_preference("network.proxy.type", 1)
    b1.set_preference("network.proxy.http", proxy_host)
    b1.set_preference("network.proxy.http_port", proxy_port)
    b1.update_preferences()
    return b1
a1 = 50
a2 = 5
b2 = "200.37.54.10"
a3 = 57040
b3 = webdriver.Firefox(firefox_profile=fonk1(b2, a3))
for page_num in range(1, a1 + 1):
    b4 = str(page_num).zfill(a2)
    b5 = f"http:
    b3.get(b5)
    b6 = b3.find_elements_by_xpath('
    with open("idmail.csv", "a") as csv_file:
        b7 = csv.writer(csv_file)
        for content in b6:
            b7.writerow([content.text])
            time.sleep(1)
    print(f"Finished scraping page {page_num}")
b3.quit()
print("All pages scraped successfully.")