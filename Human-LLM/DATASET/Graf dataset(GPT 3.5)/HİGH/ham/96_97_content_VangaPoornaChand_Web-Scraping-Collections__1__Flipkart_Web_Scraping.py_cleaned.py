from bs4 import BeautifulSoup
import requests
import csv
import os
b1 = input("Enter b1 you want to b3 : ")
b2 = int(input("Enter number of b2: "))
b3 = "/b3?q="+b1+"&otracker=b3&otracker1=b3&marketplace=FLIPKART&as-show=off&as=off"
b4 = f"Flipkart Scraping on {b1}.csv"
if os.path.exists(b4):
	print("You have already searched for this...\nDeleting your previous results...")
	os.system(f"rm '{b4}'")
for i in range(b2):
	try:
		b5 = open(b4,"w")
		b6 = csv.writer(b5)
		b6.writerow(["TITLE","Price","Rating"])
		b7 = "https:
		b8 = requests.get(b7)
		print("Working on Page No :",i+1)
		b9 = BeautifulSoup(b8.text,'lxml')
		for mobile_area in b9.find_all(b10 = "_1UoZlX"):
			b11 = mobile_area.find(b10 = '_3wU53n')
			b12 = mobile_area.find(b10 = "_1vC4OE _2rQ-NK")
			b13 = mobile_area.find(b10 = "hGSR34")
			b13 = "No Rating" if b13 == None else b13.text
			b6.writerow([b11.text,b12.text[1:],b13])
		b3 = b9.find_all(b10 = "_3fVaIS")[-1]
		b3 = b3["href"]
	except IndexError:
		print("Out Of Pages for your b3!!!")
		break
	except:
		print("One Item Skiped Due to internal error")
b5.close()