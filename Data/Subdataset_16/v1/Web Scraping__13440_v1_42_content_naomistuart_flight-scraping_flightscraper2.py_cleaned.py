from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
def fonk1():
    b1 = Options()
    b1.add_argument("--headless")
    b2 = Service('/path/to/chromedriver')
    b3 = webdriver.Chrome(service=b2, options=b1)
    return b3
def fonk2(b21, b22, b3):
    b4 = datetime.b4().strftime('%Y-%m-%d')
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = f"https:
    print(f"Getting data for {b21}_{b22} b19")
    b3.get(b14)
    time.sleep(5)
    b15 = BeautifulSoup(b3.page_source, "html.parser")
    b16 = b15.find_all("div", b17="flight-card")[2:]
    for container in b16:
        b6.append(f'static/images/{b21}_{b22}.png')
        b5.append(container.find("div", b17 = "destination-name").text.strip())
        b18 = container.find("div", b17="city-via")
        b7.append(b18.text.strip() if b18 else "-")
        b8.append(container.find("span", b17 = "with-image").text.strip())
        b9.append("https:
        b10.append(container.find("div", b17 = "heading-medium").text.strip())
        b11.append(container.find("div", b17 = "status").text.strip())
        b12.append(container.find("div", b17 = "large-scheduled-time").text.strip()[:5])
        b13.append(container.find("div", b17 = "estimated-time").text.strip()[:5])
    b19 = {
        'Type': b6,
        'Journey': b5,
        'Stopover': b7,
        'Airline': b8,
        'Logo': b9,
        'Flight number': b10,
        'Status': b11,
        'Scheduled time': b12,
        'Estimated time': b13
    }
    print(f"Finished getting data for {b21}_{b22} b19")
    return b19
if b20 = = "__main__":
    b3 = fonk1()
    b21 = "T1"
    b22 = "departures"
    b23 = fonk2(b21, b22, b3)
    b3.quit()
    b24 = pd.DataFrame(b23)
    b24.to_csv(f"{b21}_{b22}_flights.csv", b25 = False)
    print("Data saved to CSV file")