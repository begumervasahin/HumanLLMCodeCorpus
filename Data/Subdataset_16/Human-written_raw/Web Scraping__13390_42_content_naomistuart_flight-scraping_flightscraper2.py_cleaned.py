def fonk1(terminal, journey, driver):
    from datetime import datetime
    from bs4 import BeautifulSoup
    import numpy as np
    import pandas as pd
    import os
    import time
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
    b11 = "https:
    print("Getting data for {}_{} b15".format(terminal, journey))
    driver.get(b11)
    b12 = BeautifulSoup(driver.page_source, "html.parser")
    b13 = b12.find_all("div", b14={"class": "flight-card"})[2:]
    for container in b13:
        b3.append('static/images/{}_{}.png'.format(terminal, journey))
        b2.append(container.find("div", b14 = {"class": "destination-name"}).text)
        if container.find("div", b14 = {"class": "city-via"}) is not None:
            b4.append(container.find("div", b14 = {"class": "city-via"}).text)
        else:
            b4.append("-")
        b5.append(container.find("span", b14 = {"class": "with-image"}).text)
        b6.append("https:
        b7.append(container.find("div", b14 = {"class": "heading-medium"}).text)
        b8.append(container.find("div", b14 = {"class": "status"}).text)
        b9.append(container.find("div", b14 = {"class": "large-scheduled-time"}).text[0:5])
        b10.append(container.find("div", b14 = {"class": "estimated-time"}).text[0:5])
    b15 = {
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
    print("Finished getting data for {}_{} b15".format(terminal, journey))
    return b15