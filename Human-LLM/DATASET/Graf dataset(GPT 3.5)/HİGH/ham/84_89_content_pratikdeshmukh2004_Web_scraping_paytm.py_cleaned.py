import requests,webbrowser,random
from bs4 import BeautifulSoup
b1 = requests.get("https:
b2 = BeautifulSoup(b1.text,"lxml")
print ("***********Welcome to %s*************"%b2.title.text)
b3 = b2.find("div",b15="_1_Nn")
b4 = b3.find_all("a")
a1 = 1
b5 = []
for a in b4:
    print (a1,a.text)
    b5.append(a["href"])
    a1+=1
b6 = input("which category you want(1,2,3) : ")
b7 = requests.get("https:
b8 = BeautifulSoup(b7.text,"lxml")
b9 = b8.find("div",b15="_3RA-")
b10 = b9.find_all("div",b15="_1fje")
a2 = 1
b11 = []
b12 = str(random.randint(31,37))
for div in b10:
    b13 = div.find_all("div",b15="_2i1r")
    for i in b13:
        print("\033[1;"+b12+";40m"+str(a2)+" "+i.find("a").get("title"))
        a2+=1
        b14 = i.find("a").find("span")
        print ("  Price : "+b14.text)
        print (" "+i.find("div",b15 = "_27VV").text)
        b11.append("https:
b6 = int(input("which want to you : "))
webbrowser.open_new_tab(b11[b6-1])