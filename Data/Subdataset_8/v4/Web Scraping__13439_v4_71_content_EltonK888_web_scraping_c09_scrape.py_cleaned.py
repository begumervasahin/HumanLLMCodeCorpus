import urllib.request
from bs4 import BeautifulSoup
import requests
import fpdf
URL = 'https:
source = requests.get(URL).text
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
soup = BeautifulSoup(source, 'lxml')
def main():
    '''
    Finds the name of every lecture pdf and saves it to current directory
    writes all reading links to a pdf called c09_readings.pdf
    '''
    table_notes = soup.find_all('div', class_='notes')
    table_urls = soup.find_all('div', class_='readings')
    for i in range(len(table_notes)):
        try:
            cur_files = table_notes[i].find_all('a')
            cur_urls = table_urls[i].find_all('a')
        except:
            pass
        else:
            for j in range(len(cur_files)):
                cur = cur_files[j]['href']
                file_name = cur.split('/')[-1]
                urllib.request.urlretrieve(URL+cur, file_name)
                print("Successfully downloaded: " + cur + " and saved as: " + file_name)
            for k in range(len(cur_urls)):
                cur_url = cur_urls[k]['href']
                pdf.write(5, cur_url+'\n', cur_url)
                print('Wrote ' + cur_url + " to PDF file")
    pdf.output('c09_urls.pdf')
if __name__ == "__main__":
    main()