
from core.selenium_scraper import SeleniumScraper
from core.soup_scraper import SoupScraper
from core.progress_bar import ProgressBar
from core.sql_access import SqlAccess
import time
reddit_home = 'https:
slash = '/r/'
subreddit = 'DataScience'
sort_by = '/hot/'
scroll_n_times = 1000
scrape_comments = True
erase_db_first = True
start_time = time.time()
database = SqlAccess()
selenium_scraper = SeleniumScraper()
soup_scraper = SoupScraper(reddit_home, slash, subreddit)
selenium_scraper.setup_chrome_browser()
links = selenium_scraper.collect_links(page=reddit_home + slash + subreddit + sort_by,
                                       scroll_n_times=scroll_n_times)
script_data = soup_scraper.get_scripts(urls=links)
soup_scraper.data = selenium_scraper.reddit_data_to_dict(script_data=script_data)
print('Scraping data...')
progress_bar = ProgressBar(len(links))
for index, current_data in enumerate(soup_scraper.data):
    progress_bar.update()
    soup_scraper.get_url_id_and_url_title(soup_scraper.urls[index], current_data, index)
    soup_scraper.get_title()
    soup_scraper.get_upvote_ratio()
    soup_scraper.get_score()
    soup_scraper.get_posted_time()
    soup_scraper.get_author()
    soup_scraper.get_flairs()
    soup_scraper.get_num_gold()
    soup_scraper.get_category()
    soup_scraper.get_total_num_comments()
    soup_scraper.get_links_from_post()
    soup_scraper.get_main_link()
    soup_scraper.get_text()
    soup_scraper.get_comment_ids()
time.sleep(1)
soup_scraper.prepare_data_for_sql(scrape_comments=scrape_comments)
try:
    database.create_or_connect_db(erase_first=erase_db_first)
    for i in range(len(soup_scraper.post_data)):
        database.insert('post', data=soup_scraper.post_data[i])
        database.insert('link', data=soup_scraper.link_data[i])
        if scrape_comments:
            database.insert('comment', data=soup_scraper.comment_data[i])
except Exception as ex:
    print(ex)
finally:
    database.save_changes()
time.sleep(1)
end_time = time.time()
print('\nIt took {0} seconds to scrape and store {1} links'.format(round(end_time - start_time, 1),
                                                                   len(links)))