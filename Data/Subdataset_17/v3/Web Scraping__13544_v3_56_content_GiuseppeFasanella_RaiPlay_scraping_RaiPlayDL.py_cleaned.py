import os
import re
import glob
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
class Raipodcast:
    def __init__(self, url):
        self.url = url
    def download_file(self, url, filename):
        response = requests.get(url, stream=True)
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
    def clear_tmp_directory(self, tmp_dir):
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        for file in glob.glob(os.path.join(tmp_dir, '*')):
            os.remove(file)
    def get_sanitized_filename(self, text):
        return re.sub(r'(?u)[^-\w.]', '', text.strip().replace(' ', '_'))
    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("Failed to retrieve the podcast page.")
            return None
        return response.content
    def process_podcast(self, folder):
        tmp_dir = './tmp'
        self.clear_tmp_directory(tmp_dir)
        print(f"Fetching podcast from: {self.url}")
        page_content = self.fetch_page()
        if page_content is None:
            return
        soup = BeautifulSoup(page_content, "html.parser")
        title = soup.find('title').text.strip()
        sanitized_title = self.get_sanitized_filename(title)
        print(f"Starting download for \"{title}\"")
        elements = soup.find_all(['li', 'div'])
        print("Downloading individual MP3s...")
        for index, element in enumerate(elements, start=1):
            if element.has_attr('data-mediapolis') and element.has_attr('data-title'):
                mp3_url = urljoin(self.url, element['data-mediapolis'])
                track_title = self.get_sanitized_filename(element['data-title'])
                filename = os.path.join(tmp_dir, f"{str(index).zfill(2)}_{sanitized_title}.mp3")
                print(f"Downloading \"{track_title}\" from {mp3_url}")
                self.download_file(mp3_url, filename)
        print("Download complete! Files are saved in ./tmp/. Move them or they will be overwritten next time.")
def main():
    banner =
    print(banner)
    if len(sys.argv) < 2:
        print('Please provide a URL to download the podcast.')
        exit(2)
    podcast_url = sys.argv[1]
    podcast_downloader = Raipodcast(podcast_url)
    podcast_downloader.process_podcast('.')
if __name__ == '__main__':
    main()