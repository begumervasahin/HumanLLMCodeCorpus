import urllib.request
import fpdf
import requests
from bs4 import BeautifulSoup
URL = r'https:
source_code = requests.get(URL).text
pdf_document = fpdf.FPDF(format='letter')
pdf_document.add_page()
pdf_document.set_font("Arial", size=12)
soup = BeautifulSoup(source_code, 'lxml')
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
            for link in lecture_links:
                file_url = URL + link['href']
                file_name = link['href'].split('/')[-1]
                urllib.request.urlretrieve(file_url, file_name)
                print(f"Downloaded: {file_url} -> {file_name}")
            for link in reading_links:
                url = link['href']
                pdf_document.write(5, url + '\n')
                print(f"Wrote: {url} to PDF file")
    pdf_document.output('c01_urls.pdf')
if __name__ == "__main__":
    main()