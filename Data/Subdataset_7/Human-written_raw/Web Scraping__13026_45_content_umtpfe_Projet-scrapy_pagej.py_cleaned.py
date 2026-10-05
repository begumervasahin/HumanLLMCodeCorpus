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
with open ("b7.csv", "w") as f :
	b4 = webdriver.Chrome(options=b2)
for i in range(1, a1 + 1):
  b5 = (a2 - len(str(i))) * "0" + str(i)
  b6 = "https:
  b4.get(b6)
  time.sleep(10)
  b7 = b4.find_elements_by_xpath('
  b8 = len(b7)
for i in range(b8):
      f.write(b7[i].text + "," + "\n")
      b4.close()
print("fin")