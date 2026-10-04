import os
import re
import glob
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
class Raipodcast:
    def __init__(self, url):
        self.url = url
    def download_file(self, url, filename):
        os.system(f'wget -O {filename} {url}')
    def clear_temp_directory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in glob.glob(f'{directory}/*'):
            os.remove(file)
    def sanitize_title(self, title):
        return re.sub(r'(?u)[^-\w.]', '', title.strip())
    def process(self, folder):
        self.clear_temp_directory('./tmp')
        print(f"Processing URL: {self.url}")
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Failed to retrieve the URL: {self.url}")
            return
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find('title').text
        sanitized_title = self.sanitize_title(title)
        print(f"Starting download for \"{title}\"")
        media_elements = soup.find_all(['li', 'div'])
        print("Downloading individual MP3s...")
        for element_id, element in enumerate(media_elements, start=1):
            if element.has_attr('data-mediapolis') and element.has_attr('data-title'):
                mp3_url = urljoin(self.url, element['data-mediapolis'])
                media_title = self.sanitize_title(element['data-title'])
                filename = f"tmp/{str(element_id).zfill(2)}_{sanitized_title}.mp3"
                print(f"Downloading \"{media_title}\" ({mp3_url})")
                self.download_file(mp3_url, filename)
        print("Download complete! Files are saved in ./tmp/. Move them to avoid deletion next time the script runs.")
def main():
    print()
    if len(sys.argv) < 2:
        print('A URL is required to proceed.')
        sys.exit(2)
    podcast_downloader = Raipodcast(sys.argv[1])
    podcast_downloader.process('.')
if __name__ == '__main__':
    main()