import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
BASE_URL = 'https:
music = ''
def get_links(band):
    try:
        print('Obtaining links/songs')
        ctrl_page = set()
        html = urlopen(f"{BASE_URL}/{band}")
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('ul', {'class': 'cnt-list'}).find_all('a'):
            href = link.get('href')
            if href and href not in ctrl_page:
                ctrl_page.add(href)
                get_music(href)
    except Exception as e:
        print(f'An error occurred while trying to access the site. {e}')
def get_music(new_page):
    global music
    try:
        html = urlopen(f"{BASE_URL}/{new_page}")
        bs = BeautifulSoup(html, 'html.parser')
        for verse in bs.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            music += ' '.join(verse.stripped_strings) + ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site. {e}')
def clean_write(preview=100):
    print('Finalizing...')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    plain_text = ''
    for word in music.split():
        if len(word) >= 3:
            cleaned_word = ''.join(char for char in word if char not in string.punctuation)
            if cleaned_word.lower() not in stopwords:
                plain_text += cleaned_word.lower() + ' '
    try:
        with open('filename.txt', 'w') as f:
            f.write(plain_text)
    except Exception as e:
        print(f'An error occurred while trying to save the file. {e}')
    return plain_text[:preview]
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <band_name> [preview_length]")
    else:
        band_name = sys.argv[1]
        preview_length = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        get_links(band_name)
        print(clean_write(preview_length))