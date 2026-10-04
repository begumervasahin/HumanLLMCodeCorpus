class CurrencyExchange:
    def __init__(self, from_currency, to_currency, exchange_rate):
        self.__from_currency = from_currency
        self.__to_currency = to_currency
        self.__exchange_rate = float(exchange_rate)
    def __str__(self):
        return f"{self.__from_currency} -> {self.__to_currency}: {self.__exchange_rate}"
    def __repr__(self):
        return self.__str__()
    @property
    def from_currency(self):
        return self.__from_currency
    @property
    def to_currency(self):
        return self.__to_currency
    @property
    def exchange_rate(self):
        return self.__exchange_rate
def main():
    exchange = CurrencyExchange("USD", "EUR", 0.85)
    print(exchange)
    print(f"From Currency: {exchange.from_currency}")
    print(f"To Currency: {exchange.to_currency}")
    print(f"Exchange Rate: {exchange.exchange_rate}")
if __name__ == "__main__":
    main()