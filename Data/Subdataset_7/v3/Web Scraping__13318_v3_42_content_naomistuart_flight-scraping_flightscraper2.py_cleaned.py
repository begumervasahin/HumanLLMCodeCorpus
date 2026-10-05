from selenium import webdriver
from selenium.webdriver.chrome.b2 import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
def fonk1():
    return datetime.b6().strftime('%Y-%m-%d')
def fonk2():
    return {
        'Type': [],
        'Journey': [],
        'Stopover': [],
        'Airline': [],
        'Logo': [],
        'Flight number': [],
        'Status': [],
        'Scheduled time': [],
        'Estimated time': []
    }
def fonk3():
    b1 = ChromeDriverManager().install()
    b2 = Service(b1)
    return webdriver.Chrome(b2 = b2)
def fonk4(b12, b13, b6):
    return f"https:
def fonk5(b11, b12, b13):
    b3 = fonk2()
    for container in b11:
        b3['Type'].append(f'static/images/{b12}_{b13}.png')
        b3['Journey'].append(container.find("div", b4 = {"class": "destination-name"}).text)
        b5 = container.find("div", b4={"class": "city-via"})
        b3['Stopover'].append(b5.text if b5 else "-")
        b3['Airline'].append(container.find("span", b4 = {"class": "with-image"}).text)
        b3['Logo'].append("https:
        b3['Flight number'].append(container.find("div", b4 = {"class": "heading-medium"}).text)
        b3['Status'].append(container.find("div", b4 = {"class": "status"}).text)
        b3['Scheduled time'].append(container.find("div", b4 = {"class": "large-scheduled-time"}).text[0:5])
        b3['Estimated time'].append(container.find("div", b4 = {"class": "estimated-time"}).text[0:5])
    return b3
def fonk6(b12, b13):
    b6 = fonk1()
    b7 = fonk2()
    print(f"Getting data for {b12}_{b13} flights")
    b8 = fonk3()
    b9 = fonk4(b12, b13, b6)
    b8.get(b9)
    b10 = BeautifulSoup(b8.page_source, "html.parser")
    b11 = b10.find_all("div", b4={"class": "flight-card"})[2:]
    b7 = fonk5(b11, b12, b13)
    print(f"Finished getting data for {b12}_{b13} flights")
    b8.quit()
    return b7
b12 = "example_terminal"
b13 = "example_journey"
b7 = fonk6(b12, b13)
print(pd.DataFrame(b7))