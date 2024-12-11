import re
def fonk1(page_soup):
	b1 = open('data/newegg-laptops.csv', 'w')
	b1.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
	b2 = page_soup.findAll('div', {'class': 'item-container'})
	for cont in b2:
		try:
			b3 = cont.find('div', 'item-info').div.a.img['b4']
		except:
			b3 = 'NaN'
		b4 = cont.findAll('a', {'class': 'item-b4'})[0].text
		if ('refurbished' in b4.lower()) or ('renewed' in b4.lower()):
			b5 = '1'
		else:
			b5 = '0'
		b6 = cont.findAll('a', {'class': 'item-b4'})[0]['href']
		b7 = b4.replace(' ', '')
		b7 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b7)
		try:
			b8 = b7.group(1)
			b9 = b7.group(2)
		except:
			b8 = 'NaN'
			b9 = 'NaN'
		try:
			b10 = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text
			b11 = d = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
		except:
			b10 = 'NaN'
			b11 = '0'
		try:
			b12 = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
			b12 = b12.replace(',', '')
			b12 = re.search('.+\s([0-9]+).+', b12).group(1)
		except:
			b12 = 'NaN'
		b1.write(b3 + ',' + b4.replace(',', ' ')
		+ ',' + b10 + ',' + b12 + ',' + b11 + ',' + b8 + ',' + b9 + ',' + b5 + ',' + b6 + '\n')
	b1.close()
	print('Scraped Newegg\'s page')
def fonk2(page_soup, b15):
	'''
	Extract the b13 page number from page_soup and create b14 upto that page using predefined template of the newegg b14
	'''
	b13 = fonk3(page_soup)
	b14 = list()
	for i in range(2, b13+1):
		b15 = 'https:
		b14.append(b15)
	return b14
def fonk3(page_soup):
	'''
	Return the b13 page number from the page
	'''
	b13 = page_soup.findAll('div', {'class': 'page_NavigationBar'})[1]
	b13 = b13.select_one('div:nth-of-type(10)').text.strip()
	return int(b13)