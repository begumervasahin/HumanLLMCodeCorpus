import os
import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
URL = r'https:
response = requests.get(URL)
source_code = response.text
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
soup = BeautifulSoup(source_code, 'html.parser')
def main():
    '''
    Scrapes lecture PDFs and reading links from the webpage,
    downloads PDFs to the current directory, and writes reading links to a PDF file.
    '''
    lecture_notes_sections = soup.find_all('div', class_='notes')
    reading_links_sections = soup.find_all('div', class_='readings')
    for i in range(len(lecture_notes_sections)):
        try:
            lecture_files = lecture_notes_sections[i].find_all('a')
            reading_urls = reading_links_sections[i].find_all('a')
        except Exception as e:
            print("Error:", e)
            continue
        else:
            for lecture_file in lecture_files:
                lecture_url = lecture_file['href']
                file_name = lecture_url.split('/')[-1]
                urllib.request.urlretrieve(URL + lecture_url, file_name)
                print("Downloaded: " + lecture_url + " and saved as: " + file_name)
            for reading_url in reading_urls:
                pdf.cell(200, 10, txt=reading_url['href'], ln=True)
                print('Added ' + reading_url['href'] + " to the PDF file")
    pdf.output('c09_urls.pdf')
if __name__ == "__main__":
    main()