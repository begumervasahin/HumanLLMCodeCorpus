
from bs4 import BeautifulSoup
import urllib2, json
user_agent = 'Dota2GridBot9000'
stat_sources = {
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
class DotabuffStatsScraper:
    NAME_COLUMN_INDEX = 1
    def __init__(self, url, keys):
        request = urllib2.Request(url=url, headers={'User-Agent' : user_agent})
        response = urllib2.urlopen(request)
        document = BeautifulSoup(response, "lxml")
        if document.table == None:
            raise ValueError("Unable to scrape data from page: Table not found.")
        self.stats = {}
        for row in document.table.tbody.find_all('tr'):
            data = {}
            cols = row.find_all('td')
            try:
                hero_name = cols[self.NAME_COLUMN_INDEX].strings.next()
                for key_name, key_index in keys:
                    data[key_name] = cols[key_index]['data-value']
            except IndexError:
                raise ValueError("Unable to scrape data from page: Cannot read row.")
            self.stats[hero_name] = data
    def get_stats(self, hero, key):
        hero_name = hero['localized_name'];
        if hero_name in self.stats:
            if key in self.stats[hero_name]:
                return self.stats[hero_name][key]
        return None
def get_heroes_list(key):
    qkey = urllib2.quote(key)
    request = urllib2.Request(url='http:
                              headers={'User-Agent' : user_agent})
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
        if e.code == 403:
            raise ValueError("Key " + key + " was not accepted as a valid")
        else:
            raise e
    data = json.load(response)
    return data['result']['heroes']
def generate_grid(heroes, ratio='16:9'):
    if ratio == '16:9':
        scale = 0.390228
        startXPos = 0
        startYPos = 51
        iconWidth = 51
        iconHeight = 51
        numCol = 19
    elif ratio == '4:3':
        scale = 0.34848
        startXPos = 0
        startYPos = 50
        iconWidth = 55
        iconHeight = 55
        numCol = 20
    elif ratio == '16:10':
        scale = 0.390228
        startXPos = 0
        startYPos = 54
        iconWidth = 54
        iconHeight = 54
        numCol = 20
    else:
        raise ValueError("Invalid ratio.")
    layout_lines = []
    layout_lines.append('"fulldeck_layout.txt"')
    layout_lines.append('{')
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
    import argparse
    parser = argparse.ArgumentParser(description='Generate sorted grid layouts for Dota 2!')
    parser.add_argument('key',
                        help='Your Steam WebAPI key.')
    parser.add_argument('stat',
                        metavar='stat',
                        choices=stat_sources.keys(),
                        help='Stat to sort heroes. Choose from: %(choices)s.')
    parser.add_argument('out',
                        help='Path to output file.')
    parser.add_argument('--date',
                        default='month',
                        help='Date parameter to pass to Dotabuff.')
    parser.add_argument('--reverse',
                        action='store_false',
                        help='Sort from smallest to largest, instead of largest to smallest.')
    args = parser.parse_args()
    heroes = get_heroes_list(key=args.key)
    source = stat_sources[args.stat]
    url = source[0] + '?date=' + urllib2.quote(args.date)
    stat = args.stat
    column = source[1]
    buff = DotabuffStatsScraper(url=url, keys=[(args.stat, column)])
    sheroes = sorted(heroes,
                     key=lambda hero: float(buff.get_stats(hero, args.stat)),
                     reverse=args.reverse)
    with open(args.out, 'w') as output_fp:
        output_fp.write(generate_grid(sheroes))
if __name__ == '__main__':
    main()