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
b10 = b8.collect_links(page=f"{b1}/r/{b2}/hot/", a1=a1)
b11 = b9.get_scripts(urls=b10)
b9.b12 = b8.reddit_data_to_dict(b11=b11)
print('Scraping b12...')
b13 = ProgressBar(len(b10))
for i, current_data in enumerate(b9.b12):
    b13.update()
    b9.get_url_id_and_url_title(b9.urls[i], current_data, i)
    b9.extract_post_info()
    b9.extract_comment_info()
time.sleep(1)
b9.prepare_data_for_sql(b4 = b4)
try:
    b7.create_or_connect_db(b14 = b5)
    for post_data, link_data, comment_data in zip(b9.post_data, b9.link_data, b9.comment_data):
        b7.insert('post', b12 = post_data)
        b7.insert('link', b12 = link_data)
        if b4:
            b7.insert('comment', b12 = comment_data)
except Exception as ex:
    print(ex)
finally:
    b7.save_changes()
time.sleep(1)
b15 = time.time()
print(f'\nIt took {round(b15 - b6, 1)} seconds to scrape and store {len(b10)} b10')