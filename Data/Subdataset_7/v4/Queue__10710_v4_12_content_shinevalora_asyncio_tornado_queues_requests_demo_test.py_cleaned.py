import re
import logging
import asyncio
import time
import requests
logging.basicConfig(b1 = logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")
b2 = {'User-Agent': 'Mozilla/5.0'}
async def fonk1():
    await asyncio.sleep(0)
    with open('douban_top250.txt', 'a', b3 = 'utf-8') as file:
        file.write('Rank,Title,Director,Actors,Year,Country,Categories,Score,Number,Comments\n')
        for page in range(0, 250, 25):
            b4 = requests.get(f"https:
            logging.info(f"Page: {page}")
            b5 = re.compile(
                r'<em b6 = "">(.*?)</em>.*?<img width="100" alt="(.*?)" src=".*?" b6="">'
                r'.*?<p b6 = "">(.*?)</p>.*?<span b6="rating_num" property="v:average">(.*?)</span>'
                r'.*?<span>(.*?)äººè¯ä»·</span>.*?<span b6 = "inq">(.*?)</span>', re.S)
            b7 = re.findall(b5, b4)
            logging.info(f"Length of all patterns: {len(b7)}")
            for i in b7:
                b8 = i[0]
                b9 = i[1]
                b10 = i[2].replace("\n                            ", " ").replace("&nbsp;&nbsp;&nbsp;", " ")\
                    .replace("&nbsp;", " ").replace("\n                        ", " ")
                b11 = b10.split("/")
                b12 = b11[0]
                b13 = b11[1]
                b14 = b11[2]
                b15 = b11[3]
                b16 = b11[-1]
                b17 = i[3]
                b18 = i[4]
                b19 = i[5]
                file.write(f"{b8},{b9},{b12},{b13},{b14},{b15},{b16},{b17},{b18},{b19}\n")
                logging.info(f"Rank: {b8}")
                logging.info(f"Title: {b9}")
                logging.info(f"Director: {b12}")
                logging.info(f"Actors: {b13}")
                logging.info(f"Year: {b14}")
                logging.info(f"Country: {b15}")
                logging.info(f"Categories: {b16}")
                logging.info(f"Score: {b17}")
                logging.info(f"Number: {b18}")
                logging.info(f"Comments: {b19}")
async def fonk2():
    b20 = asyncio.fonk2(fonk1())
    await b20
if b21 = = '__main__':
    b22 = time.time()
    asyncio.run(fonk2())
    b23 = time.time()
    logging.info(f"Total time consumed: {b23 - b22} s")