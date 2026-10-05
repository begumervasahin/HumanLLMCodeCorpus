from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
b1 = ['https:
          'https:
          'https:
          'https:
          'https:
          'https:
          'https:
          'https:
          'https:
          'https:
b2 = "croma.csv"
b3 = open(b2,"w",encoding='utf-8')
b4 = "number,model,b30,offer_price,b21,price_difference\n"
b3.write(b4)
b5 = "past_data_croma.csv"
b6 = open(b5,"a",encoding='utf-8')
a1 = 1
a2 = 0
for y in b1 :
    b7 = uReq(y)
    b8 = b7.read()
    b7.close()
    b9 = soup(b8,'lxml')
    b10 = b9.find_all('li',{'class' :'product__list--item'})
    a2 +=1
    for x in b10:
        if a1 = = 181:
            break
        print(a1)
        b11 = x.find('div',b22 = 'row')
        b12 = b11.find('div',b22 = 'row')
        b13 = b12.find('a',b22 = 'product__list--name')
        b14 = b13.text
        b14 = b14.replace(",","")
        b14 = b14.lower()
        if((b14[0] == 'x') and (b14[1] == 'i') and (b14[2] == 'a') and (b14[3] == 'o') and (b14[4] == 'm') and (b14[5] == 'i')):
            b14 = b14.replace('xiaomi','redmi')
            print("\nTitle          : ", b14)
        else:
            print("\nTitle          : ", b14)
        b15 = b12.find('div',b22 = 'col-md-4 col-xs-8')
        b16 = b15.find('div',b22='_priceRow')
        b17 = b16.find('span',b22='pdpPrice')
        b18 = b17.text
        b19 = b18.replace("â¹","")
        b19 = b19.replace(",","")
        print("\nFinal Price    : ", b19)
        try:
            b20 = b16.find('span',b22 = 'pdpPriceMrp')
            b21 = b20.text
            b21 = b21.replace("â¹","")
            b21 = b21.replace(",","")
            print("\nOriginal Price : ",b21)
        except:
            b21 = b19
            print("\nOriginal Price : ",b21)
        for tag in b11.find_next_siblings('div',b22 = 'row'):
            try:
                b23 = tag.find('div',b22 = 'col-xs-12 col-sm-4 col-md-3')
                b24 = b23.find('div',b22 = 'b30')
                b25 = b24.find('div',b22 = 'b30-stars pull-left js-ratingCalc ')
                b26 = b25.find('div',b22 = 'greenStars js-greenStars')
                b27 = b26.find('span',b22 = 'glyphicon glyphicon-b29 active')
                b28 = b27.find_next_siblings('span',b22 = 'glyphicon glyphicon-b29 active')
                b29 = len(b28)
                print("\nRating         : ",b29)
                b30 = str(b29)
            except:
                print("\nRating         :  NO RATING")
                b30 = '0'
        b31 = float(b21) - float(b19)
        b31 = str(b31)
        print("\nPrice Difference: ", b31)
        b32 = str(a1)
        a1 += 1
        print("----------------------------------------------")
        b3.write(b32 + "," + b14 + "," + b30 + "," + b19 + "," + b21 + "," + b31 +  "\n")
print("\nProducts :", a1)
print("\nPages    :", a2)
b33 = csv.reader(open('D:\\6th Semester\\Project\\27-2\croma\\croma.csv', 'r'))
b34 = []
for row in b33:
   if row is not None:
     b34.append(row)
b34.pop(0)
b35 = []
for i in range(len(b34)):
   b35.append(float(b34[i][5]))
print ('Mean price of croma : ', (np.mean(b35)))
b36 = datetime.datetime.b36()
b37 = b36.strftime("%Y-%m-%d")
print ("\ndate          : ", b37)
b6.write(b37 + "," + str(np.mean(b35)) +  "\n")
b3.close()
b6.close()