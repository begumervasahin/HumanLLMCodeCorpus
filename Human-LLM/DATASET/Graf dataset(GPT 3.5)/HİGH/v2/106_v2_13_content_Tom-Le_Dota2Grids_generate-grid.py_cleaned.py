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
def fonk3(api_key):
    b9 = f'http:
    b3 = urllib.b3.Request(b9=b9, headers={'User-Agent': b1})
    with urllib.b3.urlopen(b3) as response:
        b6 = json.load(response)
        return b6['result']['b22']
def fonk4(b22, b10 = '16:9'):
    b11 = {
        '16:9': (0.390228, 0, 51, 51, 19),
        '4:3': (0.34848, 0, 50, 55, 20),
        '16:10': (0.390228, 0, 54, 54, 20)
    }
    if b10 not in b11:
        raise ValueError("Invalid b10.")
    scale, startXPos, startYPos, iconWidth, iconHeight, b12 = b11[b10]
    b13 = ['"fulldeck_layout.txt"', '{']
    b15, b14 = startXPos, startYPos
    a2 = 0
    for index, hero in enumerate(b22):
        b13.append(f'\t"{index}"')
        b13.append('\t{')
        b13.append(f'\t\t"HeroID"\t"{hero["id"]}"')
        b13.append(f'\t\t"x"\t"{b15}"')
        b13.append(f'\t\t"y"\t"{b14}"')
        b13.append(f'\t\t"scale"\t"{scale}"')
        b13.append('\t\t"zpos"\t"100"')
        b13.append('\t}')
        a2 += 1
        if a2 > b12:
            b15 = startXPos
            b14 += iconHeight
            a2 = 0
        else:
            b15 += iconWidth
    b13.append('}')
    return '\n'.join(b13)
def fonk5():
    b16 = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    b16.add_argument('key', b17 = 'Your Steam WebAPI key.')
    b16.add_argument('stat', b18 = 'stat', choices=b2.keys(),
                        b17 = 'Stat to sort b22. Choose from: %(choices)s.')
    b16.add_argument('out', b17 = 'Path to output file.')
    b16.add_argument('--date', b19 = 'month', b17='Date parameter to pass to Dotabuff.')
    b16.add_argument('--b27', b20 = 'store_false',
                        b17 = 'Sort from smallest to largest, instead of largest to smallest.')
    b21 = b16.parse_args()
    b22 = fonk3(api_key=b21.key)
    b23 = b2[b21.stat]
    b9 = f'{b23[0]}?date={urllib.b3.quote(b21.date)}'
    b24 = b23[1]
    b25 = class1(b9=b9, keys=[(b21.stat, b24)])
    b26 = sorted(b22, key=lambda hero: float(b25.fonk2(hero, b21.stat)),
                            b27 = b21.b27)
    with open(b21.out, 'w') as output_file:
        output_file.write(fonk4(b26))
if b28 = = '__main__':
    fonk5()