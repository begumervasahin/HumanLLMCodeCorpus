from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
def flight_scraper(terminal, journey):
    today = datetime.today().strftime('%Y-%m-%d')
    journeys = []
    types = []
    stopovers = []
    airlines = []
    airline_logos = []
    flight_numbers = []
    statuses = []
    scheduled_times = []
    estimated_times = []
    chrome_driver = ChromeDriverManager().install()
    service = Service(chrome_driver)
    driver = webdriver.Chrome(service=service)
    url = f"https:
    print(f"Getting data for {terminal}_{journey} flights")
    driver.get(url)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", attrs={"class": "flight-card"})[2:]
    for container in flight_containers:
        types.append(f'static/images/{terminal}_{journey}.png')
        journeys.append(container.find("div", attrs={"class": "destination-name"}).text)
        stopover_elem = container.find("div", attrs={"class": "city-via"})
        stopovers.append(stopover_elem.text if stopover_elem else "-")
        airlines.append(container.find("span", attrs={"class": "with-image"}).text)
        airline_logos.append("https:
        flight_numbers.append(container.find("div", attrs={"class": "heading-medium"}).text)
        statuses.append(container.find("div", attrs={"class": "status"}).text)
        scheduled_times.append(container.find("div", attrs={"class": "large-scheduled-time"}).text[0:5])
        estimated_times.append(container.find("div", attrs={"class": "estimated-time"}).text[0:5])
    flights = {
        'Type': types,
        'Journey': journeys,
        'Stopover': stopovers,
        'Airline': airlines,
        'Logo': airline_logos,
        'Flight number': flight_numbers,
        'Status': statuses,
        'Scheduled time': scheduled_times,
        'Estimated time': estimated_times
    }
    print(f"Finished getting data for {terminal}_{journey} flights")
    driver.quit()
    return flights
terminal = "example_terminal"
journey = "example_journey"
flights_data = flight_scraper(terminal, journey)
print(pd.DataFrame(flights_data))