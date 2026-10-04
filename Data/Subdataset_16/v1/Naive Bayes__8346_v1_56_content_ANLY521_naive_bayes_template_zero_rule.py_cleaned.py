import argparse
from util import labels_to_key, parse_federalist_papers, labels_to_y, find_zero_rule_class, apply_zero_rule
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
def fonk1(data_file, random_seed):
    print(data_file)
    authors, essays, b1 = parse_federalist_papers(data_file)
    b2 = len(essays)
    print(f"1: Working with {b2} reviews")
    b3 = labels_to_key(authors)
    print(f"2: Author key {b3}")
    b4 = labels_to_y(authors, b3)
    assert b4.b5 = = len(authors), f"Size of label array (b4.b5) must equal number of labels {len(authors)}"
    train_X, test_X, train_y, b6 = train_test_split(essays, b4, test_size=0.3, random_state=random_seed)
    print(f"{len(train_X)} in train; {len(test_X)} in test")
    b7 = find_zero_rule_class(train_y)
    b8 = {v: k for k, v in b3.items()}
    print(f"2. The most frequent class class1 {b8[b7]}")
    b9 = apply_zero_rule(test_X, b7)
    print(f"3. Zero rule predictions on held-out data: {b9}")
    b10 = accuracy_score(b6, b9)
    print(f"4. Accuracy of zero rule: {b10:0.03f}")
if b11 = = '__main__':
    b12 = argparse.ArgumentParser(description='Test supervised learning utilities')
    b12.add_argument('--path', b13 = str, default="federalist_dev.json",
                        b14 = 'Path to author dataset')
    b12.add_argument('--seed', b13 = int, default=7,
                        b14 = 'Random seed for dataset split')
    b15 = b12.parse_args()
    fonk1(b15.path, b15.seed)