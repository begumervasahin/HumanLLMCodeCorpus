import urllib.request
from bs4 import BeautifulSoup
import ssl
from wordcloud import WordCloud
import threading
from time import time
ListaAgricultura = []
ListaIndustria = []
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
BASE_URL = 'https:
COUNTRY_URL_BASE = 'https:
def fetch_data(country_codes, start_index, end_index, data_list):
    for i in range(start_index, end_index):
        try:
            country_html = country_codes[i] + '.html'
            url_to_get = COUNTRY_URL_BASE + country_html
            html = urllib.request.urlopen(url_to_get, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            txt = soup.get_text()
            agriculture_pos = txt.find('Agriculture - products:')
            if agriculture_pos != -1:
                for tag in soup.find_all('div', id="field-agriculture-products"):
                    for pro in tag:
                        data_list.append(pro)
            for tag in soup.find_all('div', id="field-industries"):
                for ind in tag:
                    data_list.append(ind)
        except Exception as e:
            print("Error:", e)
def generate_wordcloud(data_list, filename):
    data_str = " ".join(data_list)
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate(data_str)
    wordcloud.to_file(filename)
def main():
    print("Opening the file connection...")
    uh = urllib.request.urlopen(BASE_URL, context=ctx)
    print("HTTP status", uh.getcode())
    html = uh.read().decode()
    print(f"Reading done. Total {len(html)} characters read.")
    soup = BeautifulSoup(html, 'html.parser')
    country_codes = [tag.get('value')[5:7] for tag in soup.find_all('option')]
    country_names = [tag.text for tag in soup.find_all('option')]
    country_codes.pop(0)
    country_names.pop(0)
    midpoint = len(country_names)
    t1 = threading.Thread(target=fetch_data, args=(country_codes, 1, midpoint, ListaAgricultura))
    t2 = threading.Thread(target=fetch_data, args=(country_codes, midpoint, len(country_names)-1, ListaIndustria))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    generate_wordcloud(ListaAgricultura, 'primerparaleloagricola.png')
    generate_wordcloud(ListaIndustria, 'primerparaleloindustrial.png')
if __name__ == "__main__":
    main()