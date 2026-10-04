'''Python2.7'''
from bs4 import BeautifulSoup
import urllib2
import re
from pdf_read import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def fonk1(b12):
	b1 = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
		'Accept':'*/*',
		'Connection':'keep-alive',
		'Host':'www.plantcell.org'
	}
	b2 = urllib2.Request(b12,headers = b1)
	b3 = urllib2.urlopen(b2)
	b4 = b3.read().decode('utf-8')
	return b4
def fonk2(b4):
	b5 = BeautifulSoup(b4,'lxml')
	b6 = []
	for i in b5.find_all('p'):
		try:
			if u"p-" in str(i['id']):
				b7 = str(i)[(str(i).find(">") + 1):(str(i).find("</p>", str(i).find(">") + 1))]
				b7 = re.sub(r'<.*?>', '', str(b7))
				b7 = re.sub(r'\n', ' ', str(b7))
				b7 = re.sub(r' +', ' ', str(b7))
				if len(b7) > 250:
					b6.append(b7)
		except:
			pass
	a1 = 1
	b8 = []
	b9 = []
	for each in b5.find_all('li'):
		try:
			if 'last' in each['class'] and u'name' in str(each):
				b10 = each.find_all('a')[0].string
				b9.append(b10)
			elif 'aff' in each['class']:
				b11 = str(each.find_all('b11')[0])
				b11 = re.sub(r'<.*?>', '', str(b11))
				b11 = re.sub(r' +', ' ', str(b11))
				b11 = re.sub(r'\n', '', str(b11))
				if re.findall('[a-z]', b11[0]):
					b11 = b11[1:]
				b11 = (str(a1) + "\t" + b11 + "\n")
				b8.append(b11)
				a1 += 1
		except:
			pass
	if len(b6) > 2:
		print ("b7 error")
		b6 = []
		b8 = []
		b9 = []
	return ''.join(b6), ''.join(b9), ''.join(b8)
def fonk3(vol,page):
	b12 = "http:
	b4 = fonk1(b12)
	b7, b10, b11 = fonk2(b4)
	b13 = open((str(vol) + '-b7.csv'), 'a')
	b14 = open((str(vol) + '-b10.csv'), 'a')
	b15 = open((str(vol) + '-b11.csv'), 'a')
	if b7[-1] != "\n":
		b7 = b7 + "\n"
	if b10[-1] != "\n":
		b10 = b10 + "\n"
	if b11[-1] != "\n":
		b11 = b11 + "\n"
	b13.write(">" + str(page) + "\n" + b7)
	b14.write(">" + str(page) + "\n" + b10)
	b15.write(">" + str(page) + "\n" + b11)
if b16 = = "__main__":
	for iss in range(1,12):
		b17 = get_issues(iss)
		print ("vol:" + str(iss))
		for i in b17:
			print (i)
			try:
				fonk3(iss, i)
			except Exception, e:
				print (e)