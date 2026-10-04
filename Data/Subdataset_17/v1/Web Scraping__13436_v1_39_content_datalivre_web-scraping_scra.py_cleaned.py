import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
url = 'https:
music = ''
def get_links(band):
    '''
    Captures all links of a band, group, or artist from
    the page https:
    args
    ----
        * band: band, group, or artist whose links will be captured.
    '''
    try:
        print('Obtaining links/songs')
        ctrl_page = set()
        html = urlopen(f"{url}/{band}")
        bs = BeautifulSoup(html, 'html.parser')
        for link in bs.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                if link.attrs['href'] not in ctrl_page:
                    ctrl_page.add(f"{link.attrs['href']}")
                    get_music(link.attrs['href'])
    except Exception as e:
        print(f'An error occurred while trying to access the site. {e}')
def get_music(new_page):
    '''
    Captures all songs of a band, group, or artist from
    the page www.letras.mus.br/[band/song_name].
    args
    ----
        * new_page: receives the links captured by the get_links() function.
    '''
    global music
    try:
        html = urlopen(f"{url}/{new_page}")
        bs = BeautifulSoup(html, 'html.parser')
        for verse in bs.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            music += ' '.join(verse.stripped_strings)
            music += ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site. {e}')
def clean_write(preview=100):
    '''
    Adds to the variable plain_text all words longer than X letters
    and that are not in the stopwords list. Then, saves the entire result in a
    text file.
    args
    ----
        * preview: total number of characters to be displayed as "preview"
        after cleaning and saving the data. By default, 100 characters
        are displayed.
    '''
    print('Finalizing...')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    plain_text = ''
    for m in music.split():
        if len(m) >= 3:
            m = ''.join(p for p in m if p not in string.punctuation)
            if m.lower() not in stopwords:
                plain_text += m.lower() + ' '
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