import csv
import requests
from bs4 import BeautifulSoup
list_of_rows = []
def save_proxy():
    filename = input("File Name: ")
    with open(filename + '.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP', 'Port'])
        for row in list_of_rows:
            writer.writerow(row)
    print("File Saved Successfully")
def make_soup(url):
    response = requests.get(url)
    print(f"{url} scraped successfully")
    return BeautifulSoup(response.text, "lxml")
def proxy_scrape(table):
    for row in table.find_all('tr'):
        list_of_cells = []
        for cell in row.find_all('td'):
            text = cell.text.strip()
            list_of_cells.append(text)
        if list_of_cells:
            list_of_rows.append(list_of_cells[:2])
def scrape_proxies(url):
    soup = make_soup(url)
    proxy_table = soup.find('table', attrs={'id': 'proxylisttable'})
    if proxy_table:
        proxy_scrape(proxy_table)
    else:
        print("Proxy table not found on the page.")
def menu():
    print()
    print("Please Select A Source To Scrape From:")
    print(" 1. http:
    print(" 2. http:
    print(" 3. http:
    print(" 4. http:
    print(" 5. Exit")
    choice = input("Option: ")
    return int(choice)
def main():
    while True:
        choice = menu()
        if choice == 1:
            scrape_proxies("https:
        elif choice == 2:
            scrape_proxies("https:
        elif choice == 3:
            scrape_proxies("https:
        elif choice == 4:
            scrape_proxies("https:
        elif choice == 5:
            break
        else:
            print("Invalid choice!")
        if 1 <= choice <= 4:
            save_proxy()
            break
if __name__ == "__main__":
    main()