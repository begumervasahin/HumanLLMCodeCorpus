from core.selenium_scraper import SeleniumScraper
from core.soup_scraper import SoupScraper
from core.progress_bar import ProgressBar
from core.sql_access import SqlAccess
import time
reddit_home = 'https:
subreddit = 'DataScience'
sort_by = '/hot/'
scroll_n_times = 1000
scrape_comments = True
erase_db_first = True
start_time = time.time()
sql_access = SqlAccess()
selenium_scraper = SeleniumScraper()
soup_scraper = SoupScraper(reddit_home, '/r/', subreddit)
selenium_scraper.setup_chrome_browser()
links = selenium_scraper.collect_links(page=f"{reddit_home}/r/{subreddit}/hot/", scroll_n_times=scroll_n_times)
script_data = soup_scraper.get_scripts(urls=links)
soup_scraper.data = selenium_scraper.reddit_data_to_dict(script_data=script_data)
print('Scraping data...')
progress_bar = ProgressBar(len(links))
for i, current_data in enumerate(soup_scraper.data):
    progress_bar.update()
    soup_scraper.get_url_id_and_url_title(soup_scraper.urls[i], current_data, i)
    soup_scraper.extract_post_info()
    soup_scraper.extract_comment_info()
time.sleep(1)
soup_scraper.prepare_data_for_sql(scrape_comments=scrape_comments)
try:
    sql_access.create_or_connect_db(erase_first=erase_db_first)
    for post_data, link_data, comment_data in zip(soup_scraper.post_data, soup_scraper.link_data, soup_scraper.comment_data):
        sql_access.insert('post', data=post_data)
        sql_access.insert('link', data=link_data)
        if scrape_comments:
            sql_access.insert('comment', data=comment_data)
except Exception as ex:
    print(ex)
finally:
    sql_access.save_changes()
time.sleep(1)
end_time = time.time()
print(f'\nIt took {round(end_time - start_time, 1)} seconds to scrape and store {len(links)} links')