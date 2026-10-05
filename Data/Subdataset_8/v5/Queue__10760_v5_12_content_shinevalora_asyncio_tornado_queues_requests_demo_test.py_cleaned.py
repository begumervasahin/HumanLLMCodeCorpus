import re
import logging
import asyncio
import time
import requests
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")
HEADERS = {'User-Agent': 'Mozilla/5.0'}
DOUBAN_URL = "https:
OUTPUT_FILE = 'douban_top250.txt'
async def get_data():
    await asyncio.sleep(0)
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as file:
        file.write('Rank,Title,Director,Actors,Year,Country,Categories,Score,Number,Comments\n')
        for page in range(0, 250, 25):
            url = DOUBAN_URL.format(str(page))
            html = requests.get(url, headers=HEADERS).text
            logging.info(f"Page: {page}")
            all_pattern = re.findall(
                r'<em class="">(.*?)</em>.*?<img width="100" alt="(.*?)" src=".*?" class="">'
                r'.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>'
                r'.*?<span>(.*?)äººè¯ä»·</span>.*?<span class="inq">(.*?)</span>', html, re.S)
            logging.info(f"Length of all patterns: {len(all_pattern)}")
            for i in all_pattern:
                rank, title, director, actors, year, country, categories, score, number, comments = parse_data(i)
                file.write(f"{rank},{title},{director},{actors},{year},{country},{categories},{score},{number},{comments}\n")
                log_movie_info(rank, title, director, actors, year, country, categories, score, number, comments)
def parse_data(data_tuple):
    rank, title, text, score, number, comments = data_tuple
    director, actors, year, country, categories = [item.strip() for item in text.split("/") if item.strip()]
    return rank, title, director, actors, year, country, categories, score, number, comments
def log_movie_info(rank, title, director, actors, year, country, categories, score, number, comments):
    logging.info(f"Rank: {rank}")
    logging.info(f"Title: {title}")
    logging.info(f"Director: {director}")
    logging.info(f"Actors: {actors}")
    logging.info(f"Year: {year}")
    logging.info(f"Country: {country}")
    logging.info(f"Categories: {categories}")
    logging.info(f"Score: {score}")
    logging.info(f"Number: {number}")
    logging.info(f"Comments: {comments}")
async def create_task():
    await get_data()
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(create_task())
    end_time = time.time()
    logging.info(f"Total time consumed: {end_time - start_time} s")