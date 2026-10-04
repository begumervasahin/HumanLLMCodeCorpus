from prettytable import PrettyTable
import requests
import bs4 as bs
import datetime
import sys
import Balloon_tip as Bt
b1 = {}
b2 = {1: 'India', 2: 'Japan', 3: 'USA', 4: 'UK', 5: 'Russia', 6: 'Japan', 7: 'France'}
b3 = datetime.datetime.now().strftime("%d-%b-%Y")
b4 = datetime.datetime.strptime(b3, "%d-%b-%Y")
b5 = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
for i in b2:
    print('{}. {}'.format(i, b2[i]))
while True:
    b6 = int(input('\nChoose any one of the above Countries: \n'))
    if b6 in b2.keys():
        break
    else:
        print('\n**** PLEASE CHOOSE A VALID COUNTRY. ****')
        for i in b2:
            print('{}. {}'.format(i, b2[i]))
b6 = b2[b6]
b7 = input('Enter a Location in {}: '.format(b6)).strip().lower()
b8 = int(input('Enter the No. of Days [1-14]: '))
b8 = 3 if b8 <= 0 or b8 > 14 else b8
b9 = 'https:
b10 = requests.get(b9, b5 = b5)
b11 = b10.text
b12 = bs.BeautifulSoup(b11, 'lxml')
b13 = b12.find('tbody')
for i in range(b8):
    b14 = b4 + datetime.timedelta(days=i)
    try:
        b15 = b13.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(2)").text
        b1[b14.strftime("%d-%b-%Y")] = [b15]
        b1[b14.strftime("%d-%b-%Y")].append(b13.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(3)").text)
        b1[b14.strftime("%d-%b-%Y")].append(b13.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(4)").text)
    except AttributeError:
        print('Weather Forecast NOT AVAILABLE for this Location. Please Enter a popular location.')
        sys.exit(8)
print('\n{}-Day Weather Forecast for {}, {}:'.format(b8, b7.title(), b6))
b16 = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for i in b1:
    b16.add_row([i, *b1[i]])
print(b16)
Bt.balloon_tip('Today\'s Weather Update - ' + b7.title() + ', ' + b6,'Min/Max Temp: {}\nWeather: {}\nFeels Like: {}'
               .format(b1[b3][0], b1[b3][1],b1[b3][2]))