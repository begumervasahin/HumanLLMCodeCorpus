import os
import re
import string
b1 = re.compile("[a-zA-Z']+(?:-[a-zA-Z']+)?")
def fonk1(text):
    return list(b1.findall(text.lower()))
def fonk2(text,b8):
    b2 = list(b1.findall(text.lower()))
    b3 = []
    for word in b2:
        if(word not in b8) :
            b3.append(word)
    return(b3)
def fonk3(path):
    b4 = {}
    b5 = list(os.walk(path))[0][2]
    for file in b5:
        b6 = path+"/"+file
        with open(b6, b7 = 'utf-8',errors="ignore") as mailFile:
            b4[file]=fonk1(mailFile.read())
    return(b4)
def fonk4(path,b8):
    b4 = {}
    b5 = list(os.walk(path))[0][2]
    for file in b5:
        b6 = path+"/"+file
        with open(b6, b7 = 'utf-8',errors="ignore") as mailFile:
            b4[file]=fonk2(mailFile.read(),b8)
    return(b4)
def fonk5(path):
    with open(path, b7 = 'utf-8',errors="ignore") as stopFile:
        b8 = fonk1(stopFile.read())
        return(b8)
def fonk6(mailDict):
    b9 = []
    for key,value in mailDict.items():
        for i in value:
            b9.append(i)
    return(b9)