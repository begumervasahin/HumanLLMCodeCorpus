import requests
from bs4 import BeautifulSoup
import os
URL_PREFIX = "http:
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
    day = date_parts[1].zfill(2)
    filename = "1" + date_parts[3][2:] + month + day
    return filename, date_parts[3]
def save_to_file(filename_with_path, filename, title, date, content):
    with open(filename_with_path, 'w', encoding='utf-8') as file:
        file.write(f"<DOC>\n<DOCNO>{filename}.utf8</DOCNO>\n<TEXT>\n{title}\n{date}\n{content}\n</TEXT>\n</DOC>")
    print(f"Writing file {filename}.utf8 to {os.path.dirname(filename_with_path)}")
def get_data(page_id):
    url = URL_PREFIX + str(page_id)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all("p", class_="text-center")
        if len(links) != 1:
            title = soup.find("h1").text
            date = soup.find_all("div", class_="myd")[1].text
            content = soup.find("p", class_="").text
            filename, year = convert_to_filename(date)
            path = "DataSet/"
            os.makedirs(path, exist_ok=True)
            filename_with_path = os.path.join(path, f"{filename}{page_id}.utf8")
            save_to_file(filename_with_path, filename, title, date, content)
        else:
            print(f"File missing at {url}")
    else:
        print(f"Error: Unable to fetch data from {url} (Status code: {response.status_code})")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()