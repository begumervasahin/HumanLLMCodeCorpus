from bs4 import BeautifulSoup
import urllib2
import json
import argparse
b1 = 'Dota2GridBot9000'
b2 = {
    'cs@10': ('http:
    'cd@10': ('http:
    'gpm': ('http:
    'xpm': ('http:
    'kda': ('http:
    'wr': ('http:
    'pr': ('http:
    'hdpm': ('http:
    'tdpm': ('http:
    'hhpm': ('http:
}
a1 = 1
class class1:
    def fonk1(self, b11, keys):
        self.b3 = {}
        try:
            b4 = urllib2.Request(b11=b11, headers={'User-Agent': b1})
            b5 = urllib2.urlopen(b4)
            b6 = BeautifulSoup(b5, "lxml")
            if b6.table is None:
                raise ValueError("Unable to scrape b7 from page: Table not found.")
            for row in b6.table.tbody.find_all('tr'):
                b7 = {}
                b8 = row.find_all('td')
                b9 = b8[a1].strings.next()
                for key_name, key_index in keys:
                    b7[key_name] = b8[key_index]['b7-value']
                self.b3[b9] = b7
        except Exception as e:
            raise ValueError("Unable to scrape b7 from page: " + str(e))
    def fonk2(self, hero, key):
        b9 = hero['localized_name']
        if b9 in self.b3 and key in self.b3[b9]:
            return self.b3[b9][key]
        return None
def fonk3(api_key):
    try:
        b10 = urllib2.quote(api_key)
        b11 = 'http:
        b4 = urllib2.Request(b11=b11, headers={'User-Agent': b1})
        b5 = urllib2.urlopen(b4)
        b7 = json.load(b5)
        return b7['result']['b24']
    except Exception as e:
        raise ValueError("Failed to fetch b24 list: " + str(e))
def fonk4(b24, b12 = '16:9'):
    b13 = {
        '16:9': (0.390228, 0, 51, 51, 19),
        '4:3': (0.34848, 0, 50, 55, 20),
        '16:10': (0.390228, 0, 54, 54, 20)
    }
    if b12 not in b13:
        raise ValueError("Invalid b12.")
    scale, startXPos, startYPos, iconWidth, iconHeight, b14 = b13[b12]
    b15 = ['"fulldeck_layout.txt"', '{']
    b17, b16 = startXPos, startYPos
    a2 = 0
    for index, hero in enumerate(b24):
        b15.append('\t"{}"'.format(index))
        b15.append('\t{')
        b15.append('\t\t"HeroID"\t"{}"'.format(hero['id']))
        b15.append('\t\t"x"\t"{}"'.format(b17))
        b15.append('\t\t"y"\t"{}"'.format(b16))
        b15.append('\t\t"scale"\t"{}"'.format(scale))
        b15.append('\t\t"zpos"\t"100"')
        b15.append('\t}')
        a2 += 1
        if a2 > b14:
            b17 = startXPos
            b16 += iconHeight
            a2 = 0
        else:
            b17 += iconWidth
    b15.append('}')
    return '\n'.join(b15)
def fonk5():
    b18 = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    b18.add_argument('key', b19 = 'Your Steam WebAPI key.')
    b18.add_argument('stat', b20 = b2.keys(), b19='Stat to sort b24.')
    b18.add_argument('out', b19 = 'Path to output file.')
    b18.add_argument('--date', b21 = 'month', b19='Date parameter to pass to Dotabuff.')
    b18.add_argument('--reverse', b22 = 'store_false', b19='Sort from smallest to largest, instead of largest to smallest.')
    b23 = b18.parse_args()
    b24 = fonk3(api_key=b23.key)
    b25 = b2[b23.stat]
    b11 = b25[0] + '?date=' + urllib2.quote(b23.date)
    b26 = b25[1]
    try:
        b27 = class1(b11=b11, keys=[(b23.stat, b26)])
        b28 = sorted(b24, key=lambda hero: float(b27.fonk2(hero, b23.stat)), reverse=b23.reverse)
        with open(b23.out, 'w') as output_fp:
            output_fp.write(fonk4(b28))
    except Exception as e:
        print("Error:", e)
if b29 = = '__main__':
    fonk5()