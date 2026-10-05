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
def fonk2():
    b1 = PerfumesDBHelper("perfumes.sqlite")
    b1.setup()
    with open("perfumes_manifest.txt", "r") as f:
        b2 = f.readlines()
    b3 = len(b2)
    b4 = b1.number_of_records()
    for index in range(b4, b3):
        try:
            b5 = b2[index][:-1]
            b6 = requests.get(b5)
            b7 = html.fromstring(b6.content)
            b8 = b5[35:-6].split("/")
            b9 = b8[0].replace("-", " ")
            b10 = " ".join(b8[1].split("-")[:-1])
            b11 = b7.xpath("
            if b11:
                b12 = b11.split("/")[-1]
                request.urlretrieve(b11, "fragrantica_images/perfumes/" + b12)
            else:
                b12 = None
            b13 = {"title": b10, "image": b12}
            b14 = b7.xpath("
            b15 = b14[-4:] if b14 and fonk1(b14[-4:]) else None
            b16 = b7.xpath("
            if b16:
                b16 = [accord for accord in b16 if accord not in ["main accords", "Videos", "Pictures"]]
            else:
                b16 = None
            b17 = b7.xpath("
            b18 = {}
            if "Fragrance Notes" in b17:
                b19 = b7.xpath("
                b18["general"] = [note_tag.get("title") for note_tag in b19]
            elif "Perfume Pyramid" in b17:
                b20 = ["Top Notes", "Middle Notes", "Base Notes"]
                for section in b20:
                    b19 = b7.xpath(f"
                    b18[section.lower()] = [note_tag.get("title") for note_tag in b19] if b19 else None
            else:
                b18 = None
            b21 = b7.xpath("
            b22 = b7.xpath("
            b23 = { "poor": b21[0], "weak": b21[1], "moderate": b21[2],
                          "long lasting": b21[3], "very long lasting": b21[4]} if b21 else None
            b24 = { "soft": b22[0], "moderate": b22[1], "heavy": b22[2],
                        "enormous": b22[3]} if b22 else None
            print({"count": f"{index}/{b3}", "b9": b9, "b13": b13})
            b1.add_record((b9, json.dumps(b13), b15, json.dumps(b16), json.dumps(b18),
                           json.dumps(b23), json.dumps(b24)))
        except error.HTTPError:
            continue
if b25 = = "__main__":
    fonk2()