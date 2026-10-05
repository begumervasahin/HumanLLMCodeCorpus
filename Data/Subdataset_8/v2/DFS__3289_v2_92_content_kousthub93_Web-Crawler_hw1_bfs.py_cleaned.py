import requests
from bs4 import BeautifulSoup
import re
import time
def delete_duplicates(unique_links, temp_links, list_crawled, list_master):
    for link in temp_links:
        if link not in unique_links and len(link) > 1 and link not in list_crawled:
            unique_links.append(link)
    for link in unique_links:
        if link not in list_master:
            list_master.append(link)
    return unique_links
def hit_url(next_url, list_crawled, list_master):
    list_crawled.append(next_url)
    unique_links = []
    temp_links = []
    time.sleep(1)
    data = requests.get(next_url)
    data_text = data.text
    soup = BeautifulSoup(data_text, 'html.parser')
    data_in_focus = soup.find('div', {'id': 'mw-content-text'})
    for link in data_in_focus.find_all('a', {'href': re.compile("^/wiki")}):
        if ':' not in link.get('href'):
            final_url = "https:
            list_without_hash = final_url.split('
            temp_links.append(str(list_without_hash[0]))
    return delete_duplicates(unique_links, temp_links, list_crawled, list_master)
def next_link_to_crawl(list_in_use, *lists, list_crawled):
    for link in list_in_use:
        if link not in list_crawled:
            return link
    for lst in lists:
        if len(lst) < 1000:
            return next_link_to_crawl(lst, *lists, list_crawled)
    return 'links not found'
def list_belongs_to(next_page_url, *lists):
    for lst in lists:
        if next_page_url in lst:
            return lst
def main_web_crawler(start_url):
    list_master = []
    list_depth1 = []
    list_depth2 = []
    list_depth3 = []
    list_depth4 = []
    list_depth5 = []
    list_depth6 = []
    list_crawled = []
    list_master.append(start_url)
    list_depth1.append(start_url)
    while len(list_master) < 1000:
        next_page_url = next_link_to_crawl(list_depth1, list_depth1, list_depth2, list_depth3, list_depth4, list_depth5, list_depth6, list_crawled)
        if next_page_url == 'links not found':
            print("Crawling ends: No further links found")
            break
        else:
            current_list = list_belongs_to(next_page_url, list_depth1, list_depth2, list_depth3, list_depth4, list_depth5, list_depth6)
            if current_list == list_depth1:
                depth1_urls = hit_url(next_page_url, list_crawled, list_master)
                for link in depth1_urls:
                    list_depth2.append(link)
            elif current_list == list_depth2:
                depth2_urls = hit_url(next_page_url, list_crawled, list_master)
                for link in depth2_urls:
                    if link not in list_depth1 and link not in list_depth2:
                        list_depth3.append(link)
            elif current_list == list_depth3:
                depth3_urls = hit_url(next_page_url, list_crawled, list_master)
                for link in depth3_urls:
                    if link not in list_depth2 and link not in list_depth3:
                        list_depth4.append(link)
            elif current_list == list_depth4:
                depth4_urls = hit_url(next_page_url, list_crawled, list_master)
                for link in depth4_urls:
                    if link not in list_depth3 and link not in list_depth4:
                        list_depth5.append(link)
            elif current_list == list_depth5:
                depth5_urls = hit_url(next_page_url, list_crawled, list_master)
                for link in depth5_urls:
                    if link not in list_depth4 and link not in list_depth5:
                        list_depth6.append(link)
    with open('TASK 1-E.txt', 'w') as file:
        for url in list_master[:1000]:
            file.write(url.lower() + "\n")
start_url = "https:
main_web_crawler(start_url)