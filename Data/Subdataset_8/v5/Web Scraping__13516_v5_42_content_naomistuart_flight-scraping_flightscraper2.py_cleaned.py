from datetime import datetime
from bs4 import BeautifulSoup
def scrape_flights(terminal, journey, driver):
    today = datetime.today().strftime('%Y-%m-%d')
    flights = {
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
    url = f"https:
    print(f"Getting data for {terminal}_{journey} flights")
    driver.get(url)
    html_soup = BeautifulSoup(driver.page_source, "html.parser")
    flight_containers = html_soup.find_all("div", class_="flight-card")[2:]
    for container in flight_containers:
        flights['Type'].append(f'static/images/{terminal}_{journey}.png')
        flights['Journey'].append(container.find("div", class_="destination-name").text)
        stopover = container.find("div", class_="city-via")
        flights['Stopover'].append(stopover.text if stopover else "-")
        flights['Airline'].append(container.find("span", class_="with-image").text)
        flights['Logo'].append("https:
        flights['Flight number'].append(container.find("div", class_="heading-medium").text)
        flights['Status'].append(container.find("div", class_="status").text)
        flights['Scheduled time'].append(container.find("div", class_="large-scheduled-time").text[:5])
        flights['Estimated time'].append(container.find("div", class_="estimated-time").text[:5])
    print(f"Finished getting data for {terminal}_{journey} flights")
    return flights