import csv
import string
from typing import List, Dict
def fonk1() -> List[Dict[str, str]]:
    b1 = input('Enter b1 (without .csv extension): ') + '.csv'
    b2 = []
    try:
        with open(b1, b3 = '') as file:
            b4 = csv.b4(file)
            next(b4)
            for row in b4:
                if len(row) >= 12:
                    b5 = {
                        'FIRST': row[2],
                        'LAST': row[4],
                        'POS': row[1],
                        'PRICE': row[6],
                        'TEAM': row[9],
                        'OPP': row[10],
                        'INJ': row[11]
                    }
                    b2.append(b5)
                else:
                    print(f"Warning: Skipping row with insufficient columns: {row}")
    except FileNotFoundError:
        print(f"Error: The file '{b1}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return b2
def fonk2(b2: List[Dict[str, str]]) -> List[Dict[str, str]]:
    b6 = str.maketrans('', '', string.punctuation)
    for b5 in b2:
        b5['FIRST'] = b5['FIRST'].translate(b6)
        b5['LAST'] = b5['LAST'].translate(b6)
    return b2
def fonk3():
    b7 = fonk1()
    if b7:
        b7 = fonk2(b7)
        for b5 in b7:
            print(b5)
if b8 = = "__main__":
    fonk3()