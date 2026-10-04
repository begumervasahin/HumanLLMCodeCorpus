import json
import numpy as np
import sys
from datetime import datetime
def fonk1(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The dates should be in the following format: YYYY-MM-DD")
def fonk2(b1):
    if len(b1) != 4:
        raise AssertionError("The number of arguments should be exactly 3.\n\n(Starting Date Ending Date Commodity Name)")
    fonk1(b1[1])
    fonk1(b1[2])
    if b1[3] not in ["gold", "silver"]:
        raise ValueError("The third argument must be either 'silver' or 'gold'")
def fonk3():
    b1 = sys.argv
    fonk2(b1)
    b2 = b1[3]
    b3 = b1[1]
    b4 = b1[2]
    with open('result.json', 'r') as fp:
        b5 = json.load(fp)
    b6 = list(b5[b2].b9())
    b7 = max(b6)
    b8 = min(b6)
    if b7 < b4:
        raise ValueError(f"Sorry! My maximum date is {b7}")
    if b8 > b3:
        raise ValueError(f"Sorry! My minimum date is {b8}")
    b9 = [key for key in b5[b2] if b3 <= key <= b4]
    b10 = [float(b5[b2][x]["Price"].replace(',', '')) for x in b9]
    print(b2, np.mean(b10), np.var(b10))
if b11 = = "__main__":
    fonk3()