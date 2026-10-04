import re
from datetime import datetime
import pandas as pd
class class1(Exception):
    pass
class class2(Exception):
    pass
class class3(Exception):
    pass
b1 = {}
b2 = {}
b3 = []
def fonk1(date_str):
    if re.match(r'^\d{1,2}\.\d{1,2}\.\d{4}$', date_str):
        b4 = datetime.strptime(date_str, '%d.%m.%Y')
    elif re.match(r'^\d{4}\-\d{1,2}\-\d{1,2}$', date_str):
        b4 = datetime.strptime(date_str, '%Y-%m-%d')
    elif re.match(r'^\d{4}\/\d{1,2}\/\d{1,2}$', date_str):
        b4 = datetime.strptime(date_str, '%Y/%m/%d')
    else:
        raise class2(f"Date format is not allowed: {date_str}")
    return b4.strftime("%Y-%m-%d")
def fonk2(file_name):
    global b2
    b2 = pd.read_csv(file_name)
    print("Portfolio loaded successfully.")
def fonk3():
    global b1
    print("All b1 loaded successfully.")
def fonk4(b5 = False):
    if b5:
        print("Trading strategy executed.")
def fonk5(b6, b5 = False):
    if b5:
        print(f"Portfolio valuated on {b6}.")
def fonk6():
    fonk2('portfolio0.csv')
    fonk3()
    fonk4(b5 = True)
    fonk5(b6 = "2018-03-13", b5=True)
if b7 = = '__main__':
    fonk6()