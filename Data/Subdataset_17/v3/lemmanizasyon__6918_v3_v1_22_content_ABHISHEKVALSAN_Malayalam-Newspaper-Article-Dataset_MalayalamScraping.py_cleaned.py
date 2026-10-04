import requests
from bs4 import BeautifulSoup
import os
URL_PREFIX = "http:
DATASET_PATH = "DataSet/"
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
    month = month_to_digit(date_parts[2])
    day = date_parts[1]
    year_suffix = date_parts[3][2:]
    if int(day) < 10:
        filename = f"1{year_suffix}{month}0{day}"
    else:
        filename = f"1{year_suffix}{month}{day}"
    return filename, date_parts[3]
def fetch_and_save_data(page_number):
    url = f"{URL_PREFIX}{page_number}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data from {url}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("p", class_="text-center")
    if len(links) == 1:
        print(f"File missing at {url}")
        return
    header = soup.find("h1").text
    date_info = soup.find_all("div", class_="myd")[1].text
    content = soup.find("p", class_="").text
    text_data = f"{header}\n{date_info}\n{content}"
    filename, year = convert_to_filename(date_info)
    filename = f"{filename}{page_number}.utf8"
    filepath = os.path.join(DATASET_PATH, filename)
    os.makedirs(DATASET_PATH, exist_ok=True)
    with open(filepath, 'w+', encoding='utf-8') as file:
        file.write(f"<DOC>\n<DOCNO>{filename}</DOCNO>\n<TEXT>\n{text_data}\n</TEXT>\n</DOC>")
    print(f"Writing file {filename} to {DATASET_PATH}")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()