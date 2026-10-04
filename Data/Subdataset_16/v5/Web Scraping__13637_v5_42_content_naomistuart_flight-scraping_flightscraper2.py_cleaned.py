from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
def fonk1(terminal, journey, driver):
    b1 = datetime.b1().strftime('%Y-%m-%d')
    b2 = (
        f"https:
        f"&b3 = {terminal}&date={b1}"
        f"&b4 = scheduled_time&ascending=true&showAll=true"
    )
    print(f"Getting data for {terminal}_{journey} b11")
    driver.get(b2)
    b5 = BeautifulSoup(driver.page_source, "html.parser")
    b6 = b5.find_all("div", b9="flight-card")[2:]
    types, journeys, stopovers, airlines, b7 = [], [], [], [], []
    flight_numbers, statuses, scheduled_times, b8 = [], [], [], []
    for container in b6:
        types.append(f'static/images/{terminal}_{journey}.png')
        journeys.append(container.find("div", b9 = "destination-name").text)
        b10 = container.find("div", b9="city-via")
        stopovers.append(b10.text if b10 else "-")
        airlines.append(container.find("span", b9 = "with-image").text)
        b7.append("https:
        flight_numbers.append(container.find("div", b9 = "heading-medium").text)
        statuses.append(container.find("div", b9 = "status").text)
        scheduled_times.append(container.find("div", b9 = "large-scheduled-time").text[:5])
        b8.append(container.find("div", b9 = "estimated-time").text[:5])
    b11 = {
        'Type': types,
        'Journey': journeys,
        'Stopover': stopovers,
        'Airline': airlines,
        'Logo': b7,
        'Flight number': flight_numbers,
        'Status': statuses,
        'Scheduled time': scheduled_times,
        'Estimated time': b8
    }
    print(f"Finished getting data for {terminal}_{journey} b11")
    return b11