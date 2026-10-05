from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
def get_today_date():
    return datetime.today().strftime('%Y-%m-%d')
def initialize_lists():
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
def setup_webdriver():
    chrome_driver = ChromeDriverManager().install()
    service = Service(chrome_driver)
    return webdriver.Chrome(service=service)
def construct_url(terminal, journey, today):
    return f"https:
def extract_flight_data(flight_containers, terminal, journey):
    flight_data = initialize_lists()
    for container in flight_containers:
        flight_data['Type'].append(f'static/images/{terminal}_{journey}.png')
        flight_data['Journey'].append(container.find("div", attrs={"class": "destination-name"}).text)
        stopover_elem = container.find("div", attrs={"class": "city-via"})
        flight_data['Stopover'].append(stopover_elem.text if stopover_elem else "-")
        flight_data['Airline'].append(container.find("span", attrs={"class": "with-image"}).text)
        flight_data['Logo'].append("https:
        flight_data['Flight number'].append(container.find("div", attrs={"class": "heading-medium"}).text)
        flight_data['Status'].append(container.find("div", attrs={"class": "status"}).text)
        flight_data['Scheduled time'].append(container.find("div", attrs={"class": "large-scheduled-time"}).text[0:5])
        flight_data['Estimated time'].append(container.find("div", attrs={"class": "estimated-time"}).text[0:5])
    return flight_data
def scrape_flights(terminal, journey):
    today = get_today_date()
    flights_data = initialize_lists()
    print(f"Getting data for {terminal}_{journey} flights")
    driver = setup_webdriver()
    url = construct_url(terminal, journey, today)
    driver.get(url)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", attrs={"class": "flight-card"})[2:]
    flights_data = extract_flight_data(flight_containers, terminal, journey)
    print(f"Finished getting data for {terminal}_{journey} flights")
    driver.quit()
    return flights_data
terminal = "example_terminal"
journey = "example_journey"
flights_data = scrape_flights(terminal, journey)
print(pd.DataFrame(flights_data))