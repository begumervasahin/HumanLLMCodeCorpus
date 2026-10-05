import requests
from bs4 import BeautifulSoup
import os
import constants as const
def month_to_digit(month):
    month_dict = {'January': '01', 'February': '02', 'March': '03',
                  'April': '04', 'May': '05', 'June': '06', 'July': '07',
                  'August': '08', 'September': '09', 'October': '10',
                  'November': '11', 'December': '12'}
    return month_dict.get(month, '00')
def convert_to_filename(s):
    flist = s.split()
    m = month_to_digit(flist[2])
    day = flist[1].zfill(2)
    filename = "1" + flist[3][2:] + m + day
    return filename, flist[3]
def get_data(i):
    url = const.URL_PREFIX + str(i)
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.findAll("p", {"class": "text-center"})
        if len(links) != 1:
            title = soup.findAll("h1")[0].text
            date = soup.findAll("div", {"class": "myd"})[1].text
            content = soup.findAll("p", {"class": ""})[0].text
            filename, year = convert_to_filename(date)
            path = "DataSet/"
            filename = filename + str(i) + ".utf8"
            filename_with_path = os.path.join(path, filename)
            with open(filename_with_path, 'w+') as f:
                f.write(f"<DOC>\n<DOCNO>{filename}</DOCNO>\n<TEXT>\n{title}\n{date}\n{content}\n</TEXT>\n</DOC>")
            print(f"Writing file {filename} to {path}")
        else:
            print(f"File missing at {url}")
    else:
        print("Error")
def main():
    print('This program is obsolete since the website structure has changed')
if __name__ == "__main__":
    main()