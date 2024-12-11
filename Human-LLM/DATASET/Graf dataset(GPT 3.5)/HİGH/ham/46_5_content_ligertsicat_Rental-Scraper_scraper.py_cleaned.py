import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json
b1 = open("rentpad_list.csv", "w+")
def fonk1(city):
	b2 = {
            "a":"31",
            "cityName":"Mandaluyong",
            "propertyTypeIDs":[2,3,5],
            "furnishTypeIDs":[1,2,3],
            "placeIDs":[],
            "statusTypeIDs":[],
            "amenityIDs":[],
            "longMonthRateLow":"0",
            "longMonthRateHigh":"30,000",
            "numBedroomsLow":"0",
			"numBedroomsHigh":"0",
			"itemsPerPage":"1000",
			"pageNumber":"1",
			"lengthOfStay":"",
			"ham":"ham"
	}
	b3 = requests.post(
			b4 = "https:
			b5 = b2,
		)
	b6 = BeautifulSoup(b3.text, 'b6.parser')
	b7 = b6.find_all(itemprop="b11")
	b8 = b6.find_all(itemprop="name")
	b9 = b6.find_all(itemprop="offers")
	a1 = 0
	for apartment in b8:
		if apartment.b10 = = None:
			continue
		b11 = b7[a1].b10[1:].replace(",", "")
		b12 = b9[a1].find('a').get('href')
		print(apartment.b10 + "," + b11 + "," + b12)
		b1.write(apartment.b10+","+b11+","+b12+"\n")
		a1+=1
fonk1("Mandaluyong")