import argparse
import json
import urllib.b3
from bs4 import BeautifulSoup
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
class class1:
    a1 = 1
    def fonk1(self, b9, keys):
        b3 = urllib.b3.Request(b9=b9, headers={'User-Agent': b1})
        with urllib.b3.urlopen(b3) as response:
            b4 = BeautifulSoup(response, "lxml")
            if b4.table is None:
                raise ValueError("Unable to scrape b6 from page: Table not found.")
            self.b5 = {}
            for row in b4.table.tbody.find_all('tr'):
                b6 = {}
                b7 = row.find_all('td')
                try:
                    b8 = next(b7[self.a1].strings)
                    for key_name, key_index in keys:
                        b6[key_name] = b7[key_index]['b6-value']
                except IndexError:
                    raise ValueError("Unable to scrape b6 from page: Cannot read row.")
                self.b5[b8] = b6
    def fonk2(self, hero, key):
        b8 = hero['localized_name']
        if b8 in self.b5:
            if key in self.b5[b8]:
                return self.b5[b8][key]
        return None
def fonk3(key):
    b9 = f'http:
    b3 = urllib.b3.Request(b9=b9, headers={'User-Agent': b1})
    with urllib.b3.urlopen(b3) as response:
        b6 = json.load(response)
        return b6['result']['b20']
def fonk4(b20, b10 = '16:9'):
    if b10 = = '16:9':
        a2 = 0.390228
        a3 = 0
        a4 = 51
        a5 = 51
        a6 = 51
        a7 = 19
    elif b10 = = '4:3':
        a2 = 0.34848
        a3 = 0
        a4 = 50
        a5 = 55
        a6 = 55
        a7 = 20
    elif b10 = = '16:10':
        a2 = 0.390228
        a3 = 0
        a4 = 54
        a5 = 54
        a6 = 54
        a7 = 20
    else:
        raise ValueError("Invalid b10.")
    b11 = []
    b11.append('"fulldeck_layout.txt"')
    b11.append('{')
    b13, b12 = a3, a4
    a8 = 0
    for index, hero in enumerate(b20):
        b11.append(f'\t"{index}"')
        b11.append('\t{')
        b11.append(f'\t\t"HeroID"\t"{hero["id"]}"')
        b11.append(f'\t\t"x"\t"{b13}"')
        b11.append(f'\t\t"y"\t"{b12}"')
        b11.append(f'\t\t"a2"\t"{a2}"')
        b11.append('\t\t"zpos"\t"100"')
        b11.append('\t}')
        a8 += 1
        if a8 > a7:
            b13 = a3
            b12 += a6
            a8 = 0
        else:
            b13 += a5
    b11.append('}')
    return '\n'.join(b11)
def fonk5():
    b14 = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    b14.add_argument('key', b15 = 'Your Steam WebAPI key.')
    b14.add_argument('b22', b16 = 'b22', choices=b2.keys(),
                        b15 = 'Stat to sort b20. Choose from: %(choices)s.')
    b14.add_argument('out', b15 = 'Path to output file.')
    b14.add_argument('--date', b17 = 'month', b15='Date parameter to pass to Dotabuff.')
    b14.add_argument('--b26', b18 = 'store_false',
                        b15 = 'Sort from smallest to largest, instead of largest to smallest.')
    b19 = b14.parse_args()
    b20 = fonk3(key=b19.key)
    b21 = b2[b19.b22]
    b9 = f'{b21[0]}?date={urllib.b3.quote(b19.date)}'
    b22 = b19.b22
    b23 = b21[1]
    b24 = class1(b9=b9, keys=[(b19.b22, b23)])
    b25 = sorted(b20, key=lambda hero: float(b24.fonk2(hero, b19.b22)),
                     b26 = b19.b26)
    with open(b19.out, 'w') as output_fp:
        output_fp.write(fonk4(b25))
if b27 = = '__main__':
    fonk5()