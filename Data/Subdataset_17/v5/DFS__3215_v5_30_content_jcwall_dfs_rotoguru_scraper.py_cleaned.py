import requests
from bs4 import BeautifulSoup as bsoup
def fetch_data(year, week):
    url = f'http:
    response = requests.get(url)
    if response.status_code == 200:
        soup = bsoup(response.content, 'html.parser')
        pre_tag = soup.find('pre')
        if pre_tag:
            return pre_tag.get_text()
        else:
            print(f"No <pre> tag found for year {year}, week {week}")
    else:
        print(f"Failed to retrieve data for year {year}, week {week}")
    return None
def write_data_to_csv(data, file_path='test.csv'):
    with open(file_path, 'a+') as file:
        file.write(data)
def grab_data(years, weeks, file_path='test.csv'):
    last_pre_tag = None
    for year in years:
        for week in weeks:
            data = fetch_data(year, week)
            if data:
                write_data_to_csv(data, file_path)
                last_pre_tag = data
    print(f'Data has been written to {file_path}')
    return last_pre_tag
if __name__ == '__main__':
    years = [2016, 2015, 2014, 2013]
    weeks = range(1, 17)
    last_pre_tag = grab_data(years, weeks)
    print('Data fetching complete.')