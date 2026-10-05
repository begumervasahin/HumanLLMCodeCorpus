import csv
from bs4 import BeautifulSoup
def colorize_svg(svg_file, data_dictionary, party):
    style_description = 'font-size:12px;fill-rule:nonzero;stroke:'
    fill_colors = {
        'Democrat': {'Hillary Clinton': '
        'Republican': {'Donald Trump': '
                       'John Kasich': '
    }
    with open(svg_file, 'r') as fin:
        svg_data = fin.read()
        soup = BeautifulSoup(svg_data, "html.parser")
        paths = soup.findAll('path')
        for p in paths:
            if p['id'] not in ["State_Lines", "separator"]:
                fips_key = p['id']
                candidate = data_dictionary.get(fips_key, 'Other')
                fill_color = fill_colors[party].get(candidate, fill_colors[party]['Other'])
                p['style'] = style_description + fill_color
        with open(f'{party.lower()}_map.svg', mode='w') as out_svg:
             print(soup.prettify(), file=out_svg)
def read_from_csv_file():
    dict_democrat = {}
    dict_republican = {}
    with open('primary_results.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if len(row[3]) > 7 or row[3] == 'fips':
                continue
            fips, party_name, candidate_name, num_votes = row[3], row[4], row[5], row[6]
            if fips not in dict_democrat and fips not in dict_republican:
                if party_name == 'Republican':
                    dict_republican[fips] = candidate_name
                elif party_name == 'Democrat':
                    dict_democrat[fips] = candidate_name
            elif fips in dict_democrat and party_name == 'Democrat':
                if int(num_votes) > int(dict_democrat[fips][1]):
                    dict_democrat[fips] = (candidate_name, num_votes)
            elif fips in dict_republican and party_name == 'Republican':
                if int(num_votes) > int(dict_republican[fips][1]):
                    dict_republican[fips] = (candidate_name, num_votes)
    colorize_svg('counties.svg', dict_democrat, 'Democrat')
    colorize_svg('counties.svg', dict_republican, 'Republican')
def main():
    read_from_csv_file()
if __name__ == '__main__':
    main()