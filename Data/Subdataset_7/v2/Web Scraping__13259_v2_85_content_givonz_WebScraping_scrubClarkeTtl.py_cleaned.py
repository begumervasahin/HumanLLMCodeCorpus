from bs4 import BeautifulSoup
from urllib.request import urlopen
def fonk1(b26, file_names, file_common_names, file_symptoms):
    b1 = urlopen(b26).read()
    b2 = BeautifulSoup(b1, "html.parser")
    b3 = b2.find_all("a")
    b4 = len(b3) - 1
    for b6, link in enumerate(b3):
        if len(link.get("href")) == 5:
            continue
        if link.get("href")[-9:] == "index.htm":
            b5 = str(b3[b6])
            if ">H.I.<" in b5:
                return
            continue
        if b6 = = b4:
            return
        b7 = "http:
        b8 = urlopen(b7).read()
        b9 = BeautifulSoup(b8, "html.parser")
        b10 = b9.find_all("p")
        b11 = str(b10[2])
        b12 = fonk2(b11)
        print(b12)
        file_names.write(b12 + "\n")
        b13 = str(b10[3])
        b14 = fonk2(b13)
        b14 = fonk3(b14)
        file_common_names.write(b14 + "\n")
        b15 = fonk4(b9)
        file_symptoms.write(b15 + "\n")
        break
def fonk2(tag_text):
    b16 = b18 = 0
    a1 = 0
    for pos, b17 in enumerate(tag_text):
        if b17 = = ">":
            b16 = pos + 1
        elif b17 = = "<":
            a1 += 1
            if a1 = = 2:
                b18 = pos
                break
    return tag_text[b16:b18]
def fonk3(b13):
    b13 = b13[1:].replace("(", "").replace(")", "")
    return b13
def fonk4(b2):
    b19 = str(b2)
    b20 = False
    b21 = b22 = 0
    for pos, b17 in enumerate(b19):
        if b19[pos:pos + 8] == "Clinical":
            b20 = True
        if b20 and b19[pos:pos + 4] == "</b>":
            b21 = pos + 4
        if b21 > 0 and b19[pos:pos + 13] == "</blockquote>":
            b22 = pos
            break
    b23 = b19[b21:b22]
    b24 = fonk5(b23)
    return b24
def fonk5(b25):
    b25 = b25.replace("<i>", " 2").replace('<font color="', "").replace("</font>", "")
    b25 = b25.replace("</i>", "").replace("\n", "").replace("        ", " ")
    return b25
def fonk6():
    with open("h-remedies.csv", "w") as file_names, \
         open("commonRemedyNames.csv", "w") as file_common_names, \
         open("remedy-symptoms.csv", "w") as file_symptoms:
        for char_code in range(97, 123):
            b26 = "http:
            fonk1(b26, file_names, file_common_names, file_symptoms)
if b27 = = "__main__":
    fonk6()