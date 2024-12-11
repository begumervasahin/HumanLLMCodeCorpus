import pandas as pd
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
from time import sleep
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
b1 = pd.read_excel('eunew1.xlsx')
def fonk1(url):
    """
    Fetches the content from the URL and parses specific data using BeautifulSoup.
    Retries fetching up to three times in case of ConnectionErrors.
    Args:
        url (str): The URL to fetch and parse.
    Returns:
        list: A list of parsed text from HTML <td> elements with class "third".
    """
    a1 = 3
    a2 = 2
    for attempt in range(a1):
        try:
            b2 = requests.get(url, verify=False)
            b2.raise_for_status()
            break
        except RequestException:
            if attempt < a1 - 1:
                sleep(a2)
            else:
                raise
    b3 = BeautifulSoup(b2.content, 'html.parser')
    b4 = [td.text.strip().splitlines() for td in b3.find_all("td", class_="third", limit=8)]
    return b4
def fonk2(urls, function, b7):
    with ThreadPool(b7) as pool:
        b5 = pool.map(function, urls)
    return b5
if b6 = = "__main__":
    b7 = mp.cpu_count()
    b8 = b1['url'].tolist()
    b9 = fonk2(b8, fetch_and_parse_url, b7)
    b10 = pd.DataFrame(np.array(b9), columns=['data'])
    b11 = pd.concat([b1, b10], axis=1)
    b11.to_excel('results_oct.xlsx', b12 = False)