
import pyfpgrowth as pyfp
import fp2ar
import re
def read_transaction_file(filename):
    transactions = []
    with open(filename) as file:
        content = file.readlines()
        for line in content:
            items = re.split(r'\s+', line.strip())
            transaction = [int(item) for item in items if item.isdigit()]
            if transaction:
                transactions.append(transaction)
    return transactions
dataset = read_transaction_file("kosarak.dat")
min_support = 0.01
frequent_patterns = pyfp.getFP(dataset, min_support)
min_confidence = 0.75
min_lift = 1
association_rules = fp2ar.getAR(frequent_patterns, len(dataset), min_confidence, min_lift)
