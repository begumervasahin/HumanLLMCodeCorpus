from bs4 import BeautifulSoup
import urllib3
class Scraper:
    def __init__(self):
        self.rates = {}
        self.currency_to_key = {}
        self.key_to_currency = {}
        self.next_key = 0
        self.scrape()
    def try_generate_key(self, currency_str):
        if currency_str not in self.currency_to_key:
            self.currency_to_key[currency_str] = self.next_key
            self.key_to_currency[self.next_key] = currency_str
            self.next_key += 1
    def scrape(self):
        base_url = "http:
        http = urllib3.PoolManager()
        response_main = http.request('GET', base_url)
        soup_main = BeautifulSoup(response_main.data, "lxml")
        currency_list = soup_main.find("ul", class_="currencyList ratestable")
        for currency_link in currency_list.find_all("a"):
            currency_name = currency_link.text
            self.try_generate_key(currency_name)
            page_url = f"{base_url}{currency_link['href']}&amount=1"
            response = http.request('GET', page_url)
            soup = BeautifulSoup(response.data, "lxml")
            tables = soup.find_all("table")
            for table in tables:
                t_body = table.find("tbody")
                rows = t_body.find_all("tr")
                for row in rows:
                    columns = [item.text.strip() for item in row.find_all("td")]
                    target_currency = columns[0]
                    self.try_generate_key(target_currency)
                    forward_key = (self.currency_to_key[currency_name], self.currency_to_key[target_currency])
                    reverse_key = (forward_key[1], forward_key[0])
                    if forward_key not in self.rates:
                        self.rates[forward_key] = float(columns[1])
                        self.rates[reverse_key] = float(columns[2])
if __name__ == '__main__':
    scraper = Scraper()
    print(scraper.rates)