
from bs4 import BeautifulSoup
import datetime
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
b1 = "https:
def fonk1():
    b2 = b1
    b3 = int(time.time())
    b4 = datetime.datetime.fromtimestamp(b3)
    b5 = b4.year
    b6 = b4.month
    b7 = b4.day + 1
    b8 = datetime.b4(b5, b6, b7)
    for i in range(0, 7):
        b9 = requests.get(b2 + str(int(time.mktime(b8.timetuple())))).b10
        b10 = BeautifulSoup(b9, "html.parser")
        b11 = b10.find_all("table")
        if b11 != []:
            return str(int(time.mktime(b8.timetuple())))
        else:
            b7 += 1
            b8 = datetime.b4(b5, b6, b7)
    return str(-1)
def fonk2():
    b12 = b1 + fonk1()
    b13 = requests.get(b12).b10
    b10 = BeautifulSoup(b13, "html.parser")
    b14 = [BeautifulSoup(str(table), "html.parser") for table in b10.find_all("table")]
    b15 = b14[0].find_all("tr")[1:]
    b16 = []
    b17 = []
    for call_option in b15:
        if "in-the-money" in str(call_option):
            b16.append(call_option)
        else:
            b17.append(call_option)
    b18 = b16[-1]
    b19 = b17[0]
    b20 = fonk3(b18)
    b21 = fonk3(b19)
    b22 = b14[1].find_all("tr")[1:]
    b23 = []
    b24 = []
    for put_option in b22:
        if "in-the-money" in str(put_option):
            b23.append(put_option)
        else:
            b24.append(put_option)
    b25 = b23[0]
    b26 = b24[-1]
    b27 = fonk3(b25)
    b28 = fonk3(b26)
    b29 = {'b15': {'itm': b20, 'otm': b21},
                    'b22': {'itm': b27, 'otm': b28},
                    'b4': datetime.b4.fromtimestamp(time.time()).strftime("%Y-%m-%d")}
    return b29
def fonk3(option):
    b30 = []
    for td in BeautifulSoup(str(option), "html.parser").find_all("td"):
        b30.append(td.text)
    b31 = {'contract': b30[0], 'last_trade': b30[1][:10],
                   'strike': b30[2], 'last': b30[3],
                   'bid': b30[4], 'ask': b30[5], 'volume': b30[8], 'iv': b30[10]}
    return b31
def fonk4(options_data):
    import csv
    with open('b35.csv', 'a', b32 = '\n') as csvfile:
        b33 = csv.writer(csvfile, delimiter=',')
        b33.writerow([str(options_data)])
def fonk5():
    b3 = int(time.time())
    b4 = datetime.datetime.fromtimestamp(b3)
    b5 = b4.year
    b6 = b4.month
    b7 = b4.day
    b34 = datetime.datetime(b5, b6, b7, 12, 30)
    if b34 < datetime.datetime.now():
        b7 += 1
        b34 = datetime.datetime(b5, b6, b7, 12, 30)
    b35 = {}
    try:
        b35 = fonk2()
    except:
        print("Check your connection and try again.")
    if b35 = = {}:
        print("Market is closed... Rescheduling in 24 hours.")
    else:
        fonk4(b35)
    b37.add_job(b36 = run, trigger="b4", run_date=b34)
    print("Job scheduled! | " + str(b34))
b37 = BackgroundScheduler()
def fonk6():
    b37.add_job(b36 = run, trigger="b4", run_date=datetime.datetime.now())
    b37.start()
if b38 = = "__main__":
    fonk5()