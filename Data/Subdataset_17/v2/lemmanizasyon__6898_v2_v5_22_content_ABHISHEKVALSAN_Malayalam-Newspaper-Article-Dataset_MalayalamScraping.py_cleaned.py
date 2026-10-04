import requests
from bs4 import BeautifulSoup
import os
URL_PREFIX = 'https:
def month_to_digit(month):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return month_dict.get(month, '00')
def convert_to_filename(date_str):
    date_parts = date_str.split()
    month_digit = month_to_digit(date_parts[2])
    day = date_parts[1].zfill(2)
    filename = "1" + date_parts[3][2:] + month_digit + day
    return filename, date_parts[3]
def fetch_data(index):
    url = URL_PREFIX + str(index)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.findAll("p", {"class": "text-center"})
        if len(links) != 1:
            title = soup.find("h1").text
            date = soup.findAll("div", {"class": "myd"})[1].text
            content = soup.find("p", {"class": ""}).text
            filename, year = convert_to_filename(date)
            path = "DataSet/"
            filename_with_path = os.path.join(path, f"{filename}{index}.utf8")
            with open(filename_with_path, 'w+', encoding='utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{filename}</DOCNO>\n<TEXT>\n{title}\n{date}\n{content}\n</TEXT>\n</DOC>")
            print(f"Writing file {filename} to {path}")
        else:
            print(f"File missing at {url}")
    else:
        print(f"Error fetching data from {url}")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()