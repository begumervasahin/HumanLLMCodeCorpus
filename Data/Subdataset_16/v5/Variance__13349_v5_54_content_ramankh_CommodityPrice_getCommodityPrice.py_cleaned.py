import json
import numpy as np
import sys
from datetime import datetime
def fonk1(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The dates should be in the following format: YYYY-MM-DD")
def fonk2(arguments):
    if len(arguments) != 4:
        raise AssertionError("Exactly 3 arguments are required: Starting Date, Ending Date, and Commodity Name")
    fonk1(arguments[1])
    fonk1(arguments[2])
    if arguments[3] not in ["gold", "silver"]:
        raise ValueError("The third argument must be either 'silver' or 'gold'")
def fonk3(b1 = 'result.json'):
    with open(b1, 'r') as file:
        return json.load(file)
def fonk4(starting, ending, commodity, b10):
    b2 = list(b10[commodity].keys())
    b3 = max(b2)
    b4 = min(b2)
    if ending > b3:
        raise ValueError(f"Ending date exceeds available b10. Maximum date is {b3}.")
    if starting < b4:
        raise ValueError(f"Starting date is before available b10. Minimum date is {b4}.")
def fonk5(starting, ending, commodity, b10):
    b5 = [date for date in b10[commodity] if starting <= date <= ending]
    b6 = [float(b10[commodity][date]["b12"].replace(',', '')) for date in b5]
    return np.mean(b6), np.var(b6)
def fonk6():
    fonk2(sys.argv)
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    b9 = sys.argv[3]
    b10 = fonk3()
    fonk4(b7, b8, b9, b10)
    mean_price, b11 = fonk5(b7, b8, b9, b10)
    print(f"{b9}: Mean b12 = {mean_price:.2f}, b12 Variance = {b11:.2f}")
if b13 = = "__main__":
    fonk6()