from datetime import datetime
from bs4 import BeautifulSoup
def fonk1(terminal, journey, driver):
    b1 = datetime.b1().strftime('%Y-%m-%d')
    b2 = {
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
    b3 = f"https:
    print(f"Getting data for {terminal}_{journey} b2")
    driver.get(b3)
    b4 = BeautifulSoup(driver.page_source, "html.parser")
    b5 = b4.find_all("div", b6="flight-card")[2:]
    for container in b5:
        b2['Type'].append(f'static/images/{terminal}_{journey}.png')
        b2['Journey'].append(container.find("div", b6 = "destination-name").text)
        b7 = container.find("div", b6="city-via")
        b2['Stopover'].append(b7.text if b7 else "-")
        b2['Airline'].append(container.find("span", b6 = "with-image").text)
        b2['Logo'].append("https:
        b2['Flight number'].append(container.find("div", b6 = "heading-medium").text)
        b2['Status'].append(container.find("div", b6 = "status").text)
        b2['Scheduled time'].append(container.find("div", b6 = "large-scheduled-time").text[:5])
        b2['Estimated time'].append(container.find("div", b6 = "estimated-time").text[:5])
    print(f"Finished getting data for {terminal}_{journey} b2")
    return b2