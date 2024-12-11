from lxml import html
import requests
import json
from perfumes_db_helper import PerfumesDBHelper
from urllib import request, error
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
            b10 = b8[1].split("-")
            b10 = " ".join(b10[:-1])
            b11 = b7.xpath("
            if b11:
                b12 = b11.split("/")[-1]
                request.urlretrieve(b11, "fragrantica_images/perfumes/" + b12)
            else:
                b12 = None
            b13 = {"title": b10, "image": b12}
            b14 = b7.xpath("
            if not b14:
                b15 = None
            else:
                b15 = b14[-4:]
                if not fonk1(b15):
                    b15 = None
            b16 = b7.xpath("
            if b16:
                if "main accords" in b16:
                    b16.remove("main accords")
                if "Videos" in b16:
                    b16.remove("Videos")
                if "Pictures" in b16:
                    b16.remove("Pictures")
            else:
                b16 = None
            b17 = b7.xpath("
            b18 = {}
            if "Fragrance Notes" in b17:
                b19 = b7.xpath("
                b18["general"] = [note_tag.get("title") for note_tag in b19]
            elif "Perfume Pyramid" in b17:
                b20 = b7.xpath("
                b21 = b7.xpath("
                b22 = b7.xpath("
                if b20:
                    b18["top"] = [top_note.get("title") for top_note in b20]
                else:
                    b18["top"] = None
                if b21:
                    b18["middle"] = [middle_note.get("title") for middle_note in b21]
                else:
                    b18["middle"] = None
                if b22:
                    b18["base"] = [base_note.get("title") for base_note in b22]
                else:
                    b18["base"] = None
            else:
                b18 = None
            b23 = b7.xpath("
            if b23:
                b24 = {"poor": b23[0], "weak": b23[1], "moderate": b23[2],
                             "long lasting": b23[3], "very long lasting": b23[4]}
            else:
                b24 = None
            b25 = b7.xpath("
            if b25:
                b26 = {"soft": b25[0], "moderate": b25[1], "heavy": b25[2],
                           "enormous": b25[3]}
            else:
                b26 = None
            print({"count": "{0}/{1}".format(index, b3), "b9": b9, "b13": b13})
            b1.add_record(tuple([b9, json.dumps(b13), b15, json.dumps(b16), json.dumps(b18),
                                json.dumps(b24), json.dumps(b26)]))
        except error.HTTPError:
            continue
if b27 = = "__main__":
    fonk2()