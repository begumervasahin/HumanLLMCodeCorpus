import mysql.connector
import pandas as pd
import statistics
from sklearn.metrics import mean_squared_error
import csv
def calculate_percentage_change(values):
    percentage_changes = [(values[i] - values[i-1]) / values[i-1] * 100 for i in range(1, len(values))]
    return percentage_changes
def calculate_opposite_trends(base_changes, comparison_changes):
    opposite_count = sum(1 for base_change, comparison_change in zip(base_changes, comparison_changes) if base_change * comparison_change < 0)
    return (opposite_count / len(base_changes)) * 100
connection = mysql.connector.connect(user='student', password='cs336student',
                                     host='cs336.ckksjtjg2jto.us-east-2.rds.amazonaws.com',
                                     database='CryptoNews')
currency_data = pd.read_sql("SELECT distinct currency_name FROM CryptoNews.Value", connection)
currencies = currency_data['currency_name'].tolist()
bitcoin_values_df = pd.read_sql("SELECT quote FROM CryptoNews.Value WHERE currency_name='Bitcoin'", connection)
bitcoin_values = bitcoin_values_df['quote'].tolist()
bitcoin_changes = calculate_percentage_change(bitcoin_values)
final_results = [["Crypto Currency", "Volatility", "Mean Square Error", "Opposite Trend %", "Outlier Score"]]
for currency in currencies:
    currency_values_df = pd.read_sql(f"SELECT quote FROM CryptoNews.Value WHERE currency_name='{currency}'", connection)
    currency_values = currency_values_df['quote'].tolist()
    if len(currency_values) < 101:
        continue
    currency_changes = calculate_percentage_change(currency_values)
    standard_deviation = statistics.stdev(currency_changes)
    mean_squared_error_value = mean_squared_error(bitcoin_changes, currency_changes)
    opposite_trends_percentage = calculate_opposite_trends(bitcoin_changes, currency_changes)
    outlier_score = (standard_deviation * 0.1) + (mean_squared_error_value * 0.45) + (opposite_trends_percentage * 0.45)
    temp_result = [currency, standard_deviation, mean_squared_error_value, opposite_trends_percentage, outlier_score]
    final_results.append(temp_result)
with open("outlier.csv", 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    csv_writer.writerows(final_results)
print("Output generated in outlier.csv")