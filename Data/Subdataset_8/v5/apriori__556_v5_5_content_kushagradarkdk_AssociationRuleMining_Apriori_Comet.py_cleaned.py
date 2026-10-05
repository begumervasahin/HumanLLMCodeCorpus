import pandas as pd
import itertools
from collections import defaultdict
USED_ROWS = 100000
class Apriori:
    def __init__(self, order_file, product_file, min_support=0.01, min_confidence=0.01):
        self.order_file = order_file
        self.product_file = product_file
        self.support_threshold = min_support
        self.confidence_threshold = min_confidence
        self.total_transactions = None
        self.processed_product_names = None
        self.single_item_freq_table = None
        self.product_order_dict = None
        self.preprocess_data()
    def get_support(self, product_freq):
        return product_freq / self.total_transactions >= self.support_threshold, product_freq / self.total_transactions
    def check_confidence(self, pair_support, item_support):
        return pair_support / item_support >= self.confidence_threshold, pair_support / item_support
    def generate_k_item_set(self, item_set, k):
        result = []
        length = len(item_set)
        for i in range(length):
            for j in range(i + 1, length):
                listing1 = item_set[i]
                listing2 = item_set[j]
                combined = listing1 + list(set(listing2) - set(listing1))
                combined.sort()
                if combined not in result:
                    result.append(combined)
        return [item for item in result if len(item) == k]
    def freq_1_itemset(self):
        output_list_k_1 = []
        for product in self.single_item_freq_table:
            item_support_status, item_support = self.get_support(self.single_item_freq_table[product])
            if item_support_status:
                output_list_k_1.append([product])
        return output_list_k_1
    def generate_all_frequent_itemsets(self):
        k = 1
        item_set = self.freq_1_itemset()
        resultant_k_itemsets = []
        while k < 2:
            k += 1
            k_itemset = self.generate_k_item_set(item_set=item_set, k=k)
            generated_freq_k_itemset = []
            for item in k_itemset:
                item_count = sum(1 for order_data in self.processed_product_names if set(item).issubset(order_data))
                item_support_status, item_support = self.get_support(item_count)
                if item_support_status:
                    item.sort()
                    generated_freq_k_itemset.append([item, item_support])
            if generated_freq_k_itemset:
                item_set = generated_freq_k_itemset
                resultant_k_itemsets.append(generated_freq_k_itemset)
        return resultant_k_itemsets
    def print_baggage_content(self, association_dict, baggage):
        print("Items added to baggage:")
        print(baggage)
        choice = input("Do you want to add more items? Press Y for Yes or N for Checkout\n")
        if choice.lower() == 'y':
            self.recommend_items(association_dict, baggage)
        else:
            print("Thank you for shopping with us.")
    def recommend_items(self, association_dict, bag=[]):
        baggage = bag
        while True:
            chosen_item = input("Please choose an item you want to buy, or press 'Q' to quit\n")
            if chosen_item.lower() == 'q':
                break
            else:
                if chosen_item in association_dict:
                    print("These items are bought together often. Do you want any of these?")
                    print(association_dict[chosen_item])
                    baggage.append(chosen_item)
                else:
                    print(f"{chosen_item} not found")
        self.print_baggage_content(association_dict, baggage)
    def generate_association_rules(self):
        print("Association Rules")
        print("-----------------")
        print("RULES \t\t SUPPORT \t\t CONFIDENCE")
        k_2_itemsets = self.generate_all_frequent_itemsets()
        association_dict = defaultdict(list)
        num = 1
        for pair_list in k_2_itemsets:
            for pair in pair_list:
                data = pair[:-1]
                subset_size = 1
                for item in data:
                    data = item
                pair_support = pair[-1]
                for item in itertools.combinations(data, subset_size):
                    item = set(item)
                    item_count = sum(1 for order_data in self.processed_product_names if item.issubset(order_data))
                    item_support_status, item_support = self.get_support(item_count)
                    if item_support_status:
                        pair_confidence_status, pair_confidence = self.check_confidence(pair_support, item_support)
                        if pair_confidence_status:
                            for i in data:
                                if i not in item:
                                    product = i
                            item = list(item)
                            association_dict[item[0]].append(product)
                            print(f"Rule
                            num += 1
        baggage = []
        self.recommend_items(association_dict, baggage)
    def preprocess_data(self):
        orders = pd.read_csv(self.order_file)
        products = pd.read_csv(self.product_file)
        condensed_order = orders[['order_id', 'product_id']]
        products = products[['product_id', 'product_name']]
        products_indexID = products.set_index('product_id')['product_name']
        orDict = defaultdict(list)
        for index, row in condensed_order.head(n=USED_ROWS).iterrows():
            orDict[row[0]].append(products_indexID[row[1]].replace(" ", ""))
        transactions = 0
        item_freq = {}
        processed_product_names = []
        for key, value in orDict.items():
            temp = []
            transactions += 1
            for word in value:
                word = word.replace(" ", "")
                temp.append(word)
                if word not in item_freq.keys():
                    item_freq[word] = 1
                else:
                    item_freq[word] += 1
            processed_product_names.append(temp)
        self.total_transactions = transactions
        self.processed_product_names = [set(transaction_items) for transaction_items in processed_product_names]
        self.single_item_freq_table = item_freq
        self.product_order_dict = orDict
if __name__ == "__main__":
    MIN_SUPPORT_IN_PERCENT = 1
    MIN_CONFIDENCE_IN_PERCENT = 10
    order_file = 'https:
    product_file = 'https:
    association_rules = Apriori(
        order_file=order_file,
        product_file=product_file,
        min_support=MIN_SUPPORT_IN_PERCENT / 100,
        min_confidence=MIN_CONFIDENCE_IN_PERCENT / 100
    )
    association_rules.generate_association_rules()