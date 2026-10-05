import os
import csv
import re
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
b1 = webdriver.FirefoxProfile()
b1.set_preference("network.proxy.type", 1)
b1.set_preference("network.proxy.http", "200.37.54.10")
b1.set_preference("network.proxy.http_port", 57040)
b1.update_preferences()
a1 = 50
a2 = 5
b2 = webdriver.Firefox(firefox_profile=b1)
for i in range(1, a1 + 1):
  b3 = (a2 - len(str(i))) * "0" + str(i)
  b4 = "http:
  b2.get(b4)
  b5 = b2.find_elements_by_xpath('
  b6 = len(b5)
  with f.open("idmail.csv", "w") as f:
    for i in range(b6):
      f.write(b5[i].text + "," + "\n")
      time.sleep(1)
      f.close()
  b2.close()
  print("fin")