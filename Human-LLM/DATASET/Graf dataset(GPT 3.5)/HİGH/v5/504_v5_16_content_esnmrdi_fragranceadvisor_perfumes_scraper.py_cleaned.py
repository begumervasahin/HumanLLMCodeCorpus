import json
from lxml import html
import requests
from urllib import request, error
from perfumes_db_helper import PerfumesDBHelper
def fonk1(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def fonk2(b24):
    b1 = requests.get(b24)
    b2 = html.fromstring(b1.content)
    b3 = b24[35:-6].split("/")
    b4 = b3[0].replace("-", " ")
    b5 = " ".join(b3[1].split("-")[:-1])
    b6 = b2.xpath("
    if b6:
        b7 = b6.split("/")[-1]
        request.urlretrieve(b6, f"fragrantica_images/perfumes/{b7}")
    else:
        b7 = None
    b8 = {"title": b5, "image": b7}
    b9 = b2.xpath("
    b10 = b9[-4:] if b9 and fonk1(b9[-4:]) else None
    b11 = b2.xpath("
    if b11:
        b11 = [accord for accord in b11 if accord not in ["main accords", "Videos", "Pictures"]]
    else:
        b11 = None
    b12 = b2.xpath("
    b13 = {}
    if "Fragrance Notes" in b12:
        b14 = b2.xpath("
        b13["general"] = [note_tag.get("title") for note_tag in b14]
    elif "Perfume Pyramid" in b12:
        b15 = ["Top Notes", "Middle Notes", "Base Notes"]
        for section in b15:
            b14 = b2.xpath(f"
            b13[section.lower()] = [note_tag.get("title") for note_tag in b14] if b14 else None
    else:
        b13 = None
    b16 = b2.xpath("
    b17 = b2.xpath("
    b18 = { "poor": b16[0], "weak": b16[1], "moderate": b16[2],
                  "long lasting": b16[3], "very long lasting": b16[4]} if b16 else None
    b19 = { "soft": b17[0], "moderate": b17[1], "heavy": b17[2],
                "enormous": b17[3]} if b17 else None
    return b4, b8, b10, b11, b13, b18, b19
def fonk3():
    b20 = PerfumesDBHelper("perfumes.sqlite")
    b20.setup()
    with open("perfumes_manifest.txt", "r") as f:
        b21 = f.readlines()
    b22 = len(b21)
    b23 = b20.number_of_records()
    for index in range(b23, b22):
        try:
            b24 = b21[index].strip()
            b4, b8, b10, b11, b13, b18, b19 = fonk2(b24)
            print({"count": f"{index}/{b22}", "b4": b4, "b8": b8})
            b20.add_record((b4, json.dumps(b8), b10, json.dumps(b11), json.dumps(b13),
                           json.dumps(b18), json.dumps(b19)))
        except error.HTTPError:
            continue
if b25 = = "__main__":
    fonk3()