import re
class CurrencyExchange:
    def __init__(self, from_currency, to_currency, exchange_rate):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange_rate = float(exchange_rate)
    def __str__(self):
        return f"{self.from_currency} -> {self.to_currency}: {self.exchange_rate}"
    def __repr__(self):
        return self.__str__()
class CurrencyExchangeReader:
    def __init__(self, file_name):
        self.file_name = file_name
    def parse_currency_name(self, name_line):
        parts = name_line.split(" ", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid currency name line: {name_line}")
        return parts[0], parts[1]
    def parse_currency_exchange_rate(self, rate_line):
        parts = rate_line.split(" ", 2)
        if len(parts) != 3:
            raise ValueError(f"Invalid currency exchange rate line: {rate_line}")
        return CurrencyExchange(parts[0], parts[1], parts[2])
    def read_data(self):
        currency_name_regex = re.compile(r"[A-Z]{3} [A-Z\(\)\.& \-]+")
        currency_exchange_rate_regex = re.compile(r"[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        currency_code_name_map = {}
        currency_exchange_rate_list = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    line = line.strip()
                    if currency_exchange_rate_regex.match(line):
                        currency_exchange_rate_list.append(self.parse_currency_exchange_rate(line))
                    elif currency_name_regex.match(line):
                        code, name = self.parse_currency_name(line)
                        currency_code_name_map[code] = name
                    else:
                        raise ValueError(f"Invalid line in file {self.file_name}: {line}")
        except IOError as e:
            print(f"Cannot open file {self.file_name}: {e}")
        return currency_code_name_map, currency_exchange_rate_list
def main():
    file_name = "currency_data.txt"
    reader = CurrencyExchangeReader(file_name)
    currency_code_name_map, currency_exchange_rate_list = reader.read_data()
    print("Currency Codes and Names:")
    for code, name in currency_code_name_map.items():
        print(f"{code}: {name}")
    print("\nCurrency Exchange Rates:")
    for exchange in currency_exchange_rate_list:
        print(exchange)
if __name__ == "__main__":
    main()