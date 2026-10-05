
from core.selenium_scraper import SeleniumScraper
from core.soup_scraper import SoupScraper
from core.progress_bar import ProgressBar
from core.sql_access import SqlAccess
import time
b1 = 'https:
b2 = '/r/'
b3 = 'DataScience'
b4 = '/hot/'
a1 = 1000
b5 = True
b6 = True
b7 = time.time()
b8 = SqlAccess()
b9 = SeleniumScraper()
b10 = SoupScraper(b1, b2, b3)
b9.setup_chrome_browser()
b11 = b9.collect_links(page=b1 + b2 + b3 + b4,
                                 a1 = a1)
b12 = b10.get_scripts(urls=b11)
b10.b13 = b9.reddit_data_to_dict(b12=b12)
print('Scraping b13...')
b14 = ProgressBar(len(b11))
for i, current_data in enumerate(b10.b13):
    b14.update()
    b10.get_url_id_and_url_title(b10.urls[i], current_data, i)
    b10.get_title()
    b10.get_upvote_ratio()
    b10.get_score()
    b10.get_posted_time()
    b10.get_author()
    b10.get_flairs()
    b10.get_num_gold()
    b10.get_category()
    b10.get_total_num_comments()
    b10.get_links_from_post()
    b10.get_main_link()
    b10.get_text()
    b10.get_comment_ids()
time.sleep(1)
b10.prepare_data_for_sql(b5 = b5)
try:
    b8.create_or_connect_db(b15 = b6)
    for i in range(len(b10.post_data)):
        b8.insert('post', b13 = b10.post_data[i])
        b8.insert('link', b13 = b10.link_data[i])
        if b5:
            b8.insert('comment', b13 = b10.comment_data[i])
except Exception as ex:
    print(ex)
finally:
    b8.save_changes()
time.sleep(1)
b16 = time.time()
print('\nIt took {0} seconds to scrape and store {1} b11'.format(round(b16 - b7, 1),
                                                                   len(b11)))