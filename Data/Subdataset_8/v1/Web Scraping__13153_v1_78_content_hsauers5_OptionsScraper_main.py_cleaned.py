from bs4 import BeautifulSoup
import datetime
import requests
import csv
import time
from apscheduler.schedulers.background import BackgroundScheduler
YAHOO_URL = "https:
def get_next_trading_date():
    today = datetime.datetime.now()
    next_close = datetime.datetime(today.year, today.month, today.day, 12, 30)
    if next_close < today:
        next_close += datetime.timedelta(days=1)
    return next_close
def get_datestamp():
    today = datetime.datetime.now()
    for i in range(0, 7):
        options_day = today + datetime.timedelta(days=i)
        options_url = YAHOO_URL + str(int(time.mktime(options_day.timetuple())))
        test_req = requests.get(options_url).content
        content = BeautifulSoup(test_req, "html.parser")
        tables = content.find_all("table")
        if tables:
            return str(int(time.mktime(options_day.timetuple())))
    return str(-1)
def fetch_options():
    data_url = YAHOO_URL + get_datestamp()
    data_html = requests.get(data_url).content
    content = BeautifulSoup(data_html, "html.parser")
    options_tables = [BeautifulSoup(str(table), "html.parser") for table in content.find_all("table")]
    calls = options_tables[0].find_all("tr")[1:]
    puts = options_tables[1].find_all("tr")[1:]
    itm_calls = [call for call in calls if "in-the-money" in str(call)]
    otm_calls = [call for call in calls if "in-the-money" not in str(call)]
    itm_puts = [put for put in puts if "in-the-money" in str(put)]
    otm_puts = [put for put in puts if "in-the-money" not in str(put)]
    call_data = {
        'itm': get_option_info(itm_calls[-1]),
        'otm': get_option_info(otm_calls[0])
    }
    put_data = {
        'itm': get_option_info(itm_puts[0]),
        'otm': get_option_info(otm_puts[-1])
    }
    options_list = {
        'calls': call_data,
        'puts': put_data,
        'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    return options_list
def get_option_info(option):
    option_data = [td.text for td in option.find_all("td")]
    return {
        'contract': option_data[0],
        'last_trade': option_data[1][:10],
        'strike': option_data[2],
        'last': option_data[3],
        'bid': option_data[4],
        'ask': option_data[5],
        'volume': option_data[8],
        'iv': option_data[10]
    }
def write_to_csv(options_data):
    with open('options.csv', 'a', newline='\n') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([str(options_data)])
def run():
    next_close = get_next_trading_date()
    print("Job scheduled! | " + str(next_close))
    try:
        options = fetch_options()
        write_to_csv(options)
    except Exception as e:
        print("Error:", e)
        print("Check your connection and try again.")
    scheduler.add_job(func=run, trigger="date", run_date=next_close)
scheduler = BackgroundScheduler()
if __name__ == "__main__":
    scheduler.start()
    scheduler.add_job(func=run, trigger="date", run_date=datetime.datetime.now())
    input("Press enter to exit.")