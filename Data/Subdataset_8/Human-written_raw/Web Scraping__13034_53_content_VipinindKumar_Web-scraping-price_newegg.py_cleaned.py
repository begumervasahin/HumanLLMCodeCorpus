import re
def newegg(page_soup):
	f =  open('data/newegg-laptops.csv', 'w')
	f.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
	conts = page_soup.findAll('div', {'class': 'item-container'})
	for cont in conts:
		try:
			brand = cont.find('div', 'item-info').div.a.img['title']
		except:
			brand = 'NaN'
		title = cont.findAll('a', {'class': 'item-title'})[0].text
		if ('refurbished' in title.lower()) or ('renewed' in title.lower()):
			refurb = '1'
		else:
			refurb = '0'
		link = cont.findAll('a', {'class': 'item-title'})[0]['href']
		features = title.replace(' ', '')
		features = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', features)
		try:
			ram = features.group(1)
			hdd = features.group(2)
		except:
			ram = 'NaN'
			hdd = 'NaN'
		try:
			pw = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text
			dc = d = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
		except:
			pw = 'NaN'
			dc = '0'
		try:
			pc = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
			pc = pc.replace(',', '')
			pc = re.search('.+\s([0-9]+).+', pc).group(1)
		except:
			pc = 'NaN'
		f.write(brand + ',' + title.replace(',', ' ')
		+ ',' + pw + ',' + pc + ',' + dc + ',' + ram + ',' + hdd + ',' + refurb + ',' + link + '\n')
	f.close()
	print('Scraped Newegg\'s page')
def eggUrls(page_soup, url):
	'''
	Extract the last page number from page_soup and create urls upto that page using predefined template of the newegg urls
	'''
	last = eggLast(page_soup)
	urls = list()
	for i in range(2, last+1):
		url = 'https:
		urls.append(url)
	return urls
def eggLast(page_soup):
	'''
	Return the last page number from the page
	'''
	last = page_soup.findAll('div', {'class': 'page_NavigationBar'})[1]
	last = last.select_one('div:nth-of-type(10)').text.strip()
	return int(last)