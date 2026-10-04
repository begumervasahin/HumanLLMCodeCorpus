from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
def flightscraper2(terminal, journey, driver):
    today = datetime.today().strftime('%Y-%m-%d')
    url = (
        f"https:
        f"&terminalType={terminal}&date={today}"
        f"&sortColumn=scheduled_time&ascending=true&showAll=true"
    )
    print(f"Getting data for {terminal}_{journey} flights")
    driver.get(url)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", class_="flight-card")[2:]
    types, journies, stopovers, airlines, airline_logos = [], [], [], [], []
    flight_numbers, statuses, scheduled_times, estimated_times = [], [], [], []
    for container in flight_containers:
        types.append(f'static/images/{terminal}_{journey}.png')
        journies.append(container.find("div", class_="destination-name").text)
        stopover = container.find("div", class_="city-via")
        stopovers.append(stopover.text if stopover else "-")
        airlines.append(container.find("span", class_="with-image").text)
        airline_logos.append("https:
        flight_numbers.append(container.find("div", class_="heading-medium").text)
        statuses.append(container.find("div", class_="status").text)
        scheduled_times.append(container.find("div", class_="large-scheduled-time").text[:5])
        estimated_times.append(container.find("div", class_="estimated-time").text[:5])
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
    print(f"Finished getting data for {terminal}_{journey} flights")
    return flights