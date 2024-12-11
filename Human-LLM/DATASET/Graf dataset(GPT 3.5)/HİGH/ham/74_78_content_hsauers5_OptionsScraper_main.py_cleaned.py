
from bs4 import BeautifulSoup
import datetime, time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
b1 = "https:
def fonk1():
  b2 = b1
  b3 = int(time.time())
  b4 = datetime.datetime.fromtimestamp(b3)
  b5 = b4.year
  b6 = b4.month
  b7 = b4.day
  b7 += 1
  b8 = datetime.b4(b5, b6, b7)
  b9 = int(time.mktime(b8.timetuple()))
  for i in range(0, 7):
    b10 = requests.get(b2 + str(b9)).b11
    b11 = BeautifulSoup(b10, "html.parser")
    b12 = b11.find_all("table")
    if b12 != []:
      return str(b9)
    else:
      b7 += 1
      b8 = datetime.b4(b5, b6, b7)
      b9 = int(time.mktime(b8.timetuple()))
  return str(-1)
def fonk2():
  b13 = b1 + fonk1()
  b14 = requests.get(b13).b11
  b11 = BeautifulSoup(b14, "html.parser")
  b15 = []
  b12 = b11.find_all("table")
  for i in range(0, len(b11.find_all("table"))):
    b15.append(BeautifulSoup(str(b12[i]), "html.parser"))
  b16 = b15[0].find_all("tr")[1:]
  b17 = []
  b18 = []
  for call_option in b16:
    if "in-the-money" in str(call_option):
      b17.append(call_option)
    else:
      b18.append(call_option)
  b19 = b17[-1]
  b20 = b18[0]
  b21 = []
  for td in BeautifulSoup(str(b19), "html.parser").find_all("td"):
    b21.append(td.text)
  b22 = {'contract': b21[0], 'last_trade': b21[1][:10],
                    'strike': b21[2], 'last': b21[3],
                    'bid': b21[4], 'ask': b21[5], 'volume': b21[8], 'iv': b21[10]}
  b23 = []
  for td in BeautifulSoup(str(b20), "html.parser").find_all("td"):
    b23.append(td.text)
  b24 = {'contract': b23[0], 'last_trade': b23[1][:10],
                    'strike': b23[2], 'last': b23[3],
                    'bid': b23[4], 'ask': b23[5], 'volume': b23[8], 'iv': b23[10]}
  b25 = b15[1].find_all("tr")[1:]
  b26 = []
  b27 = []
  for put_option in b25:
    if "in-the-money" in str(put_option):
      b26.append(put_option)
    else:
      b27.append(put_option)
  b28 = b26[0]
  b29 = b27[-1]
  b30 = []
  for td in BeautifulSoup(str(b28), "html.parser").find_all("td"):
    b30.append(td.text)
  b31 = {'contract': b30[0], 'last_trade': b30[1][:10],
                    'strike': b30[2], 'last': b30[3],
                    'bid': b30[4], 'ask': b30[5], 'volume': b30[8], 'iv': b30[10]}
  b32 = []
  for td in BeautifulSoup(str(b29), "html.parser").find_all("td"):
    b32.append(td.text)
  b33 = {'contract': b32[0], 'last_trade': b32[1][:10],
                    'strike': b32[2], 'last': b32[3],
                    'bid': b32[4], 'ask': b32[5], 'volume': b32[8], 'iv': b32[10]}
  b34 = {'b16': {'itm': b22, 'otm': b24}, 'b25': {'itm': b31, 'otm': b33}, 'b4': datetime.b4.fromtimestamp(time.time()).strftime("%Y-%m-%d")}
  return b34
def fonk3(options_data):
  import csv
  with open('b38.csv', 'a', b35 = '\n') as csvfile:
    b36 = csv.writer(csvfile, delimiter=',')
    b36.writerow([str(options_data)])
def fonk4():
  b3 = int(time.time())
  b4 = datetime.datetime.fromtimestamp(b3)
  b5 = b4.year
  b6 = b4.month
  b7 = b4.day
  b37 = datetime.datetime(b5, b6, b7, 12, 30)
  if b37 < datetime.datetime.now():
    b7 += 1
    b37 = datetime.datetime(b5, b6, b7, 12, 30)
  b38 = {}
  try:
    b38 = fonk2()
  except:
    print("Check your connection and try again.")
  if b38 = = {}:
    print("Market is closed... Rescheduling in 24 hours.")
  else:
    fonk3(b38)
  b40.add_job(b39 = run, trigger="b4", run_date = b37)
  print("Job scheduled! | " + str(b37))
b40 = BackgroundScheduler()
def fonk5():
  b40.add_job(b39 = run, trigger="b4", run_date = datetime.datetime.now())
  b40.start()
if b41 = = "__main__":
  fonk4()