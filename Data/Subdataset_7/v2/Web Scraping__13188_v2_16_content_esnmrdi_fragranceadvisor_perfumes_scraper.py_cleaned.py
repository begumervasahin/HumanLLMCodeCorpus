from lxml import html
import requests
import json
import os
from urllib import request, error
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        pass
    def fonk3(self):
        pass
    def fonk4(self, record):
        pass
def fonk5(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def fonk6():
    b2 = class1("perfumes.sqlite")
    b2.fonk2()
    with open("perfumes_manifest.txt", "r") as f:
        b3 = f.readlines()
    b4 = len(b3)
    b5 = b2.fonk3()
    for index in range(b5, b4):
        try:
            b6 = b3[index][:-1]
            b7 = requests.get(b6)
            b8 = html.fromstring(b7.content)
            b9 = b6[35:-6].split("/")
            b10 = b9[0].replace("-", " ")
            b11 = " ".join(b9[1].split("-")[:-1])
            b12 = b8.xpath("
            if b12:
                b13 = b12.split("/")[-1]
                if not os.path.exists("fragrantica_images/perfumes"):
                    os.makedirs("fragrantica_images/perfumes")
                request.urlretrieve(b12, "fragrantica_images/perfumes/" + b13)
            else:
                b13 = None
            b14 = {"title": b11, "image": b13}
            b15 = b8.xpath("
            b16 = b15[-4:] if b15 and fonk5(b15[-4:]) else None
            b17 = b8.xpath("
            if b17:
                b17 = [accord for accord in b17 if accord not in ["main accords", "Videos", "Pictures"]]
            else:
                b17 = None
            b18 = b8.xpath("
            b19 = {}
            if "Fragrance Notes" in b18:
                b20 = b8.xpath("
                b19["general"] = [note_tag.get("title") for note_tag in b20]
            elif "Perfume Pyramid" in b18:
                b21 = ["Top Notes", "Middle Notes", "Base Notes"]
                for category in b21:
                    b20 = b8.xpath(f"
                    b19[category.lower().replace(" ", "_")] = [note.get("title") for note in b20] if b20 else None
            else:
                b19 = None
            b22 = b8.xpath("
            b23 = {"poor": b22[0], "weak": b22[1], "moderate": b22[2],
                         "long lasting": b22[3], "very long lasting": b22[4]} if b22 else None
            b24 = b8.xpath("
            b25 = {"soft": b24[0], "moderate": b24[1], "heavy": b24[2],
                       "enormous": b24[3]} if b24 else None
            print({"count": f"{index}/{b4}", "b10": b10, "b14": b14})
            b2.fonk4((b10, json.dumps(b14), b16, json.dumps(b17), json.dumps(b19),
                           json.dumps(b23), json.dumps(b25)))
        except error.HTTPError:
            continue
if b26 = = "__main__":
    fonk6()