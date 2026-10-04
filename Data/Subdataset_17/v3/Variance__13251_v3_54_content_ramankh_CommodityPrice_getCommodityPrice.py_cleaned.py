import json
import numpy as np
import sys
from datetime import datetime
def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Date format should be YYYY-MM-DD.")
def validate_arguments(args):
    if len(args) != 4:
        raise AssertionError("Exactly 3 arguments required: Starting Date, Ending Date, Commodity Name.")
    validate_date(args[1])
    validate_date(args[2])
    if args[3] not in ["gold", "silver"]:
        raise ValueError("Commodity name must be either 'gold' or 'silver'.")
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def validate_date_range(data, commodity, start_date, end_date):
    all_dates = list(data[commodity].keys())
    max_date = max(all_dates)
    min_date = min(all_dates)
    if end_date > max_date:
        raise ValueError(f"Maximum available date is {max_date}.")
    if start_date < min_date:
        raise ValueError(f"Minimum available date is {min_date}.")
def filter_prices(data, commodity, start_date, end_date):
    filtered_keys = [key for key in data[commodity] if start_date <= key <= end_date]
    return [float(data[commodity][key]["Price"].replace(',', '')) for key in filtered_keys]
def main():
    args = sys.argv
    validate_arguments(args)
    commodity = args[3]
    start_date = args[1]
    end_date = args[2]
    data = load_data('result.json')
    validate_date_range(data, commodity, start_date, end_date)
    prices = filter_prices(data, commodity, start_date, end_date)
    mean_price = np.mean(prices)
    variance_price = np.var(prices)
    print(f"{commodity.capitalize()} - Mean Price: {mean_price:.2f}, Variance: {variance_price:.2f}")
if __name__ == "__main__":
    main()