import requests,webbrowser,random
from bs4 import BeautifulSoup
url=requests.get("https:
soup=BeautifulSoup(url.text,"lxml")
print ("***********Welcome to %s*************"%soup.title.text)
main_div=soup.find("div",class_="_1_Nn")
all_a=main_div.find_all("a")
num=1
url_list=[]
for a in all_a:
    print (num,a.text)
    url_list.append(a["href"])
    num+=1
user=input("which category you want(1,2,3) : ")
url2=requests.get("https:
soup2=BeautifulSoup(url2.text,"lxml")
mainDiv=soup2.find("div",class_="_3RA-")
divs=mainDiv.find_all("div",class_="_1fje")
count=1
h_list=[]
color=str(random.randint(31,37))
for div in divs:
    DIV=div.find_all("div",class_="_2i1r")
    for i in DIV:
        print("\033[1;"+color+";40m"+str(count)+" "+i.find("a").get("title"))
        count+=1
        price=i.find("a").find("span")
        print ("  Price : "+price.text)
        print (" "+i.find("div",class_="_27VV").text)
        h_list.append("https:
user=int(input("which want to you : "))
webbrowser.open_new_tab(h_list[user-1])