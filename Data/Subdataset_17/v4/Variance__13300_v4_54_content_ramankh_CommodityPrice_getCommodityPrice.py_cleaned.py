import json
import numpy as np
import sys
from datetime import datetime
def validate(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The dates should be in the following format: YYYY-MM-DD")
def args_validate(args):
    if len(args) != 4:
        raise AssertionError("The number of arguments should be exactly 3: Starting Date, Ending Date, and Commodity Name")
    validate(args[1])
    validate(args[2])
    if args[3] not in ["gold", "silver"]:
        raise ValueError("The third argument must be either 'silver' or 'gold'")
def load_data(file_path='result.json'):
    with open(file_path, 'r') as fp:
        return json.load(fp)
def final_validation(starting, ending, commodity, data):
    all_keys = list(data[commodity].keys())
    max_date = max(all_keys)
    min_date = min(all_keys)
    if max_date < ending:
        raise ValueError(f"Sorry! My maximum date is {max_date}")
    if min_date > starting:
        raise ValueError(f"Sorry! My minimum date is {min_date}")
def calculate_statistics(starting, ending, commodity, data):
    keys = [key for key in data[commodity] if starting <= key <= ending]
    prices = [float(data[commodity][x]["Price"].replace(',', '')) for x in keys]
    return np.mean(prices), np.var(prices)
def main(args):
    args_validate(args)
    starting = args[1]
    ending = args[2]
    commodity = args[3]
    data = load_data()
    final_validation(starting, ending, commodity, data)
    mean_price, price_variance = calculate_statistics(starting, ending, commodity, data)
    print(commodity, mean_price, price_variance)
if __name__ == "__main__":
    main(sys.argv)