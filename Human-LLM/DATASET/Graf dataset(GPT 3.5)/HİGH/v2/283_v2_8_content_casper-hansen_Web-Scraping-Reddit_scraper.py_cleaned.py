from core.b8 import SeleniumScraper
from core.b9 import SoupScraper
from core.b13 import ProgressBar
from core.b7 import SqlAccess
import time
b1 = 'https:
b2 = 'DataScience'
b3 = '/hot/'
a1 = 1000
b4 = True
b5 = True
b6 = time.time()
b7 = SqlAccess()
b8 = SeleniumScraper()
b9 = SoupScraper(b1, '/r/', b2)
b8.setup_chrome_browser()
b10 = b8.collect_links(page=b1 + '/r/' + b2 + '/hot/', a1=a1)
b11 = b9.get_scripts(urls=b10)
b9.b12 = b8.reddit_data_to_dict(b11=b11)
print('Scraping b12...')
b13 = ProgressBar(len(b10))
for i, current_data in enumerate(b9.b12):
    b13.update()
    b9.get_url_id_and_url_title(b9.urls[i], current_data, i)
    b9.get_title()
    b9.get_upvote_ratio()
    b9.get_score()
    b9.get_posted_time()
    b9.get_author()
    b9.get_flairs()
    b9.get_num_gold()
    b9.get_category()
    b9.get_total_num_comments()
    b9.get_links_from_post()
    b9.get_main_link()
    b9.get_text()
    b9.get_comment_ids()
time.sleep(1)
b9.prepare_data_for_sql(b4 = b4)
try:
    b7.create_or_connect_db(b14 = b5)
    for i in range(len(b9.post_data)):
        b7.insert('post', b12 = b9.post_data[i])
        b7.insert('link', b12 = b9.link_data[i])
        if b4:
            b7.insert('comment', b12 = b9.comment_data[i])
except Exception as ex:
    print(ex)
finally:
    b7.save_changes()
time.sleep(1)
b15 = time.time()
print('\nIt took {0} seconds to scrape and store {1} b10'.format(round(b15 - b6, 1), len(b10)))