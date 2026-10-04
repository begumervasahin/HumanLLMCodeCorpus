import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
BASE_URL = 'https:
lyrics = ''
def fetch_band_links(band):
    try:
        print('Obtaining links/songs...')
        unique_links = set()
        html = urlopen(f"{BASE_URL}/{band}")
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                href = link.attrs['href']
                if href not in unique_links:
                    unique_links.add(href)
                    fetch_lyrics(href)
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fetch_lyrics(page_url):
    global lyrics
    try:
        html = urlopen(f"{BASE_URL}/{page_url}")
        soup = BeautifulSoup(html, 'html.parser')
        for verse in soup.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            lyrics += ' '.join(verse.stripped_strings) + ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def clean_and_write_lyrics(preview_length=100):
    print('Finalizing...')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    cleaned_text = ''
    for word in lyrics.split():
        cleaned_word = ''.join(char for char in word if char not in string.punctuation)
        if len(cleaned_word) >= 3 and cleaned_word.lower() not in stopwords:
            cleaned_text += cleaned_word.lower() + ' '
    try:
        with open('lyrics.txt', 'w') as file:
            file.write(cleaned_text)
    except Exception as e:
        print(f'An error occurred while trying to write the file: {e}')
    return cleaned_text[:preview_length]
if __name__ == "__main__":
    if len(sys.argv) > 1:
        band_name = sys.argv[1]
        fetch_band_links(band_name)
        preview_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        print(clean_and_write_lyrics(preview_chars))
    else:
        print("Please provide the band name as an argument.")