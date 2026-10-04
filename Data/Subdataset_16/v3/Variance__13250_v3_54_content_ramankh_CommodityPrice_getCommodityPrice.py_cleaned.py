import json
import numpy as np
import sys
from datetime import datetime
def fonk1(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Date format should be YYYY-MM-DD.")
def fonk2(b5):
    if len(b5) != 4:
        raise AssertionError("Exactly 3 arguments required: Starting Date, Ending Date, Commodity Name.")
    fonk1(b5[1])
    fonk1(b5[2])
    if b5[3] not in ["gold", "silver"]:
        raise ValueError("Commodity name must be either 'gold' or 'silver'.")
def fonk3(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def fonk4(b9, b6, b7, b8):
    b1 = list(b9[b6].keys())
    b2 = max(b1)
    b3 = min(b1)
    if b8 > b2:
        raise ValueError(f"Maximum available date is {b2}.")
    if b7 < b3:
        raise ValueError(f"Minimum available date is {b3}.")
def fonk5(b9, b6, b7, b8):
    b4 = [key for key in b9[b6] if b7 <= key <= b8]
    return [float(b9[b6][key]["Price"].replace(',', '')) for key in b4]
def fonk6():
    b5 = sys.argv
    fonk2(b5)
    b6 = b5[3]
    b7 = b5[1]
    b8 = b5[2]
    b9 = fonk3('result.json')
    fonk4(b9, b6, b7, b8)
    b10 = fonk5(b9, b6, b7, b8)
    b11 = np.mean(b10)
    b12 = np.var(b10)
    print(f"{b6.capitalize()} - Mean Price: {b11:.2f}, Variance: {b12:.2f}")
if b13 = = "__main__":
    fonk6()