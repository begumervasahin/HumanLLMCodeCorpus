from selenium import webdriver
from selenium.webdriver.chrome.b11 import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import numpy as np
import pandas as pd
def fonk1(b18, b19):
    b1 = datetime.b1().strftime('%Y-%m-%d')
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = Service(ChromeDriverManager().install())
    b12 = webdriver.Chrome(b11=b11)
    b13 = "https:
    print("Getting data for {}_{} b17".format(b18, b19))
    b12.get(b13)
    b14 = BeautifulSoup(b12.page_source, "html.parser")
    b15 = b14.find_all("div", b16={"class": "flight-card"})[2:]
    for container in b15:
        b3.append('static/images/{}_{}.png'.format(b18, b19))
        b2.append(container.find("div", b16 = {"class": "destination-name"}).text)
        if container.find("div", b16 = {"class": "city-via"}) is not None:
            b4.append(container.find("div", b16 = {"class": "city-via"}).text)
        else:
            b4.append("-")
        b5.append(container.find("span", b16 = {"class": "with-image"}).text)
        b6.append("https:
        b7.append(container.find("div", b16 = {"class": "heading-medium"}).text)
        b8.append(container.find("div", b16 = {"class": "status"}).text)
        b9.append(container.find("div", b16 = {"class": "large-scheduled-time"}).text[0:5])
        b10.append(container.find("div", b16 = {"class": "estimated-time"}).text[0:5])
    b17 = {
        'Type': b3,
        'Journey': b2,
        'Stopover': b4,
        'Airline': b5,
        'Logo': b6,
        'Flight number': b7,
        'Status': b8,
        'Scheduled time': b9,
        'Estimated time': b10
    }
    print("Finished getting data for {}_{} b17".format(b18, b19))
    b12.quit()
    return b17
b18 = "example_terminal"
b19 = "example_journey"
b20 = fonk1(b18, b19)
print(pd.DataFrame(b20))