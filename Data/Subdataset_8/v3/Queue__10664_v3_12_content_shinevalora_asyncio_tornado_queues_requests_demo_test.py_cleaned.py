import re
import logging
import asyncio
import time
import aiohttp
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")
headers = {'User-Agent': 'Mozilla/5.0'}
async def fetch_data(session, page):
    url = f"https:
    async with session.get(url, headers=headers) as response:
        return await response.text()
async def parse_data(html, file):
    pattern = re.compile(r'<em class="">(.*?)</em>.*?<img width="100" alt="(.*?)" src=".*?" class="">.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)äººè¯ä»·</span>.*?<span class="inq">(.*?)</span>', re.S)
    all_patterns = re.findall(pattern, html)
    for item in all_patterns:
        rank, title, text, score, number, comments = item[0], item[1], item[2].replace("\n                            ", " ").replace("&nbsp;&nbsp;&nbsp;", " ").replace("&nbsp;", " ").replace("\n                        ", " "), item[3], item[4], item[5]
        contents = text.split(" ")
        director, actors, year, country, categories = contents[0], contents[1], contents[2], contents[3], contents[-1]
        file.write(f"{rank},{title},{director},{actors},{year},{country},{categories},{score},{number},{comments}\n")
        logging.info(f"Rank: {rank}, Title: {title}, Director: {director}, Actors: {actors}, Year: {year}, Country: {country}, Categories: {categories}, Score: {score}, Number: {number}, Comments: {comments}")
async def get_data():
    async with aiohttp.ClientSession() as session:
        async with open('douban_top250.txt', 'a', encoding='utf-8') as file:
            file.write('Rank,Title,Director,Actors,Year,Country,Categories,Score,Number,Comments\n')
            for page in range(0, 250, 25):
                html = await fetch_data(session, page)
                logging.info(f"Page: {page}")
                logging.info(f"HTML Content Length: {len(html)}")
                await parse_data(html, file)
async def main():
    start_time = time.time()
    await get_data()
    end_time = time.time()
    logging.info(f"Total Time Consumed: {end_time - start_time} s")
if __name__ == '__main__':
    asyncio.run(main())