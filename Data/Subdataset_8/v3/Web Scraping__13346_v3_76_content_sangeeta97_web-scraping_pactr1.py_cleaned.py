import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
START_ID = 86
END_ID = 10000
URL_TEMPLATE = "https:
def extract_trial_data(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'lxml')
        primary_topic = soup.find_all('table')[2].find_all('td')[2].get_text().strip()
        participant_type = soup.find_all('table')[2].find_all('td')[9].get_text().strip()
        study_type = soup.find_all('table')[2].find_all('td')[11].get_text().strip()
        notes = ' '.join(td.text.strip() for td in soup.find_all('table')[4].find_all('td'))
        time.sleep(2)
        return primary_topic, participant_type, study_type, notes
    except Exception as e:
        print(f"Error processing URL: {url} | Error: {e}")
        return 'no_value', 'no_value', 'no_value', 'no_value'
trial_urls = [URL_TEMPLATE.format(trial_id) for trial_id in range(START_ID, END_ID)]
with ThreadPool(mp.cpu_count()) as pool:
    results = pool.map(extract_trial_data, trial_urls)
df = pd.DataFrame(results, columns=['Primary Topic', 'Participant Type', 'Study Type', 'Notes'])
trial_info_df = pd.DataFrame({'Number': range(START_ID, END_ID), 'URL': trial_urls})
final_df = pd.concat([trial_info_df, df], axis=1)
final_df.to_excel('pac_trials_info.xlsx', index=False)
print("Data extraction and saving completed.")