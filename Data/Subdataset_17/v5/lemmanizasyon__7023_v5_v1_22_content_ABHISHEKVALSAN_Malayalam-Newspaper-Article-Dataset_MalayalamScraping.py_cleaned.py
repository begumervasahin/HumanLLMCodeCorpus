import requests
from bs4 import BeautifulSoup
import os
URL_PREFIX = "http:
DATASET_PATH = "DataSet/"
MONTH_TO_DIGIT = {
    'January': '01', 'February': '02', 'March': '03',
    'April': '04', 'May': '05', 'June': '06', 'July': '07',
    'August': '08', 'September': '09', 'October': '10',
    'November': '11', 'December': '12'
}
def month_to_digit(month):
    return MONTH_TO_DIGIT.get(month, '00')
def convert_to_filename(date_string):
    date_parts = date_string.split()
    month = month_to_digit(date_parts[2])
    day = int(date_parts[1])
    year_suffix = date_parts[3][2:]
    filename = f"1{year_suffix}{month}{day:02d}"
    return filename, date_parts[3]
def fetch_data(page_number):
    url = f"{URL_PREFIX}{page_number}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        center_text_elements = soup.find_all("p", {"class": "text-center"})
        if len(center_text_elements) != 1:
            title = soup.find("h1").text
            date_text = soup.find_all("div", {"class": "myd"})[1].text
            content = soup.find("p", {"class": ""}).text
            filename, year = convert_to_filename(date_text)
            filename_with_path = os.path.join(DATASET_PATH, f"{filename}{page_number}.utf8")
            with open(filename_with_path, 'w+', encoding='utf-8') as file:
                file.write(f"<DOC>\n<DOCNO>{filename}</DOCNO>\n<TEXT>\n{title}\n{date_text}\n{content}\n</TEXT>\n</DOC>")
            print(f"Writing file {filename} to {DATASET_PATH}")
        else:
            print(f"File missing at {url}")
    else:
        print(f"Error fetching data from {url}")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()