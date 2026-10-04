from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver
def flightscraper2(terminal, journey, driver):
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
    url = f"https:
    print(f"Getting data for {terminal}_{journey} flights")
    driver.get(url)
    time.sleep(5)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", class_="flight-card")[2:]
    for container in flight_containers:
        types.append(f'static/images/{terminal}_{journey}.png')
        journies.append(container.find("div", class_="destination-name").text.strip())
        stopover = container.find("div", class_="city-via")
        stopovers.append(stopover.text.strip() if stopover else "-")
        airlines.append(container.find("span", class_="with-image").text.strip())
        airline_logos.append("https:
        flight_numbers.append(container.find("div", class_="heading-medium").text.strip())
        statuses.append(container.find("div", class_="status").text.strip())
        scheduled_times.append(container.find("div", class_="large-scheduled-time").text.strip()[:5])
        estimated_times.append(container.find("div", class_="estimated-time").text.strip()[:5])
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
if __name__ == "__main__":
    driver = setup_driver()
    terminal = "T1"
    journey = "departures"
    flight_data = flightscraper2(terminal, journey, driver)
    driver.quit()
    df = pd.DataFrame(flight_data)
    df.to_csv(f"{terminal}_{journey}_flights.csv", index=False)
    print("Data saved to CSV file")