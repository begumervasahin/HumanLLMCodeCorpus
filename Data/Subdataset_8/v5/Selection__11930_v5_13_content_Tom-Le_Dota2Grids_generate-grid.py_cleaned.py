from bs4 import BeautifulSoup
import urllib2
import json
import argparse
USER_AGENT = 'Dota2GridBot9000'
STAT_SOURCES = {
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
NAME_COLUMN_INDEX = 1
class DotabuffStatsScraper:
    def __init__(self, url, keys):
        self.stats = {}
        try:
            request = urllib2.Request(url=url, headers={'User-Agent': USER_AGENT})
            response = urllib2.urlopen(request)
            document = BeautifulSoup(response, "lxml")
            if document.table is None:
                raise ValueError("Unable to scrape data from page: Table not found.")
            for row in document.table.tbody.find_all('tr'):
                data = {}
                cols = row.find_all('td')
                hero_name = cols[NAME_COLUMN_INDEX].strings.next()
                for key_name, key_index in keys:
                    data[key_name] = cols[key_index]['data-value']
                self.stats[hero_name] = data
        except Exception as e:
            raise ValueError("Unable to scrape data from page: " + str(e))
    def get_stats(self, hero, key):
        hero_name = hero['localized_name']
        if hero_name in self.stats and key in self.stats[hero_name]:
            return self.stats[hero_name][key]
        return None
def get_heroes_list(api_key):
    try:
        qkey = urllib2.quote(api_key)
        url = 'http:
        request = urllib2.Request(url=url, headers={'User-Agent': USER_AGENT})
        response = urllib2.urlopen(request)
        data = json.load(response)
        return data['result']['heroes']
    except Exception as e:
        raise ValueError("Failed to fetch heroes list: " + str(e))
def generate_grid(heroes, ratio='16:9'):
    ratios = {
        '16:9': (0.390228, 0, 51, 51, 19),
        '4:3': (0.34848, 0, 50, 55, 20),
        '16:10': (0.390228, 0, 54, 54, 20)
    }
    if ratio not in ratios:
        raise ValueError("Invalid ratio.")
    scale, startXPos, startYPos, iconWidth, iconHeight, numCol = ratios[ratio]
    layout_lines = ['"fulldeck_layout.txt"', '{']
    xPos, yPos = startXPos, startYPos
    col = 0
    for index, hero in enumerate(heroes):
        layout_lines.append('\t"{}"'.format(index))
        layout_lines.append('\t{')
        layout_lines.append('\t\t"HeroID"\t"{}"'.format(hero['id']))
        layout_lines.append('\t\t"x"\t"{}"'.format(xPos))
        layout_lines.append('\t\t"y"\t"{}"'.format(yPos))
        layout_lines.append('\t\t"scale"\t"{}"'.format(scale))
        layout_lines.append('\t\t"zpos"\t"100"')
        layout_lines.append('\t}')
        col += 1
        if col > numCol:
            xPos = startXPos
            yPos += iconHeight
            col = 0
        else:
            xPos += iconWidth
    layout_lines.append('}')
    return '\n'.join(layout_lines)
def main():
    parser = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    parser.add_argument('key', help='Your Steam WebAPI key.')
    parser.add_argument('stat', choices=STAT_SOURCES.keys(), help='Stat to sort heroes.')
    parser.add_argument('out', help='Path to output file.')
    parser.add_argument('--date', default='month', help='Date parameter to pass to Dotabuff.')
    parser.add_argument('--reverse', action='store_false', help='Sort from smallest to largest, instead of largest to smallest.')
    args = parser.parse_args()
    heroes = get_heroes_list(api_key=args.key)
    source = STAT_SOURCES[args.stat]
    url = source[0] + '?date=' + urllib2.quote(args.date)
    column = source[1]
    try:
        buff = DotabuffStatsScraper(url=url, keys=[(args.stat, column)])
        sorted_heroes = sorted(heroes, key=lambda hero: float(buff.get_stats(hero, args.stat)), reverse=args.reverse)
        with open(args.out, 'w') as output_fp:
            output_fp.write(generate_grid(sorted_heroes))
    except Exception as e:
        print("Error:", e)
if __name__ == '__main__':
    main()