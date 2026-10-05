
b1 = [
    ["factor list 1 item 1", "factor list 1 item 2", "factor list 1 item 3"],
    ["factor list 2 item 1", "factor list 2 item 2", "factor list 2 item 3", "factor list 2 item 4"],
    ["factor list 3 item 1", "factor list 3 item 2"],
    ["factor list 4 item 1", "factor list 4 item 2", "factor list 4 item 3", "factor list 4 item 4", "factor list 4 item 5"],
    ["factor list 5 item 1", "factor list 5 item 2", "factor list 5 item 3"]
]
a1 = 1
for items in zip(*b1):
    item_1, item_2, item_3, item_4, b2 = items
    print("[[Block]]")
    print(f"{a1}. You are {item_1}. You see {item_2}. When you, {item_3} reacts {item_4} in order to {b2}.")
    print("\nThis situation is acceptable to me:")
    print("\nStrongly Agree.")
    print("Agree.")
    print("Neither Agree nor Disagree.")
    print("Disagree.")
    print("Strongly Disagree.\n")
    a1 += 1
print("\n")