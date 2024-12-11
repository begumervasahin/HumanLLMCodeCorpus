import re
import logging
import asyncio
import time
import aiohttp
logging.basicConfig(b1 = logging.INFO, format="%(asctime)s %(levelname)-8s: %(message)s")
b2 = {'User-Agent': 'Mozilla/5.0'}
async def fonk1(session, page):
    b3 = f"https:
    async with session.get(b3, b2 = b2) as response:
        return await response.text()
async def fonk2(b10, file):
    b4 = re.compile(r'<em class="">(.*?)</em>.*?<img width="100" alt="(.*?)" src=".*?" class="">.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)äººè¯ä»·</span>.*?<span class="inq">(.*?)</span>', re.S)
    b5 = re.findall(b4, b10)
    for i in b5:
        rank, title, text, score, number, b6 = i[0], i[1], i[2].replace("\n                            ", " ").replace("&nbsp;&nbsp;&nbsp;", " ").replace("&nbsp;", " ").replace("\n                        ", " "), i[3], i[4], i[5]
        b7 = text.split(" ")
        director, actors, year, country, b8 = b7[0], b7[1], b7[2], b7[3], b7[-1]
        file.write(f"{rank},{title},{director},{actors},{year},{country},{b8},{score},{number},{b6}\n")
        logging.info(f"rank: {rank}, title: {title}, director: {director}, actors: {actors}, year: {year}, country: {country}, b8: {b8}, score: {score}, number: {number}, b6: {b6}")
async def fonk3():
    async with aiohttp.ClientSession() as session:
        async with open('douban_top250.txt', 'a', b9 = 'utf-8') as file:
            file.write('Rank,Title,Director,Actors,Year,Country,Categories,Score,Number,Comments\n')
            for page in range(0, 250, 25):
                b10 = await fonk1(session, page)
                logging.info(f"page is {page}")
                logging.info(f"len(b5) is {len(b10)}")
                await fonk2(b10, file)
async def fonk4():
    b11 = time.time()
    await fonk3()
    b12 = time.time()
    logging.info(f"Total time consumed: {b12 - b11} s")
if b13 = = '__main__':
    asyncio.run(fonk4())