import re
def fonk1(page_soup):
    with open('data/newegg-laptops.csv', 'w') as file:
        file.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
        b1 = page_soup.find_all('div', class_='item-container')
        for container in b1:
            b2 = container.find('div', class_='item-info').div.a.img.get('b3', 'NaN')
            b3 = container.find('a', class_='item-b3').text
            b4 = '1' if any(keyword in b3.lower() for keyword in ['b4', 'renewed']) else '0'
            b5 = container.find('a', class_='item-b3').get('href', '')
            ram, b6 = fonk2(b3)
            b11, b7 = fonk3(container)
            b8 = fonk4(container)
            file.write(f'{b2},{b3.replace(",", " ")},{b11},{b8},{b7},{ram},{b6},{b4},{b5}\n')
    print('Scraped Newegg\'s page')
def fonk2(b3):
    b9 = b3.replace(' ', '')
    b10 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b9)
    if b10:
        ram, b6 = b10.groups()
    else:
        ram, b6 = 'NaN', 'NaN'
    return ram, b6
def fonk3(container):
    try:
        b11 = container.find('div', class_='item-info').find('div', class_='item-action').ul.li.span.text
        b7 = container.find('div', class_='item-info').find('div', class_='item-action').ul.find('li', class_='price-save').find('span', class_='price-save-percent').text[:-1]
    except:
        b11 = 'NaN'
        b7 = '0'
    return b11, b7
def fonk4(container):
    try:
        b8 = container.find('div', class_='item-info').find('div', class_='item-action').ul.find('li', class_='price-current').text
        b8 = b8.replace(',', '')
        b8 = re.search('.+\s([0-9]+).+', b8).group(1)
    except:
        b8 = 'NaN'
    return b8
def fonk5(page_soup, base_url):
    '''
    Generate a list of URLs for Newegg's laptop pages, up to the last page number
    '''
    b12 = fonk6(page_soup)
    b13 = [f'{base_url}/Page-{i}?Tid=1297918' for i in range(2, b12 + 1)]
    return b13
def fonk6(page_soup):
    '''
    Extract the last page number from the page
    '''
    b14 = page_soup.find_all('div', class_='page_NavigationBar')[1]
    b12 = b14.select_one('div:nth-of-type(10)').text.strip()
    return int(b12)