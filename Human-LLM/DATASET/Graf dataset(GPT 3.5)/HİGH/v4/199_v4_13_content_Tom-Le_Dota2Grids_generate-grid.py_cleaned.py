from bs4 import BeautifulSoup
import urllib2
import json
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
    def fonk1(self, b26, keys):
        b3 = urllib2.Request(b26=b26, b11={'User-Agent': b1})
        b4 = urllib2.urlopen(b3)
        b5 = BeautifulSoup(b4, "lxml")
        if b5.table is None:
            raise ValueError("Unable to scrape b7 from page: Table not found.")
        self.b6 = {}
        for row in b5.table.tbody.find_all('tr'):
            b7 = {}
            b8 = row.find_all('td')
            try:
                b9 = b8[a1].strings.next()
                for key_name, key_index in keys:
                    b7[key_name] = b8[key_index]['b7-value']
            except IndexError:
                raise ValueError("Unable to scrape b7 from page: Cannot read row.")
            self.b6[b9] = b7
    def fonk2(self, hero, b31):
        b9 = hero['localized_name'];
        if b9 in self.b6:
            if b31 in self.b6[b9]:
                return self.b6[b9][b31]
        return None
def fonk3(b31):
    b10 = urllib2.quote(b31)
    b3 = urllib2.Request(b26='http:
                              b11 = {'User-Agent': b1})
    try:
        b4 = urllib2.urlopen(b3)
    except urllib2.HTTPError as e:
        if e.b12 = = 403:
            raise ValueError("Key " + b31 + " was not accepted as a valid")
        else:
            raise e
    b7 = json.load(b4)
    return b7['result']['b24']
def fonk4(b24, b13 = '16:9'):
    if b13 = = '16:9':
        a2 = 0.390228
        a3 = 0
        a4 = 51
        a5 = 51
        a6 = 51
        a7 = 19
    elif b13 = = '4:3':
        a2 = 0.34848
        a3 = 0
        a4 = 50
        a5 = 55
        a6 = 55
        a7 = 20
    elif b13 = = '16:10':
        a2 = 0.390228
        a3 = 0
        a4 = 54
        a5 = 54
        a6 = 54
        a7 = 20
    else:
        raise ValueError("Invalid b13.")
    b14 = []
    b14.append('"fulldeck_layout.txt"')
    b14.append('{')
    b16, b15 = a3, a4
    a8 = 0
    for index, hero in enumerate(b24):
        b14.append('\t"{}"'.format(index))
        b14.append('\t{')
        b14.append('\t\t"HeroID"\t"{}"'.format(hero['id']))
        b14.append('\t\t"x"\t"{}"'.format(b16))
        b14.append('\t\t"y"\t"{}"'.format(b15))
        b14.append('\t\t"a2"\t"{}"'.format(a2))
        b14.append('\t\t"zpos"\t"100"')
        b14.append('\t}')
        a8 += 1
        if a8 > a7:
            b16 = a3
            b15 += a6
            a8 = 0
        else:
            b16 += a5
    b14.append('}')
    return '\n'.join(b14)
def fonk5():
    import argparse
    b17 = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    b17.add_argument('b31',
                        b18 = 'Your Steam WebAPI b31.')
    b17.add_argument('b27',
                        b19 = 'b27',
                        b20 = b2.keys(),
                        b18 = 'Stat to sort b24.')
    b17.add_argument('out',
                        b18 = 'Path to output file.')
    b17.add_argument('--date',
                        b21 = 'month',
                        b18 = 'Date parameter to pass to Dotabuff.')
    b17.add_argument('--b32',
                        b22 = 'store_false',
                        b18 = 'Sort from smallest to largest, instead of largest to smallest.')
    b23 = b17.parse_args()
    b24 = fonk3(b31=b23.b31)
    b25 = b2[b23.b27]
    b26 = b25[0] + '?date=' + urllib2.quote(b23.date)
    b27 = b23.b27
    b28 = b25[1]
    b29 = class1(b26=b26, keys=[(b23.b27, b28)])
    b30 = sorted(b24,
                     b31 = lambda hero: float(b29.fonk2(hero, b23.b27)),
                     b32 = b23.b32)
    with open(b23.out, 'w') as output_fp:
        output_fp.write(fonk4(b30))
if b33 = = '__main__':
    fonk5()