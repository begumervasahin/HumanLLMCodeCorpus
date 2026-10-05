import re
class WatchList:
    def __init__(self, filename=""):
        self.bills = {"5": [], "10": [], "20": [], "50": [], "100": []}
        self.is_sorted = filename == ''
        if not self.is_sorted:
            self.load_watchlist_from_file(filename)
        self.validator = re.compile(r'^[A-M][A-L](?!00000000)\d{8}(?![OZ])[A-Z]$')
    def load_watchlist_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                serial_number, denomination = line.split()
                self.bills[denomination].append(serial_number)
    def insert(self, bill_string):
        serial_number, denomination = bill_string.split()
        specific_bill_values = self.bills[denomination]
        if self.is_sorted and serial_number not in specific_bill_values:
            self.insert_sorted(serial_number, specific_bill_values)
        elif not self.is_sorted and serial_number not in specific_bill_values:
            specific_bill_values.append(serial_number)
    def insert_sorted(self, serial_number, specific_bill_values):
        for i, value in enumerate(specific_bill_values):
            if serial_number < value:
                specific_bill_values.insert(i, serial_number)
                return
        specific_bill_values.append(serial_number)
    def sort_bills(self):
        for key in self.bills:
            self.bills[key].sort()
        self.is_sorted = True
    def linear_search(self, bill_string):
        serial_number, denomination = bill_string.split()
        return serial_number in self.bills[denomination]
    def binary_search(self, bill_string):
        serial_number, denomination = bill_string.split()
        dictionary_list = self.bills[denomination]
        low_index, high_index = 0, len(dictionary_list) - 1
        while low_index <= high_index:
            mid = (high_index + low_index)
            if dictionary_list[mid] == serial_number:
                return True
            elif dictionary_list[mid] > serial_number:
                high_index = mid - 1
            else:
                low_index = mid + 1
        return False
    def check_bills(self, filename, sort_watchlist=False):
        if sort_watchlist and not self.is_sorted:
            self.sort_bills()
        search_method = self.binary_search if self.is_sorted else self.linear_search
        bad_bills = []
        with open(filename, 'r') as file:
            for line in file:
                serial_number, denomination = line.split()
                sn_dm = f"{serial_number} {denomination}"
                if search_method(line) or not self.validator.match(serial_number):
                    bad_bills.append(sn_dm)
        return bad_bills
watchlist = WatchList("your_watchlist_file.txt")
watchlist.insert("ABC12345678 20")
watchlist.insert("DEF98765432 10")
watchlist.insert("GHI87654321 5")
print(watchlist.check_bills("bill_file.txt", sort_watchlist=True))