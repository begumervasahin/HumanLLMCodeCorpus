import requests
from bs4 import BeautifulSoup
def fonk1(b17, file_names, file_common_names, file_symptoms):
    b1 = requests.get(b17)
    b2 = BeautifulSoup(b1.text, "html.parser")
    b3 = b2.find_all("a")
    for link in b3:
        b4 = link.get("b4")
        if len(b4) == 5:
            continue
        if b4.endswith("index.htm"):
            b5 = str(link)
            if ">H.I.<" in b5:
                return
            continue
        b6 = "http:
        b7 = requests.get(b6)
        b8 = BeautifulSoup(b7.text, "html.parser")
        b9 = b8.find_all("p")[2].get_text()
        file_names.write(b9 + "\n")
        b10 = b8.find_all("p")[3].get_text().replace("        ", "").replace("(", "").replace(")", "").strip()
        b11 = fonk3(b10)
        file_common_names.write(b11 + "\n")
        b12 = fonk2(b8)
        file_symptoms.write(b12 + "\n")
        break
def fonk2(b2):
    b13 = str(b2)
    a1 = 0
    a2 = 0
    a3 = 0
    for index, b16 in enumerate(b13):
        if b13[index:index+8] == "Clinical":
            a1 = 1
        if a1 = = 1 and b13[index:index+4] == "</b>":
            a2 = index + 4
        if a2 > 0 and b13[index:index+13] == "</blockquote>":
            a3 = index
            break
    b14 = b13[a2:a3]
    b14 = b14.replace("<i>", "").replace("</i>", "")
    b14 = b14.replace("<font color=", "").replace("</font>", "").replace("\n", "").replace("        ", "")
    return fonk3(b14)
def fonk3(out_rec):
    b15 = '"'
    a4 = 0
    for index, b16 in enumerate(out_rec):
        if b16 = = '.':
            if out_rec[index-1:index] == 'N' or out_rec[index-1:index] == 'O':
                continue
            b15 += out_rec[a4:index] + '","'
            a5 = 1
            while out_rec[index + a5:index + a5 + 1] == ' ':
                a5 += 1
            a4 = index + a5
    b15 = b15[:-2]
    for index, b16 in enumerate(b15):
        if b16 = = '"' and ('A' <= b15[index+1:index+2] <= 'Z'):
            b15 = b15[:index+1] + '1' + b15[index+1:]
    for index, b16 in enumerate(b15):
        if b16 = = '"':
            if b15[index+1:index+2] == "1":
                b15 = b15[:index+2] + '","' + b15[index+2:]
            if b15[index+1:index+2] == "2":
                b15 = b15[:index+2] + '","' + b15[index+2:]
    return b15
def fonk4():
    with open("h-remedies", "w") as file_names, open("commonRemedyNames", "w") as file_common_names, open("remedy-symptoms", "w") as file_symptoms:
        for x in range(26):
            b17 = f"http:
            fonk1(b17, file_names, file_common_names, file_symptoms)
fonk4()