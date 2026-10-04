from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
def setup_driver(chrome_driver_path):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
def fetch_flight_data(terminal, journey, driver):
    """
    Scrape flight data from Sydney Airport website based on terminal and journey type.
    Args:
        terminal (str): The terminal (e.g., "T1").
        journey (str): The journey type (e.g., "departures").
        driver (WebDriver): The Selenium WebDriver instance.
    Returns:
        dict: A dictionary containing flight data.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    flight_data = {
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
    url = (
        f"https:
        f"&terminalType={terminal}&date={today}&sortColumn=scheduled_time&ascending=true&showAll=true"
    )
    print(f"Getting data for {terminal}_{journey} flights")
    driver.get(url)
    time.sleep(5)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", class_="flight-card")[2:]
    for container in flight_containers:
        flight_data['Type'].append(f'static/images/{terminal}_{journey}.png')
        flight_data['Journey'].append(container.find("div", class_="destination-name").text.strip())
        stopover = container.find("div", class_="city-via")
        flight_data['Stopover'].append(stopover.text.strip() if stopover else "-")
        flight_data['Airline'].append(container.find("span", class_="with-image").text.strip())
        flight_data['Logo'].append("https:
        flight_data['Flight number'].append(container.find("div", class_="heading-medium").text.strip())
        flight_data['Status'].append(container.find("div", class_="status").text.strip())
        flight_data['Scheduled time'].append(container.find("div", class_="large-scheduled-time").text.strip()[:5])
        flight_data['Estimated time'].append(container.find("div", class_="estimated-time").text.strip()[:5])
    print(f"Finished getting data for {terminal}_{journey} flights")
    return flight_data
def save_to_csv(flight_data, filename):
    df = pd.DataFrame(flight_data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
if __name__ == "__main__":
    chrome_driver_path = '/path/to/chromedriver'
    driver = setup_driver(chrome_driver_path)
    terminal = "T1"
    journey = "departures"
    flight_data = fetch_flight_data(terminal, journey, driver)
    driver.quit()
    filename = f"{terminal}_{journey}_flights.csv"
    save_to_csv(flight_data, filename)