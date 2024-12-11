from selenium import webdriver
from selenium.webdriver.chrome.b12 import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
def fonk1(b20, b21):
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
    b11 = ChromeDriverManager().install()
    b12 = Service(b11)
    b13 = webdriver.Chrome(b12=b12)
    b14 = f"https:
    print(f"Getting data for {b20}_{b21} b19")
    b13.get(b14)
    b15 = BeautifulSoup(b13.page_source, "html.parser")
    b16 = b15.find_all("div", b17={"class": "flight-card"})[2:]
    for container in b16:
        b3.append(f'static/images/{b20}_{b21}.png')
        b2.append(container.find("div", b17 = {"class": "destination-name"}).text)
        b18 = container.find("div", b17={"class": "city-via"})
        b4.append(b18.text if b18 else "-")
        b5.append(container.find("span", b17 = {"class": "with-image"}).text)
        b6.append("https:
        b7.append(container.find("div", b17 = {"class": "heading-medium"}).text)
        b8.append(container.find("div", b17 = {"class": "status"}).text)
        b9.append(container.find("div", b17 = {"class": "large-scheduled-time"}).text[0:5])
        b10.append(container.find("div", b17 = {"class": "estimated-time"}).text[0:5])
    b19 = {
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
    print(f"Finished getting data for {b20}_{b21} b19")
    b13.quit()
    return b19
b20 = "example_terminal"
b21 = "example_journey"
b22 = fonk1(b20, b21)
print(pd.DataFrame(b22))