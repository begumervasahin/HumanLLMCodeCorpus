import csv
from bs4 import BeautifulSoup
def colorize_svg_map(data, output_file):
    '''Colorize the SVG map based on the provided data'''
    with open('counties.svg', 'r') as svg_file:
        svg_data = svg_file.read()
        soup = BeautifulSoup(svg_data, "html.parser")
        paths = soup.findAll('path')
        for path in paths:
            if path['id'] not in ["State_Lines", "separator"]:
                fips = path['id']
                if fips in data:
                    candidate = data[fips]
                    fill_color = get_candidate_color(candidate)
                    path['style'] = f'font-size:12px;fill-rule:nonzero;stroke:{fill_color}'
        with open(output_file, mode='w') as out_svg:
            print(soup.prettify(), file=out_svg)
def get_candidate_color(candidate):
    '''Return color based on the candidate'''
    colors = {
        'Hillary Clinton': '
        'Bernie Sanders': '
        'Donald Trump': '
        'Ted Cruz': '
        'Marco Rubio': '
        'John Kasich': '
        'Ben Carson': '
    }
    return colors.get(candidate, '
def read_data_from_csv(csv_file):
    '''Read data from the CSV file and return dictionaries for Democrat and Republican data'''
    democrat_data = {}
    republican_data = {}
    with open(csv_file, newline='') as csvfile:
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
    return democrat_data, republican_data
def main():
    '''Main function'''
    democrat_data, republican_data = read_data_from_csv('primary_results.csv')
    colorize_svg_map(democrat_data, 'democrat_map.svg')
    colorize_svg_map(republican_data, 'republican_map.svg')
if __name__ == '__main__':
    main()