import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
b1 = "https:
def fonk1():
    b2 = datetime.datetime.now()
    b3 = datetime.datetime(b2.year, b2.month, b2.day, 12, 30)
    if b3 < b2:
        b3 += datetime.timedelta(b4 = 1)
    return b3
def fonk2():
    b2 = datetime.datetime.now()
    for i in range(0, 7):
        b5 = b2 + datetime.timedelta(b4=i)
        b6 = b1 + str(int(time.mktime(b5.timetuple())))
        b7 = requests.get(b6)
        b8 = BeautifulSoup(b7.b8, "html.parser")
        b9 = b8.find_all("table")
        if b9:
            return str(int(time.mktime(b5.timetuple())))
    return str(-1)
def fonk3():
    b10 = b1 + fonk2()
    b7 = requests.get(b10)
    b8 = BeautifulSoup(b7.b8, "html.parser")
    b11 = [BeautifulSoup(str(table), "html.parser") for table in b8.find_all("table")]
    b12 = b11[0].find_all("tr")[1:]
    b13 = b11[1].find_all("tr")[1:]
    b14 = [call for call in b12 if "in-the-money" in str(call)]
    b15 = [call for call in b12 if "in-the-money" not in str(call)]
    b16 = [put for put in b13 if "in-the-money" in str(put)]
    b17 = [put for put in b13 if "in-the-money" not in str(put)]
    b18 = {
        'itm': fonk4(b14[-1]),
        'otm': fonk4(b15[0])
    }
    b19 = {
        'itm': fonk4(b16[0]),
        'otm': fonk4(b17[-1])
    }
    b20 = {
        'b12': b18,
        'b13': b19,
        'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    return b20
def fonk4(option):
    b21 = [td.text for td in option.find_all("td")]
    return {
        'contract': b21[0],
        'last_trade': b21[1][:10],
        'strike': b21[2],
        'last': b21[3],
        'bid': b21[4],
        'ask': b21[5],
        'volume': b21[8],
        'iv': b21[10]
    }
def fonk5(options_data):
    with open('b24.csv', 'a', b22 = '\n') as csvfile:
        b23 = csv.b23(csvfile, delimiter=',')
        b23.writerow([str(options_data)])
def fonk6():
    b3 = fonk1()
    print("Next data fetch scheduled for:", b3)
    try:
        b24 = fonk3()
        fonk5(b24)
    except Exception as e:
        print("Error occurred:", e)
        print("Please check your connection and try again.")
    b26.add_job(b25 = run, trigger="date", run_date=b3)
b26 = BackgroundScheduler()
if b27 = = "__main__":
    b26.start()
    b26.add_job(b25 = run, trigger="date", run_date=datetime.datetime.now())
    input("Press Enter to exit.")