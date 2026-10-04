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
    filename = f"1{date_parts[3][2:]}{month_digit}{day}"
    return filename, date_parts[3]
def fetch_data(index):
    url = f"{URL_PREFIX}{index}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data from {url}")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all("p", class_="text-center")
    if len(links) == 1:
        print(f"File missing at {url}")
        return
    title = soup.find("h1").text
    date = soup.find_all("div", class_="myd")[1].text
    content = soup.find("p", class_="").text
    filename, year = convert_to_filename(date)
    directory = "DataSet"
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, f"{filename}{index}.utf8")
    with open(file_path, 'w+', encoding='utf-8') as file:
        file.write(
            f"<DOC>\n"
            f"<DOCNO>{filename}</DOCNO>\n"
            f"<TEXT>\n"
            f"{title}\n"
            f"{date}\n"
            f"{content}\n"
            f"</TEXT>\n"
            f"</DOC>"
        )
    print(f"Writing file {filename} to {directory}")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()