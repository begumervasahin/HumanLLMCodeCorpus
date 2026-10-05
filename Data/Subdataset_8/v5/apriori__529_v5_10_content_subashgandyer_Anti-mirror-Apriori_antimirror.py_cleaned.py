import CSVtoLIST_def as cs
import am
import sys
import time
def main():
    print_usage_info()
    start_time = time.clock()
    filename, minsup, min_confidence = extract_command_line_args()
    print_args_info(filename, minsup, min_confidence)
    n_itemlist, count = cs.readCSV(filename)
    print('Total Transactions:', count)
    result, test_dict, Mapper_list, Transaction_list = process_transactions(n_itemlist)
    list2, support_data = perform_additional_processing(Transaction_list, minsup)
    answer = generate_association_rules(list2, minsup, min_confidence, support_data, result, test_dict)
    print_association_rules(answer)
    print_program_completion(start_time)
def print_usage_info():
    print("Usage: $ python scriptname filename.csv minsup min_confidence")
    print("Ex: $ python testclass.py groceries_small.csv 3 0.5")
def extract_command_line_args():
    try:
        filename = sys.argv[1]
        minsup = int(sys.argv[2])
        min_confidence = float(sys.argv[3])
        return filename, minsup, min_confidence
    except IndexError:
        print("Please provide the required command line arguments.")
        sys.exit(1)
def print_args_info(filename, minsup, min_confidence):
    print('Script Name:', sys.argv[0])
    print('Filename:', filename)
    print('Minsup:', minsup)
    print('Min Confidence:', min_confidence)
def process_transactions(n_itemlist):
    a = cs.manyToOne(n_itemlist)
    result = cs.removeDuplicates(a)
    test_dict = cs.createDictionary(result)
    Mapper_list = cs.mapper(n_itemlist, test_dict)
    Transaction_list = cs.binaryTransactionListBuilder(Mapper_list, result)
    return result, test_dict, Mapper_list, Transaction_list
def perform_additional_processing(Transaction_list, minsup):
    Transaction_list2 = am.countTransactions(Transaction_list)
    b = am.remDupSortReverseList(Transaction_list2)
    temp_list1 = am.addCountersTransactions(b)
    not_to_be_pruned_items, to_be_pruned_items_list, list1, list2, support_data = am.antiMirroring(temp_list1, minsup)
    return list2, support_data
def generate_association_rules(list2, minsup, min_confidence, support_data, result, test_dict):
    rules = am.rules_generator(list2, minsup, min_confidence, support_data)
    cleanRules = am.cleanRules(rules)
    result = am.reversed(cleanRules, [], test_dict)
    answer = am.formattedRules(result)
    return answer
def print_association_rules(answer):
    print(' ')
    print(' ')
    print('Association Rules:')
    for idx, items in enumerate(answer, start=1):
        print(f'{idx}. {items}')
    print(' ')
    print(' ')
def print_program_completion(start_time):
    print(f'---- PROGRAM OVER in {time.clock() - start_time} seconds ----')
if __name__ == '__main__':
    main()