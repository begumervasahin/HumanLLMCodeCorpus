import os
import urllib.request
from fpdf import FPDF
import requests
from bs4 import BeautifulSoup
LECTURE_URL = r'https:
response = requests.get(LECTURE_URL)
html_content = response.text
pdf = FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
soup = BeautifulSoup(html_content, 'html.parser')
def download_lecture_pdfs(lecture_notes_sections):
    '''
    Download lecture PDFs and save them to the current directory.
    '''
    for section in lecture_notes_sections:
        for link in section.find_all('a'):
            lecture_url = link['href']
            file_name = lecture_url.split('/')[-1]
            urllib.request.urlretrieve(LECTURE_URL + lecture_url, file_name)
            print("Downloaded:", lecture_url, "and saved as:", file_name)
def write_reading_links_to_pdf(reading_links_sections):
    '''
    Write reading links to the PDF document.
    '''
    for section in reading_links_sections:
        for link in section.find_all('a'):
            pdf.cell(200, 10, txt=link['href'], ln=True)
            print("Added", link['href'], "to the PDF file")
def main():
    '''
    Scrapes lecture PDFs and reading links from the webpage,
    downloads PDFs to the current directory, and writes reading links to a PDF file.
    '''
    lecture_notes_sections = soup.find_all('div', class_='notes')
    reading_links_sections = soup.find_all('div', class_='readings')
    download_lecture_pdfs(lecture_notes_sections)
    write_reading_links_to_pdf(reading_links_sections)
    pdf.output('c09_urls.pdf')
if __name__ == "__main__":
    main()