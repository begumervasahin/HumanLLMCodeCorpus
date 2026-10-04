import re
class CurrencyExchange:
    def __init__(self, from_currency, to_currency, exchange_rate):
        self._from_currency = from_currency
        self._to_currency = to_currency
        self._exchange_rate = float(exchange_rate)
    def __str__(self):
        return f"{self._from_currency} -> {self._to_currency}: {self._exchange_rate}"
    def __repr__(self):
        return self.__str__()
    @property
    def from_currency(self):
        return self._from_currency
    @property
    def to_currency(self):
        return self._to_currency
    @property
    def exchange_rate(self):
        return self._exchange_rate
class CurrencyExchangeReader:
    def __init__(self, iFileName):
        self._fileName = iFileName
    def parseCurrencyName(self, iNameLine):
        currencyCodeNameList = iNameLine.split(" ", 1)
        assert len(currencyCodeNameList) == 2
        return currencyCodeNameList
    def parseCurrencyExchangeRate(self, iRateLine):
        exchangeInfoList = iRateLine.split(" ", 2)
        assert len(exchangeInfoList) == 3
        return CurrencyExchange(*exchangeInfoList)
    def readData(self):
        currencyNameRegEx = re.compile(r"[A-Z]{3} [A-Z\(\)\.& \-]+")
        currencyExchangeRateRegEx = re.compile(r"[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        currencyCodeNameMap = {}
        currencyExchangeRateList = []
        try:
            with open(self._fileName, 'r') as fileHandle:
                for line in fileHandle:
                    line = line.rstrip("\n\r")
                    if re.match(currencyExchangeRateRegEx, line):
                        currencyExchangeRateList.append(self.parseCurrencyExchangeRate(line))
                    elif re.match(currencyNameRegEx, line):
                        currencyCode, currencyName = self.parseCurrencyName(line)
                        currencyCodeNameMap[currencyCode] = currencyName
                    else:
                        raise Exception(f"Invalid line in file {self._fileName}: {line}")
        except IOError as exception:
            print(f"Cannot open file {self._fileName}: {exception}")
        return currencyCodeNameMap, currencyExchangeRateList
def main():
    fileName = "currency_data.txt"
    reader = CurrencyExchangeReader(fileName)
    currencyCodeNameMap, currencyExchangeRateList = reader.readData()
    print("Currency Codes and Names:")
    for code, name in currencyCodeNameMap.items():
        print(f"{code}: {name}")
    print("\nCurrency Exchange Rates:")
    for exchange in currencyExchangeRateList:
        print(exchange)
if __name__ == "__main__":
    main()