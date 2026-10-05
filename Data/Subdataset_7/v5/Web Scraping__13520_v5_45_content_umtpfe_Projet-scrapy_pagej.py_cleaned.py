import csv
from selenium import webdriver
import time
b1 = "5.58.85.32:43214"
b2 = webdriver.ChromeOptions()
b2.add_argument('--proxy-b3 = %s' % b1)
b2.add_argument('--ignore_certificate-errors')
b2.add_argument('--ignore-ssl-errors')
a1 = 16
a2 = 3
b4 = "b8.csv"
a3 = 10
def fonk1(page_num):
    return f"https:
with open(b4, "w") as csv_file:
    b5 = webdriver.Chrome(options=b2)
    for page_num in range(1, a1 + 1):
        b6 = f"{page_num:03}"
        b7 = fonk1(b6)
        b5.get(b7)
        time.sleep(a3)
        b8 = b5.find_elements_by_xpath('
        for contact in b8:
            csv_file.write(contact.text + ",\n")
    b5.close()
print("Finished writing b8 to CSV.")