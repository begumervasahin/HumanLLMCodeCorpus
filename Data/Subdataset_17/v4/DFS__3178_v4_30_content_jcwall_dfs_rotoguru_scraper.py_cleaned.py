import requests
from bs4 import BeautifulSoup as bsoup
def fetch_data(year, week):
    url = f'http:
    response = requests.get(url)
    if response.status_code == 200:
        soup = bsoup(response.content, 'html.parser')
        pre_tags = soup.find_all('pre')
        if pre_tags:
            return pre_tags[0].get_text()
    else:
        print(f"Failed to retrieve data for year {year}, week {week}")
        return None
def write_data_to_csv(data, file_path='test.csv'):
    with open(file_path, 'a+') as file:
        file.write(data)
def grab_first():
    years = [2016, 2015, 2014, 2013]
    weeks = range(1, 17)
    last_pre_tag = None
    for year in years:
        for week in weeks:
            data = fetch_data(year, week)
            if data:
                write_data_to_csv(data)
                last_pre_tag = data
    return last_pre_tag
if __name__ == '__main__':
    last_pre_tag = grab_first()
    print('Data fetching complete.')