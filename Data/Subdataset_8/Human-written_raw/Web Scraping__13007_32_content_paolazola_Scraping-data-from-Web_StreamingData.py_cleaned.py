
def Yahoo_realTime(ticker,finish_time,delta):
    import datetime
    import time
    import pandas as pd
    import requests
    from lxml import html
    from random import uniform
    url  = 'https:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    list_values=[]
    list_timeNow=[]
    list_timeYahoo=[]
    while datetime.datetime.now() < finish_time:
        page = requests.get(url,headers = headers)
        time.sleep(uniform(2,3))
        parser = html.fromstring(page.content)
        value=parser.xpath('
        yahooTime=parser.xpath('
        list_values.append(value)
        list_timeNow.append(datetime.datetime.now())
        list_timeYahoo.append(yahooTime)
        time.sleep(delta*60)
    dataframe=pd.DataFrame({'scraperTime':list_timeNow,'quotes':list_values,
                            'YahooPriceTime':list_timeYahoo})
    return(dataframe)