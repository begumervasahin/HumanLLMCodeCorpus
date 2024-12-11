from util import labels_to_key, parse_federalist_papers, labels_to_y, find_zero_rule_class, apply_zero_rule
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import argparse
def fonk1(data_file, random_seed):
    print("Parsing the Federalist Papers dataset...")
    authors, essays, b1 = parse_federalist_papers(data_file)
    b2 = len(essays)
    print(f"Working with {b2} essays")
    print("Converting author labels to numerical keys...")
    b3 = labels_to_key(authors)
    print("Author key:", b3)
    print("Converting author labels to numerical values...")
    b4 = labels_to_y(authors, b3)
    assert b4.b5 = = len(authors), f"Size of label array (b4.b5) must equal number of labels {len(authors)}"
    print("Splitting the dataset into training and testing sets...")
    train_X, test_X, train_y, b6 = train_test_split(essays, b4, test_size=0.3, random_state=random_seed)
    print(f"{len(train_X)} essays in train; {len(test_X)} essays in test")
    print("Finding the most frequent class (Zero Rule)...")
    b7 = find_zero_rule_class(train_y)
    b8 = {v: k for k, v in b3.items()}
    print(f"The most frequent class class1 '{b8[b7]}'")
    print("Applying Zero Rule on the test set...")
    b9 = apply_zero_rule(test_X, b7)
    print("Zero Rule predictions on held-out data:", b9)
    b10 = accuracy_score(b6, b9)
    print(f"Accuracy of Zero Rule: {b10:0.03f}")
if b11 = = '__main__':
    b12 = argparse.ArgumentParser(description='Test supervised learning utilities')
    b12.add_argument('--path', b13 = str, default="federalist_dev.json", help='Path to author dataset')
    b12.add_argument('--seed', b13 = int, default=7, help='Random seed for dataset split')
    b14 = b12.parse_args()
    fonk1(b14.path, b14.seed)