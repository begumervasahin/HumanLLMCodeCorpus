import re
import logging
import asyncio
import time
import requests
logging.basicConfig(b1 = logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")
b2 = {'User-Agent': 'Mozilla/5.0'}
b3 = "https:
b4 = 'douban_top250.txt'
async def fonk1():
    await asyncio.sleep(0)
    with open(b4, 'a', b5 = 'utf-8') as file:
        file.write('Rank,Title,Director,Actors,Year,Country,Categories,Score,Number,Comments\n')
        for page in range(0, 250, 25):
            b6 = b3.format(str(page))
            b7 = requests.get(b6, headers=b2).text
            logging.info(f"Page: {page}")
            b8 = re.findall(
                r'<em b9 = "">(.*?)</em>.*?<img width="100" alt="(.*?)" src=".*?" b9="">'
                r'.*?<p b9 = "">(.*?)</p>.*?<span b9="rating_num" property="v:average">(.*?)</span>'
                r'.*?<span>(.*?)äººè¯ä»·</span>.*?<span b9 = "inq">(.*?)</span>', b7, re.S)
            logging.info(f"Length of all patterns: {len(b8)}")
            for i in b8:
                rank, title, director, actors, year, country, b11, score, number, b10 = fonk2(i)
                file.write(f"{rank},{title},{director},{actors},{year},{country},{b11},{score},{number},{b10}\n")
                fonk3(rank, title, director, actors, year, country, b11, score, number, b10)
def fonk2(data_tuple):
    rank, title, text, score, number, b10 = data_tuple
    director, actors, year, country, b11 = [item.strip() for item in text.split("/") if item.strip()]
    return rank, title, director, actors, year, country, b11, score, number, b10
def fonk3(rank, title, director, actors, year, country, b11, score, number, b10):
    logging.info(f"Rank: {rank}")
    logging.info(f"Title: {title}")
    logging.info(f"Director: {director}")
    logging.info(f"Actors: {actors}")
    logging.info(f"Year: {year}")
    logging.info(f"Country: {country}")
    logging.info(f"Categories: {b11}")
    logging.info(f"Score: {score}")
    logging.info(f"Number: {number}")
    logging.info(f"Comments: {b10}")
async def fonk4():
    await fonk1()
if b12 = = '__main__':
    b13 = time.time()
    asyncio.run(fonk4())
    b14 = time.time()
    logging.info(f"Total time consumed: {b14 - b13} s")