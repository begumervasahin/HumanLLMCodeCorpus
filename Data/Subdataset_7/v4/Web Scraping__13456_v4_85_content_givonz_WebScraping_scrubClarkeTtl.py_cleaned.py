import requests
from bs4 import BeautifulSoup
def fonk1(b23, b20, b21, b22):
    b1 = requests.get(b23)
    b2 = BeautifulSoup(b1.text, "html.parser")
    b3 = b2.find_all("a")
    b4 = len(b3) - 1
    for index, link in enumerate(b3):
        b5 = link.get("b5")
        if len(b5) == 5:
            continue
        if b5.endswith("index.htm"):
            b6 = str(b3[index])
            if ">H.I.<" in b6:
                return
            continue
        b7 = "http:
        b8 = requests.get(b7)
        b9 = BeautifulSoup(b8.text, "html.parser")
        b10 = b9.find_all("p")
        b11 = b10[2].get_text()
        b20.write(b11 + "\n")
        b12 = b10[3].get_text().replace("        ", "")
        b12 = b12.replace("(", "").replace(")", "")
        b12 = b12[1:].strip()
        b13 = fonk3(b12)
        b21.write(b13 + "\n")
        b14 = fonk2(b9)
        b22.write(b14 + "\n")
        break
def fonk2(b2):
    b15 = str(b2)
    a1 = 0
    a2 = 0
    a3 = 0
    for index, b19 in enumerate(b15):
        if b15[index:index+8] == "Clinical":
            a1 = 1
        if a1 = = 1 and b15[index:index+4] == "</b>":
            a2 = index + 4
        if a2 > 0 and b15[index:index+13] == "</blockquote>":
            a3 = index
            break
    b16 = b15[a2:a3]
    b16 = b16.replace("<i>", "").replace("</i>", "")
    b16 = b16.replace("<font color=", "")
    b16 = b16.replace("</font>", "").replace("\n", "")
    b16 = b16.replace("        ", "")
    b17 = fonk3(b16)
    return b17
def fonk3(b17):
    b18 = '"'
    a4 = 0
    for index, b19 in enumerate(b17):
        if b19 = = '.':
            if b17[index-1:index] == 'N' or b17[index-1:index] == 'O':
                continue
            b18 += b17[a4:index] + '","'
            a5 = 1
            while b17[index + a5:index + a5 + 1] == ' ':
                a5 += 1
            a4 = index + a5
    b18 = b18[:-2]
    for index, b19 in enumerate(b18):
        if b19 = = '"' and ('A' <= b18[index+1:index+2] <= 'Z'):
            b18 = b18[:index+1] + '1' + b18[index+1:]
    for index, b19 in enumerate(b18):
        if b19 = = '"':
            if b18[index+1:index+2] == "1":
                b18 = b18[:index+2] + '","' + b18[index+2:]
            if b18[index+1:index+2] == "2":
                b18 = b18[:index+2] + '","' + b18[index+2:]
    return b18
def fonk4():
    b20 = open("h-remedies", "w")
    b21 = open("commonRemedyNames", "w")
    b22 = open("remedy-symptoms", "w")
    for x in range(26):
        b23 = "http:
        fonk1(b23, b20, b21, b22)
    b20.close()
    b21.close()
    b22.close()
fonk4()