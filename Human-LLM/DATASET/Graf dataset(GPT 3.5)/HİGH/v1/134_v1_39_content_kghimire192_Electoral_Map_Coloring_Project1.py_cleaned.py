import csv
from bs4 import BeautifulSoup
def fonk1(democrat_dictionary):
    '''Colorize the svg map based on the data from the democrat dictionary that has the winning candidate name in each county'''
    b1 = ''
    b2 = 'font-size:12px;fill-rule:nonzero;stroke:'
    with open('counties.svg', 'r') as fin:
        b3 = fin.read()
        b4 = BeautifulSoup(b3, "html.parser")
        b5 = b4.findAll('path')
        for p in b5:
            if p['id'] not in ["State_Lines", "separator"]:
                for fips_key in democrat_dictionary:
                    if p['id'] == fips_key:
                        if democrat_dictionary[fips_key] == 'Hillary Clinton':
                            b1 = '
                        elif democrat_dictionary[fips_key] == 'Bernie Sanders':
                            b1 = '
                        else:
                            b1 = '
                        p['style'] = b2 + b1
                    else:
                        continue
        with open('democrat_map.svg', b6 = 'w') as out_svg:
             print(b4.prettify(), b7 = out_svg)
def fonk2(republican_dictionary):
    '''Colorize the svg map based on the data from the republican dictionary that has the winning candidate name in each county'''
    b1 = ''
    b2 = 'font-size:12px;fill-rule:nonzero;stroke:'
    with open('counties.svg', 'r') as fin:
        b3 = fin.read()
        b4 = BeautifulSoup(b3, "html.parser")
        b5 = b4.findAll('path')
        for p in b5:
            if p['id'] not in ["State_Lines", "separator"]:
                for fips_key in republican_dictionary:
                    if p['id'] == fips_key:
                        if republican_dictionary[fips_key] == 'Donald Trump':
                            b1 = '
                        elif republican_dictionary[fips_key] == 'Ted Cruz':
                            b1 = '
                        elif republican_dictionary[fips_key] == 'Marco Rubio':
                            b1 = '
                        elif republican_dictionary[fips_key] == 'John Kasich':
                            b1 = '
                        elif republican_dictionary[fips_key] == 'Ben Carson':
                            b1 = '
                        else:
                            b1 = '
                        p['style'] = b2 + b1
                    else:
                        continue
        with open('republican_map.svg', b6 = 'w') as out_svg:
            print(b4.prettify(), b7 = out_svg)
def fonk3():
    '''A function that reads from the given csv b7, creates dictionaries for both republican and democratic party with
    b8 as the key and winning candidate name as the value. The function then calls two functions sending corresponding
    dictionaries as arguments'''
    b8 = ''
    b9 = ''
    b10 = ''
    b11 = ''
    b12 = {}
    b13 = {}
    with open('primary_results.csv', b14 = '') as csvfile:
        b15 = csv.b15(csvfile, delimiter=",")
        for row in b15:
            if len(row) < 7:
                continue
            if row[3] == 'b8':
                continue
            if (b8 = = ''):
                b8 = row[3]
                b11 = row[6]
                b10 = row[5]
                b9 = row[4]
            elif b8 = = row[3] and b9 == row[4]:
                if int(b11) < int(row[6]):
                    b11 = row[6]
                    b10 = row[5]
            elif b8 != row[3] and b8 != '':
                b8 = b8.strip('.0')
                if len(b8) < 5:
                    b8 = '0'*(5 - len(b8)) + b8
                if b9 = = 'Republican':
                   b13[b8] = b10
                elif b9 = = 'Democrat':
                    b12[b8] = b10
                b8 = row[3]
                b11 = row[6]
                b10 = row[5]
                b9 = row[4]
    fonk1(b12)
    fonk2(b13)
def fonk4():
    '''The fonk4() function'''
    fonk3()
if b16 = = '__main__':
    fonk4()