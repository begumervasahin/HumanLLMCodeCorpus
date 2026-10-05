import csv
from bs4 import BeautifulSoup
def colorize_democrat_svg(democrat_data):
    '''Colorize the SVG map based on the data from the Democrat dictionary'''
    with open('counties.svg', 'r') as svg_file:
        svg_data = svg_file.read()
        soup = BeautifulSoup(svg_data, "html.parser")
        paths = soup.findAll('path')
        for path in paths:
            if path['id'] not in ["State_Lines", "separator"]:
                fips = path['id']
                if fips in democrat_data:
                    candidate = democrat_data[fips]
                    fill_color = get_democrat_color(candidate)
                    path['style'] = f'font-size:12px;fill-rule:nonzero;stroke:{fill_color}'
        with open('democrat_map.svg', mode='w') as out_svg:
            print(soup.prettify(), file=out_svg)
def colorize_republican_svg(republican_data):
    '''Colorize the SVG map based on the data from the Republican dictionary'''
    with open('counties.svg', 'r') as svg_file:
        svg_data = svg_file.read()
        soup = BeautifulSoup(svg_data, "html.parser")
        paths = soup.findAll('path')
        for path in paths:
            if path['id'] not in ["State_Lines", "separator"]:
                fips = path['id']
                if fips in republican_data:
                    candidate = republican_data[fips]
                    fill_color = get_republican_color(candidate)
                    path['style'] = f'font-size:12px;fill-rule:nonzero;stroke:{fill_color}'
        with open('republican_map.svg', mode='w') as out_svg:
            print(soup.prettify(), file=out_svg)
def get_democrat_color(candidate):
    '''Return color based on the Democrat candidate'''
    if candidate == 'Hillary Clinton':
        return '
    elif candidate == 'Bernie Sanders':
        return '
    else:
        return '
def get_republican_color(candidate):
    '''Return color based on the Republican candidate'''
    if candidate == 'Donald Trump':
        return '
    elif candidate == 'Ted Cruz':
        return '
    elif candidate == 'Marco Rubio':
        return '
    elif candidate == 'John Kasich':
        return '
    elif candidate == 'Ben Carson':
        return '
    else:
        return '
def read_from_csv_file():
    '''Read data from the CSV file and colorize the maps'''
    democrat_data = {}
    republican_data = {}
    with open('primary_results.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if len(row) < 7 or row[3] == 'fips':
                continue
            fips = row[3].strip('.0').zfill(5)
            candidate = row[5]
            party = row[4]
            if party == 'Democrat':
                democrat_data[fips] = candidate
            elif party == 'Republican':
                republican_data[fips] = candidate
    colorize_democrat_svg(democrat_data)
    colorize_republican_svg(republican_data)
def main():
    '''Main function'''
    read_from_csv_file()
if __name__ == '__main__':
    main()