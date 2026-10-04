import csv
import requests
from bs4 import BeautifulSoup
list_of_rows = []
def save_proxy():
    filename = input("Enter the file name to save the proxies: ")
    with open(filename + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'Port'])
        for row in list_of_rows:
            writer.writerow(row)
    print(f"File saved successfully as {filename}.csv")
def make_soup(url):
    try:
        page = requests.get(url)
        page.raise_for_status()
        print(f"{url} scraped successfully")
        return BeautifulSoup(page.text, "lxml")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return None
def proxy_scrape(table):
    if table:
        for row in table.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) > 1:
                ip = cells[0].text.strip()
                port = cells[1].text.strip()
                list_of_rows.append([ip, port])
def scrape_proxies(url):
    soup = make_soup(url)
    if soup:
        table = soup.find('table', attrs={'id': 'proxylisttable'})
        proxy_scrape(table)
def menu():
    print("   _______      ___      .______      .______       _______ .___________.___________. ")
    print("  /  _____|    /   \     |   _  \     |   _  \     |   ____||           |           | ")
    print(" |  |  __     /  ^  \    |  |_)  |    |  |_)  |    |  |__   `---|  |----`---|  |----` ")
    print(" |  | |_ |   /  /_\\  \\   |      /     |      /     |   __|      |  |        |  |      ")
    print(" |  |__| |  /  _____  \\  |  |\\  \\----.|  |\\  \\----.|  |____     |  |        |  |      ")
    print("  \\______| /__/     \\__\\ | _| `._____|| _| `._____||_______|    |__|        |__|      ")
    print("")
    print("Please select a source to scrape proxies from:")
    print(" 1. https:
    print(" 2. https:
    print(" 3. https:
    print(" 4. https:
    print(" 5. Exit")
    choice = input("Option: ")
    return int(choice)
def main():
    while True:
        choice = menu()
        if choice == 1:
            scrape_proxies(url="https:
        elif choice == 2:
            scrape_proxies(url="https:
        elif choice == 3:
            scrape_proxies(url="https:
        elif choice == 4:
            scrape_proxies(url="https:
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
        if 1 <= choice <= 4:
            save_proxy()
            list_of_rows.clear()
if __name__ == "__main__":
    main()