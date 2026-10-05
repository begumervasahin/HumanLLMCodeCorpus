import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
start_id = 86
end_id = 10000
index = list(range(start_id, end_id))
urls = [f"https:
df = pd.DataFrame({'number': index, 'url': urls})
def extract_text(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'lxml')
        primary_topic = soup.find_all('table')[2].find_all('td')[2].get_text().strip()
        participant_type = soup.find_all('table')[2].find_all('td')[9].get_text().strip()
        study_type = soup.find_all('table')[2].find_all('td')[11].get_text().strip()
        notes = ' '.join([td.text.strip() for td in soup.find_all('table')[4].find_all('td')])
        time.sleep(2)
        return primary_topic, participant_type, study_type, notes
    except Exception as e:
        print(f"Error processing URL: {url} | Error: {str(e)}")
        return ('no_value',) * 4
pool = ThreadPool(mp.cpu_count())
results = pool.map(extract_text, urls)
pool.close()
pool.join()
df2 = pd.DataFrame(results, columns=['Primary Topic', 'Participant Type', 'Study Type', 'Notes'])
df_final = pd.concat([df, df2], axis=1)
df_final.to_excel('pac_trials_info.xlsx', index=False)
print("Data extraction and saving completed.")