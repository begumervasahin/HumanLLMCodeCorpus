import requests
from bs4 import BeautifulSoup
import os
URL_PREFIX = "http:
DATASET_PATH = "DataSet/"
def month_to_digit(month):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09',
        'October': '10', 'November': '11', 'December': '12'
    }
    return month_dict.get(month, '00')
def convert_to_filename(date_str):
    date_components = date_str.split()
    year = date_components[3][2:]
    month = month_to_digit(date_components[2])
    day = date_components[1]
    filename = f"1{year}{month}{day.zfill(2)}"
    return filename, date_components[3]
def get_data(page_number):
    url = URL_PREFIX + str(page_number)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.findAll("p", {"class": "text-center"})
        if len(paragraphs) != 1:
            title = soup.findAll("h1")[0].text
            date_info = soup.findAll("div", {"class": "myd"})[1].text
            content = soup.findAll("p", {"class": ""})[0].text
            filename, year = convert_to_filename(date_info)
            file_path = os.path.join(DATASET_PATH, filename + str(page_number) + ".utf8")
            with open(file_path, 'w+') as file:
                file.write(
                    "<DOC>\n<DOCNO>" + filename + "</DOCNO>\n<TEXT>\n" +
                    title + "\n" + date_info + "\n" + content +
                    "\n</TEXT>\n</DOC>"
                )
            print("File " + filename + " written to " + DATASET_PATH)
        else:
            print("File missing at " + url)
    else:
        print("Error fetching data from " + url)
def main():
    print("This program is obsolete since the website structure has changed.")
if __name__ == "__main__":
    main()