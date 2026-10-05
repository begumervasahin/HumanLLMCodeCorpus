from bs4 import BeautifulSoup
import datetime
import requests
import csv
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
        b7 = requests.get(b6).b8
        b8 = BeautifulSoup(b7, "html.parser")
        b9 = b8.find_all("table")
        if b9:
            return str(int(time.mktime(b5.timetuple())))
    return str(-1)
def fonk3():
    b10 = b1 + fonk2()
    b11 = requests.get(b10).b8
    b8 = BeautifulSoup(b11, "html.parser")
    b12 = [BeautifulSoup(str(table), "html.parser") for table in b8.find_all("table")]
    b13 = b12[0].find_all("tr")[1:]
    b14 = b12[1].find_all("tr")[1:]
    b15 = [call for call in b13 if "in-the-money" in str(call)]
    b16 = [call for call in b13 if "in-the-money" not in str(call)]
    b17 = [put for put in b14 if "in-the-money" in str(put)]
    b18 = [put for put in b14 if "in-the-money" not in str(put)]
    b19 = {
        'itm': fonk4(b15[-1]),
        'otm': fonk4(b16[0])
    }
    b20 = {
        'itm': fonk4(b17[0]),
        'otm': fonk4(b18[-1])
    }
    b21 = {
        'b13': b19,
        'b14': b20,
        'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    return b21
def fonk4(option):
    b22 = [td.text for td in option.find_all("td")]
    return {
        'contract': b22[0],
        'last_trade': b22[1][:10],
        'strike': b22[2],
        'last': b22[3],
        'bid': b22[4],
        'ask': b22[5],
        'volume': b22[8],
        'iv': b22[10]
    }
def fonk5(options_data):
    with open('b25.csv', 'a', b23 = '\n') as csvfile:
        b24 = csv.writer(csvfile, delimiter=',')
        b24.writerow([str(options_data)])
def fonk6():
    b3 = fonk1()
    print("Job scheduled! | " + str(b3))
    try:
        b25 = fonk3()
        fonk5(b25)
    except Exception as e:
        print("Error:", e)
        print("Check your connection and try again.")
    b27.add_job(b26 = run, trigger="date", run_date=b3)
b27 = BackgroundScheduler()
if b28 = = "__main__":
    b27.start()
    b27.add_job(b26 = run, trigger="date", run_date=datetime.datetime.now())
    input("Press enter to exit.")