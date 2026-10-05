from lxml import html
import requests
import json
import os
from urllib import request, error
class PerfumesDBHelper:
    def __init__(self, db_name):
        self.db_name = db_name
    def setup(self):
        pass
    def number_of_records(self):
        pass
    def add_record(self, record):
        pass
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def download_image(image_url, folder="fragrantica_images/perfumes"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = image_url.split("/")[-1]
    path = os.path.join(folder, filename)
    request.urlretrieve(image_url, path)
    return filename
def parse_perfume_page(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    brand, *perfume_title_parts = url[35:-6].replace("-", " ").split("/")
    perfume_title = " ".join(perfume_title_parts[:-1])
    perfume_image_url = tree.xpath("
    perfume_image_file_name = download_image(perfume_image_url[0]) if perfume_image_url else None
    page_title = tree.xpath("
    launch_year = page_title[0][-4:] if page_title and represents_int(page_title[0][-4:]) else None
    main_accords = [accord for accord in tree.xpath("
    notes = {}
    note_tags = tree.xpath("
    notes["general"] = [note_tag.get("title") for note_tag in note_tags] if note_tags else {}
    longevity_votes = tree.xpath("
    sillage_votes = tree.xpath("
    longevity = {key: value for key, value in zip(["poor", "weak", "moderate", "long lasting", "very long lasting"], longevity_votes)} if longevity_votes else {}
    sillage = {key: value for key, value in zip(["soft", "moderate", "heavy", "enormous"], sillage_votes)} if sillage_votes else {}
    return {
        "brand": brand,
        "title": perfume_title,
        "image": perfume_image_file_name,
        "launch_year": launch_year,
        "main_accords": main_accords,
        "notes": notes,
        "longevity": longevity,
        "sillage": sillage
    }
def main():
    DB = PerfumesDBHelper("perfumes.sqlite")
    DB.setup()
    with open("perfumes_manifest.txt", "r") as f:
        perfume_urls = [url.strip() for url in f]
    current_count = DB.number_of_records()
    for index, url in enumerate(perfume_urls[current_count:], start=current_count):
        try:
            perfume_info = parse_perfume_page(url)
            print(f"Processing {index + 1}/{len(perfume_urls)}: {perfume_info['brand']} - {perfume_info['title']}")
            DB.add_record(perfume_info)
        except error.HTTPError:
            print(f"Failed to process {url}")
            continue
if __name__ == "__main__":
    main()