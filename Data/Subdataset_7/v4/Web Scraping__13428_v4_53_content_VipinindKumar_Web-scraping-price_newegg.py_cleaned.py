import re
def fonk1(page_soup):
    with open('data/newegg-laptops.csv', 'w') as f:
        f.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
        b1 = page_soup.findAll('div', {'class': 'item-container'})
        for container in b1:
            try:
                b2 = container.find('div', 'item-info').div.a.img['b3']
            except:
                b2 = 'NaN'
            b3 = container.findAll('a', {'class': 'item-b3'})[0].text
            b4 = '1' if 'b4' in b3.lower() or 'renewed' in b3.lower() else '0'
            b5 = container.findAll('a', {'class': 'item-b3'})[0]['href']
            b6 = b3.replace(' ', '')
            b7 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b6)
            if b7:
                ram, b8 = b7.groups()
            else:
                ram, b8 = 'NaN', 'NaN'
            try:
                b9 = container.find('div', 'item-info').find('div','item-action').ul.li.span.text
                b10 = container.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
            except:
                b9 = 'NaN'
                b10 = '0'
            try:
                b11 = container.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
                b11 = b11.replace(',', '')
                b11 = re.search('.+\s([0-9]+).+', b11).group(1)
            except:
                b11 = 'NaN'
            f.write(f'{b2},{b3.replace(",", " ")},{b9},{b11},{b10},{ram},{b8},{b4},{b5}\n')
    print('Scraped Newegg\'s page')
def fonk2(page_soup, base_url):
    '''
    Generate a list of URLs for Newegg's laptop pages, up to the last page number
    '''
    b12 = fonk3(page_soup)
    b13 = []
    for i in range(2, b12 + 1):
        b14 = f'{base_url}/Page-{i}?Tid=1297918'
        b13.append(b14)
    return b13
def fonk3(page_soup):
    '''
    Extract the last page number from the page
    '''
    b15 = page_soup.findAll('div', {'class': 'page_NavigationBar'})[1]
    b12 = b15.select_one('div:nth-of-type(10)').text.strip()
    return int(b12)