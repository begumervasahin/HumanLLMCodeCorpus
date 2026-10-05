import json
from lxml import html
import requests
from urllib import request, error
from perfumes_db_helper import PerfumesDBHelper
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def extract_perfume_data(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    brand_and_perfume = url[35:-6].split("/")
    brand = brand_and_perfume[0].replace("-", " ")
    perfume_title = " ".join(brand_and_perfume[1].split("-")[:-1])
    perfume_image_url = tree.xpath("
    if perfume_image_url:
        perfume_image_file_name = perfume_image_url.split("/")[-1]
        request.urlretrieve(perfume_image_url, f"fragrantica_images/perfumes/{perfume_image_file_name}")
    else:
        perfume_image_file_name = None
    perfume = {"title": perfume_title, "image": perfume_image_file_name}
    page_title = tree.xpath("
    launch_year = page_title[-4:] if page_title and represents_int(page_title[-4:]) else None
    main_accords = tree.xpath("
    if main_accords:
        main_accords = [accord for accord in main_accords if accord not in ["main accords", "Videos", "Pictures"]]
    else:
        main_accords = None
    notes_captions = tree.xpath("
    notes = {}
    if "Fragrance Notes" in notes_captions:
        note_tags = tree.xpath("
        notes["general"] = [note_tag.get("title") for note_tag in note_tags]
    elif "Perfume Pyramid" in notes_captions:
        note_sections = ["Top Notes", "Middle Notes", "Base Notes"]
        for section in note_sections:
            note_tags = tree.xpath(f"
            notes[section.lower()] = [note_tag.get("title") for note_tag in note_tags] if note_tags else None
    else:
        notes = None
    longevity_votes = tree.xpath("
    sillage_votes = tree.xpath("
    longevity = { "poor": longevity_votes[0], "weak": longevity_votes[1], "moderate": longevity_votes[2],
                  "long lasting": longevity_votes[3], "very long lasting": longevity_votes[4]} if longevity_votes else None
    sillage = { "soft": sillage_votes[0], "moderate": sillage_votes[1], "heavy": sillage_votes[2],
                "enormous": sillage_votes[3]} if sillage_votes else None
    return brand, perfume, launch_year, main_accords, notes, longevity, sillage
def main():
    DB = PerfumesDBHelper("perfumes.sqlite")
    DB.setup()
    with open("perfumes_manifest.txt", "r") as f:
        perfume_urls = f.readlines()
    number_of_perfumes = len(perfume_urls)
    flag = DB.number_of_records()
    for index in range(flag, number_of_perfumes):
        try:
            url = perfume_urls[index].strip()
            brand, perfume, launch_year, main_accords, notes, longevity, sillage = extract_perfume_data(url)
            print({"count": f"{index}/{number_of_perfumes}", "brand": brand, "perfume": perfume})
            DB.add_record((brand, json.dumps(perfume), launch_year, json.dumps(main_accords), json.dumps(notes),
                           json.dumps(longevity), json.dumps(sillage)))
        except error.HTTPError:
            continue
if __name__ == "__main__":
    main()