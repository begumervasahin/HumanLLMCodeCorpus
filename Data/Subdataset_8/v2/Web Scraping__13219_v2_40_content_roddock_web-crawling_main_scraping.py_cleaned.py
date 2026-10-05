import requests
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        print("Error:", e)
        return None
def getBody(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.body
        return body
    except Exception as e:
        print("Error:", e)
        return None
def getText(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        textList = soup.find_all('p')
        return textList
    except Exception as e:
        print("Error:", e)
        return None
def getHead(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        head = soup.head
        return head
    except Exception as e:
        print("Error:", e)
        return None
def getLink(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        linkList = soup.find_all('a')
        return linkList
    except Exception as e:
        print("Error:", e)
        return None
def getImg(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        imgList = soup.find_all('img')
        return imgList
    except Exception as e:
        print("Error:", e)
        return None
url = "https:
title = getTitle(url)
if title == None:
    print("title not found")
else:
    print("***title below here***")
    print(title)
body = getBody(url)
if body == None:
    print("body not found")
else:
    print("***body below here***")
    print(body)
textList = getText(url)
if textList == None:
    print("text not found")
else:
    print("***text below here***")
    for text in textList:
        print(text.get_text())
head = getHead(url)
if head == None:
    print("head not found")
else:
    print("***head below here***")
    print(head)
linkList = getLink(url)
if linkList == None:
    print("url not found")
else:
    print("***link below here***")
    for link in linkList:
        if "href" in link.attrs:
            print(link.attrs["href"])
imgList = getImg(url)
if imgList == None:
    print("url not found")
else:
    print("***link image below here***")
    for img in imgList:
        if "src" in img.attrs:
            print(img.attrs["src"])