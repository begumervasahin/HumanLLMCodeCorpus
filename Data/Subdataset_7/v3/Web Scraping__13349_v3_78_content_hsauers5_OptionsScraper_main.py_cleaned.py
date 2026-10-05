import requests
from bs4 import BeautifulSoup
import csv
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
b1 = "https:
def fonk1():
    b2 = datetime.datetime.now()
    b3 = datetime.datetime(b2.year, b2.month, b2.day, 12, 30)
    return b3 if b3 > b2 else b3 + datetime.timedelta(b4 = 1)
def fonk2():
    for i in range(7):
        b5 = datetime.datetime.now() + datetime.timedelta(b4=i)
        b6 = b1 + str(int(b5.timestamp()))
        b7 = requests.get(b6)
        b8 = BeautifulSoup(b7.b8, "html.parser")
        if b8.find_all("table"):
            return str(int(b5.timestamp()))
    return str(-1)
def fonk3():
    b9 = b1 + fonk2()
    b7 = requests.get(b9)
    b8 = BeautifulSoup(b7.b8, "html.parser")
    b10 = [BeautifulSoup(str(table), "html.parser") for table in b8.find_all("table")]
    calls, b11 = b10[0].find_all("tr")[1:], b10[1].find_all("tr")[1:]
    b12 = [call for call in calls if "in-the-money" in str(call)]
    b13 = [call for call in calls if "in-the-money" not in str(call)]
    b14 = [put for put in b11 if "in-the-money" in str(put)]
    b15 = [put for put in b11 if "in-the-money" not in str(put)]
    b16 = {
        'itm': fonk4(b12[-1]),
        'otm': fonk4(b13[0])
    }
    b17 = {
        'itm': fonk4(b14[0]),
        'otm': fonk4(b15[-1])
    }
    b18 = {
        'calls': b16,
        'b11': b17,
        'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    return b18
def fonk4(option):
    b19 = [td.text for td in option.find_all("td")]
    return {
        'contract': b19[0],
        'last_trade': b19[1][:10],
        'strike': b19[2],
        'last': b19[3],
        'bid': b19[4],
        'ask': b19[5],
        'volume': b19[8],
        'iv': b19[10]
    }
def fonk5(options_data):
    with open('b23.csv', 'a', b20 = '\n') as csvfile:
        b21 = csv.b21(csvfile, delimiter=',')
        b21.writerow([str(options_data)])
def fonk6():
    b22 = fonk1()
    print("Next data fetch scheduled for:", b22)
    try:
        b23 = fonk3()
        fonk5(b23)
    except Exception as e:
        print("An error occurred:", e)
        print("Please check your connection and try again.")
    b25.add_job(b24 = run, trigger="date", run_date=b22)
b25 = BackgroundScheduler()
if b26 = = "__main__":
    b25.start()
    b25.add_job(b24 = run, trigger="date", run_date=datetime.datetime.now())
    input("Press Enter to exit.")