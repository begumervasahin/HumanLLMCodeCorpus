import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
LECTURE_URL = 'https:
def fetch_webpage(url):
    response = requests.get(url)
    return response.text
def download_file(url, file_name):
    urllib.request.urlretrieve(url, file_name)
    print("Successfully downloaded:", url, "and saved as:", file_name)
def main():
    '''
    Scrapes lecture materials from the webpage and saves them locally.
    Writes all reading links to a PDF file named 'c01_urls.pdf'.
    '''
    source = fetch_webpage(LECTURE_URL)
    pdf = FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    soup = BeautifulSoup(source, 'lxml')
    lecture_notes = soup.find_all('div', class_='notes')
    reading_links = soup.find_all('div', class_='readings')
    for notes_section, links_section in zip(lecture_notes, reading_links):
        note_links = notes_section.find_all('a')
        url_links = links_section.find_all('a')
        for note_link in note_links:
            note_url = note_link['href']
            file_name = note_url.split('/')[-1]
            download_file(LECTURE_URL + note_url, file_name)
        for url_link in url_links:
            pdf.write(5, url_link['href'] + '\n')
            print('Wrote', url_link['href'], 'to the PDF file')
    pdf.output('c01_urls.pdf')
if __name__ == "__main__":
    main()