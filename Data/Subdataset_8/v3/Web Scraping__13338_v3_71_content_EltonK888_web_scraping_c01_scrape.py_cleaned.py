import urllib.request
import fpdf
import requests
from bs4 import BeautifulSoup
LECTURE_URL = r'https:
source_code = requests.get(LECTURE_URL).text
pdf_document = fpdf.FPDF(format='letter')
pdf_document.add_page()
pdf_document.set_font("Arial", size=12)
soup = BeautifulSoup(source_code, 'lxml')
def download_lecture_notes(lecture_links):
    for link in lecture_links:
        file_url = LECTURE_URL + link['href']
        file_name = link['href'].split('/')[-1]
        urllib.request.urlretrieve(file_url, file_name)
        print(f"Downloaded: {file_url} -> {file_name}")
def write_reading_urls_to_pdf(reading_links):
    for link in reading_links:
        url = link['href']
        pdf_document.write(5, url + '\n')
        print(f"Wrote: {url} to PDF file")
def main():
    '''
    Scrapes lecture notes and reading URLs, saves lecture notes to current directory,
    and writes reading URLs to a PDF file called c01_urls.pdf.
    '''
    lecture_notes = soup.find_all('div', class_='notes')
    reading_urls = soup.find_all('div', class_='readings')
    for i in range(len(lecture_notes)):
        try:
            lecture_links = lecture_notes[i].find_all('a')
            reading_links = reading_urls[i].find_all('a')
        except:
            pass
        else:
            download_lecture_notes(lecture_links)
            write_reading_urls_to_pdf(reading_links)
    pdf_document.output('c01_urls.pdf')
if __name__ == "__main__":
    main()