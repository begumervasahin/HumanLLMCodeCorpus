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
            b11 = b9[1].split("-")
            b11 = " ".join(b11[:-1])
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
                if "main accords" in b17:
                    b17.remove("main accords")
                if "Videos" in b17:
                    b17.remove("Videos")
                if "Pictures" in b17:
                    b17.remove("Pictures")
            else:
                b17 = None
            b18 = b8.xpath("
            b19 = {}
            if "Fragrance Notes" in b18:
                b20 = b8.xpath("
                b19["general"] = [note_tag.get("title") for note_tag in b20]
            elif "Perfume Pyramid" in b18:
                b21 = b8.xpath("
                b22 = b8.xpath("
                b23 = b8.xpath("
                b19["top"] = [top_note.get("title") for top_note in b21] if b21 else None
                b19["middle"] = [middle_note.get("title") for middle_note in b22] if b22 else None
                b19["base"] = [base_note.get("title") for base_note in b23] if b23 else None
            else:
                b19 = None
            b24 = b8.xpath("
            b25 = {"poor": b24[0], "weak": b24[1], "moderate": b24[2],
                         "long lasting": b24[3], "very long lasting": b24[4]} if b24 else None
            b26 = b8.xpath("
            b27 = {"soft": b26[0], "moderate": b26[1], "heavy": b26[2],
                       "enormous": b26[3]} if b26 else None
            print({"count": "{0}/{1}".format(index, b4), "b10": b10, "b14": b14})
            b2.fonk4((b10, json.dumps(b14), b16, json.dumps(b17), json.dumps(b19),
                           json.dumps(b25), json.dumps(b27)))
        except error.HTTPError:
            continue
if b28 = = "__main__":
    fonk6()