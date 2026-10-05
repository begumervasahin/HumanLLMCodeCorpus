
from bs4 import BeautifulSoup
import datetime
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
YAHOO_URL = "https:
def get_datestamp():
    options_url = YAHOO_URL
    today = int(time.time())
    date = datetime.datetime.fromtimestamp(today)
    yy = date.year
    mm = date.month
    dd = date.day + 1
    options_day = datetime.date(yy, mm, dd)
    for i in range(0, 7):
        test_req = requests.get(options_url + str(int(time.mktime(options_day.timetuple())))).content
        content = BeautifulSoup(test_req, "html.parser")
        tables = content.find_all("table")
        if tables != []:
            return str(int(time.mktime(options_day.timetuple())))
        else:
            dd += 1
            options_day = datetime.date(yy, mm, dd)
    return str(-1)
def fetch_options():
    data_url = YAHOO_URL + get_datestamp()
    data_html = requests.get(data_url).content
    content = BeautifulSoup(data_html, "html.parser")
    options_tables = [BeautifulSoup(str(table), "html.parser") for table in content.find_all("table")]
    calls = options_tables[0].find_all("tr")[1:]
    itm_calls = []
    otm_calls = []
    for call_option in calls:
        if "in-the-money" in str(call_option):
            itm_calls.append(call_option)
        else:
            otm_calls.append(call_option)
    itm_call = itm_calls[-1]
    otm_call = otm_calls[0]
    itm_call_info = extract_option_info(itm_call)
    otm_call_info = extract_option_info(otm_call)
    puts = options_tables[1].find_all("tr")[1:]
    itm_puts = []
    otm_puts = []
    for put_option in puts:
        if "in-the-money" in str(put_option):
            itm_puts.append(put_option)
        else:
            otm_puts.append(put_option)
    itm_put = itm_puts[0]
    otm_put = otm_puts[-1]
    itm_put_info = extract_option_info(itm_put)
    otm_put_info = extract_option_info(otm_put)
    options_list = {'calls': {'itm': itm_call_info, 'otm': otm_call_info},
                    'puts': {'itm': itm_put_info, 'otm': otm_put_info},
                    'date': datetime.date.fromtimestamp(time.time()).strftime("%Y-%m-%d")}
    return options_list
def extract_option_info(option):
    option_data = []
    for td in BeautifulSoup(str(option), "html.parser").find_all("td"):
        option_data.append(td.text)
    option_info = {'contract': option_data[0], 'last_trade': option_data[1][:10],
                   'strike': option_data[2], 'last': option_data[3],
                   'bid': option_data[4], 'ask': option_data[5], 'volume': option_data[8], 'iv': option_data[10]}
    return option_info
def write_to_csv(options_data):
    import csv
    with open('options.csv', 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(options_data)])
def run():
    today = int(time.time())
    date = datetime.datetime.fromtimestamp(today)
    yy = date.year
    mm = date.month
    dd = date.day
    next_close = datetime.datetime(yy, mm, dd, 12, 30)
    if next_close < datetime.datetime.now():
        dd += 1
        next_close = datetime.datetime(yy, mm, dd, 12, 30)
    options = {}
    try:
        options = fetch_options()
    except:
        print("Check your connection and try again.")
    if options == {}:
        print("Market is closed... Rescheduling in 24 hours.")
    else:
        write_to_csv(options)
    scheduler.add_job(func=run, trigger="date", run_date=next_close)
    print("Job scheduled! | " + str(next_close))
scheduler = BackgroundScheduler()
def schedule():
    scheduler.add_job(func=run, trigger="date", run_date=datetime.datetime.now())
    scheduler.start()
if __name__ == "__main__":
    run()