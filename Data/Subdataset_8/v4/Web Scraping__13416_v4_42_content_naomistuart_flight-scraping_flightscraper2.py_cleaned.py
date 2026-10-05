
from datetime import datetime
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os
import time
def flight_scraper(terminal, journey, driver):
    today = datetime.today().strftime('%Y-%m-%d')
    journies = []
    types = []
    stopovers = []
    airlines = []
    airline_logos = []
    flight_numbers = []
    statuses = []
    scheduled_times = []
    estimated_times = []
    url = "https:
    print("Getting data for {}_{} flights".format(terminal, journey))
    driver.get(url)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", attrs={"class": "flight-card"})[2:]
    for container in flight_containers:
        types.append('static/images/{}_{}.png'.format(terminal, journey))
        journies.append(container.find("div", attrs={"class": "destination-name"}).text)
        if container.find("div", attrs={"class": "city-via"}) is not None:
            stopovers.append(container.find("div", attrs={"class": "city-via"}).text)
        else:
            stopovers.append("-")
        airlines.append(container.find("span", attrs={"class": "with-image"}).text)
        airline_logos.append("https:
        flight_numbers.append(container.find("div", attrs={"class": "heading-medium"}).text)
        statuses.append(container.find("div", attrs={"class": "status"}).text)
        scheduled_times.append(container.find("div", attrs={"class": "large-scheduled-time"}).text[0:5])
        estimated_times.append(container.find("div", attrs={"class": "estimated-time"}).text[0:5])
    flights = {
        'Type': types,
        'Journey': journies,
        'Stopover': stopovers,
        'Airline': airlines,
        'Logo': airline_logos,
        'Flight number': flight_numbers,
        'Status': statuses,
        'Scheduled time': scheduled_times,
        'Estimated time': estimated_times
    }
    print("Finished getting data for {}_{} flights".format(terminal, journey))
    return flights