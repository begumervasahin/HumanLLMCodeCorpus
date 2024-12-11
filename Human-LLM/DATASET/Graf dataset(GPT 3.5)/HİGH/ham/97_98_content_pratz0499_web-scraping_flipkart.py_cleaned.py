from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
b1 = "https:
b2 = uReq(b1)
b3 = b2.read()
b2.close()
b4 = soup(b3, "html.parser")
b5 = b4.findAll("div", {"class": "_3O0U0u"})
b6 = b5[0]
b7 = b6.findAll("div",{"class":"col col-5-12 _2o7WAb"})
b8 = b6.findAll("div",{"class":"niH0FQ"})
b9 = "products.csv"
b10 = open(b9,"w")
b11 = "Product_name,Pricing,Ratings\n"
b10.write(b11)
for b6 in b5:
  b12 = b6.div.img["alt"]
  b13 = b6.findAll("div",{"class":"col col-5-12 _2o7WAb"})
  b7 = b13[0].text.strip()
  b14 = b6.findAll("div",{"class":"hGSR34"})
  b15 = b14[0].text
  b16 = "".join(b7.split(","))
  b17 = b16.split("â¹")
  b18 = "Rs."+b17[1]
  b19 = b18.split("E")
  b20 = b19[0]
  b21 = b15.split(" ")
  b22 = b21[0]
  print(b12.replace(",","|")+","+b20+","+b22+"\n")
  b10.write(b12.replace(",","|")+","+b20+","+b22+"\n")
b10.close()