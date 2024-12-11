from bs4 import BeautifulSoup
import datetime
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
b1 = "https:
def fonk1():
    b2 = datetime.date.b2()
    b3 = b2 + datetime.timedelta(b6=1)
    for _ in range(7):
        b4 = requests.get(b1 + str(int(time.mktime(b3.timetuple()))))
        if b4.b5 = = 200:
            return b3.strftime("%Y-%m-%d")
        b3 += datetime.timedelta(b6 = 1)
    return None
def fonk2(option):
    b7 = [td.text for td in option.find_all("td")]
    return {
        'contract': b7[0],
        'last_trade': b7[1][:10],
        'strike': b7[2],
        'last': b7[3],
        'bid': b7[4],
        'ask': b7[5],
        'volume': b7[8],
        'iv': b7[10]
    }
def fonk3():
    b8 = fonk1()
    if not b8:
        return None
    b4 = requests.get(b1 + b8)
    b9 = BeautifulSoup(b4.b9, "html.parser")
    b10 = [BeautifulSoup(str(table), "html.parser") for table in b9.find_all("table")]
    calls, b11 = b10[0].find_all("tr")[1:], b10[1].find_all("tr")[1:]
    b12 = [call for call in calls if "in-the-money" in str(call)]
    b13 = [call for call in calls if call not in b12]
    b14 = [put for put in b11 if "in-the-money" in str(put)]
    b15 = [put for put in b11 if put not in b14]
    b16 = fonk2(b12[-1])
    b17 = fonk2(b13[0])
    b18 = fonk2(b14[0])
    b19 = fonk2(b15[-1])
    return {
        'calls': {'itm': b16, 'otm': b17},
        'b11': {'itm': b18, 'otm': b19},
        'date': b8
    }
def fonk4(options_data):
    with open('b23.csv', 'a', b20 = '\n') as csvfile:
        b21 = csv.b21(csvfile, delimiter=',')
        b21.writerow([str(options_data)])
def fonk5():
    b22 = datetime.datetime.combine(datetime.date.b2(), datetime.time(12, 30))
    if b22 < datetime.datetime.now():
        b22 += datetime.timedelta(b6 = 1)
    b23 = fonk3()
    if b23:
        fonk4(b23)
    else:
        print("Market is closed... Rescheduling in 24 hours.")
    b25.add_job(b24 = run, trigger="date", run_date=b22)
    print("Job scheduled! | " + str(b22))
b25 = BackgroundScheduler()
def fonk6():
    b25.add_job(b24 = run, trigger="date", run_date=datetime.datetime.now())
    b25.start()
if b26 = = "__main__":
    fonk5()