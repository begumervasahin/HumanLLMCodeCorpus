import requests
from bs4 import BeautifulSoup
import os
import constants as const
def month_to_digit(month):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03',
        'April': '04', 'May': '05', 'June': '06', 'July': '07',
        'August': '08', 'September': '09', 'October': '10',
        'November': '11', 'December': '12'
    }
    return month_dict.get(month, '00')
def convert_to_filename(date_string):
    """
    Converts a date string into a valid filename.
    Args:
        date_string (str): Date in the format "Day Month Year".
    Returns:
        tuple: Filename and year extracted from the date string.
    """
    date_parts = date_string.split()
    month_digit = month_to_digit(date_parts[2])
    day = f"0{date_parts[1]}" if int(date_parts[1]) < 10 else date_parts[1]
    year_suffix = date_parts[3][2:]
    filename = f"1{year_suffix}{month_digit}{day}"
    return filename, date_parts[3]
def fetch_data(index):
    url = f"{const.URL_PREFIX}{index}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_center_paragraphs = soup.find_all("p", {"class": "text-center"})
        if len(text_center_paragraphs) != 1:
            title = soup.find("h1").text
            date_info = soup.find_all("div", {"class": "myd"})[1].text
            main_text = soup.find("p", {"class": ""}).text
            full_text = f"{title}\n{date_info}\n{main_text}"
            filename, year = convert_to_filename(date_info)
            directory_path = "DataSet"
            os.makedirs(directory_path, exist_ok=True)
            complete_filename = f"{filename}{index}.utf8"
            full_file_path = os.path.join(directory_path, complete_filename)
            with open(full_file_path, 'w+', encoding='utf-8') as file:
                file_content = f"<DOC>\n<DOCNO>{complete_filename}</DOCNO>\n<TEXT>\n{full_text}\n</TEXT>\n</DOC>"
                file.write(file_content)
            print(f"Writing file {complete_filename} to {directory_path}")
        else:
            print(f"File missing at {url}")
    else:
        print("Error")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()