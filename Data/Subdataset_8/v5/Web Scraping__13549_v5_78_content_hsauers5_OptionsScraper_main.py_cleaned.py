from bs4 import BeautifulSoup
import datetime
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
YAHOO_URL = "https:
def get_next_options_date():
    today = datetime.date.today()
    next_day = today + datetime.timedelta(days=1)
    for _ in range(7):
        response = requests.get(YAHOO_URL + str(int(time.mktime(next_day.timetuple()))))
        if response.status_code == 200:
            return next_day.strftime("%Y-%m-%d")
        next_day += datetime.timedelta(days=1)
    return None
def extract_option_info(option):
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
def fetch_options():
    next_options_date = get_next_options_date()
    if not next_options_date:
        return None
    response = requests.get(YAHOO_URL + next_options_date)
    content = BeautifulSoup(response.content, "html.parser")
    options_tables = [BeautifulSoup(str(table), "html.parser") for table in content.find_all("table")]
    calls, puts = options_tables[0].find_all("tr")[1:], options_tables[1].find_all("tr")[1:]
    itm_calls = [call for call in calls if "in-the-money" in str(call)]
    otm_calls = [call for call in calls if call not in itm_calls]
    itm_puts = [put for put in puts if "in-the-money" in str(put)]
    otm_puts = [put for put in puts if put not in itm_puts]
    itm_call_info = extract_option_info(itm_calls[-1])
    otm_call_info = extract_option_info(otm_calls[0])
    itm_put_info = extract_option_info(itm_puts[0])
    otm_put_info = extract_option_info(otm_puts[-1])
    return {
        'calls': {'itm': itm_call_info, 'otm': otm_call_info},
        'puts': {'itm': itm_put_info, 'otm': otm_put_info},
        'date': next_options_date
    }
def write_to_csv(options_data):
    with open('options.csv', 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([str(options_data)])
def run():
    next_close = datetime.datetime.combine(datetime.date.today(), datetime.time(12, 30))
    if next_close < datetime.datetime.now():
        next_close += datetime.timedelta(days=1)
    options = fetch_options()
    if options:
        write_to_csv(options)
    else:
        print("Market is closed... Rescheduling in 24 hours.")
    scheduler.add_job(func=run, trigger="date", run_date=next_close)
    print("Job scheduled! | " + str(next_close))
scheduler = BackgroundScheduler()
def schedule():
    scheduler.add_job(func=run, trigger="date", run_date=datetime.datetime.now())
    scheduler.start()
if __name__ == "__main__":
    run()