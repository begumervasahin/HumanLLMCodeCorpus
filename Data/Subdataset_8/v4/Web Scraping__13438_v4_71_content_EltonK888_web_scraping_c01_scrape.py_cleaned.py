import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
URL = 'https:
source = requests.get(URL).text
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
soup = BeautifulSoup(source, 'lxml')
def main():
    '''
    Scrapes lecture materials from the webpage and saves them locally.
    Writes all reading links to a PDF file named 'c01_readings.pdf'.
    '''
    lecture_notes = soup.find_all('div', class_='notes')
    reading_links = soup.find_all('div', class_='readings')
    for i in range(len(lecture_notes)):
        try:
            note_links = lecture_notes[i].find_all('a')
            url_links = reading_links[i].find_all('a')
        except:
            pass
        else:
            for note in note_links:
                note_url = note['href']
                file_name = note_url.split('/')[-1]
                urllib.request.urlretrieve(URL + note_url, file_name)
                print("Successfully downloaded: " + note_url + " and saved as: " + file_name)
            for url in url_links:
                pdf.write(5, url['href'] + '\n')
                print('Wrote ' + url['href'] + " to the PDF file")
    pdf.output('c01_urls.pdf')
if __name__ == "__main__":
    main()