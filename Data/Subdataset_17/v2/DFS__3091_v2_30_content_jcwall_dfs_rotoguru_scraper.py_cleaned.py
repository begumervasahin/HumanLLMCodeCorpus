import requests
from bs4 import BeautifulSoup as bsoup
def fetch_and_write_data(file_path='data.csv'):
    years = [2016, 2015, 2014, 2013]
    weeks = range(1, 17)
    with open(file_path, 'a+') as file:
        for year in years:
            for week in weeks:
                url = f'http:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = bsoup(response.content, 'html.parser')
                    pre_tags = soup.find_all('pre')
                    if pre_tags:
                        file.write(pre_tags[0].get_text())
                else:
                    print(f"Failed to retrieve data for year {year}, week {week}")
    print(f'Data has been written to {file_path}')
    return pre_tags
if __name__ == '__main__':
    pre_tags = fetch_and_write_data()