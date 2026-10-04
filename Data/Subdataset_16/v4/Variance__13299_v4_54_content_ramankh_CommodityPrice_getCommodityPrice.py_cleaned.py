import json
import numpy as np
import sys
from datetime import datetime
def fonk1(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The dates should be in the following format: YYYY-MM-DD")
def fonk2(args):
    if len(args) != 4:
        raise AssertionError("The number of arguments should be exactly 3: Starting Date, Ending Date, and Commodity Name")
    fonk1(args[1])
    fonk1(args[2])
    if args[3] not in ["gold", "silver"]:
        raise ValueError("The third argument must be either 'silver' or 'gold'")
def fonk3(b1 = 'result.json'):
    with open(b1, 'r') as fp:
        return json.load(fp)
def fonk4(b7, b8, b9, b10):
    b2 = list(b10[b9].b5())
    b3 = max(b2)
    b4 = min(b2)
    if b3 < b8:
        raise ValueError(f"Sorry! My maximum date is {b3}")
    if b4 > b7:
        raise ValueError(f"Sorry! My minimum date is {b4}")
def fonk5(b7, b8, b9, b10):
    b5 = [key for key in b10[b9] if b7 <= key <= b8]
    b6 = [float(b10[b9][x]["Price"].replace(',', '')) for x in b5]
    return np.mean(b6), np.var(b6)
def fonk6(args):
    fonk2(args)
    b7 = args[1]
    b8 = args[2]
    b9 = args[3]
    b10 = fonk3()
    fonk4(b7, b8, b9, b10)
    mean_price, b11 = fonk5(b7, b8, b9, b10)
    print(b9, mean_price, b11)
if b12 = = "__main__":
    fonk6(sys.argv)