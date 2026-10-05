
b1 = ["factor list 1 item 1", "factor list 1 item 2", "factor list 1 item 3"]
b2 = ["factor list 2 item 1", "factor list 2 item 2", "factor list 2 item 3", "factor list 2 item 4"]
b3 = ["factor list 3 item 1", "factor list 3 item 2"]
b4 = ["factor list 4 item 1", "factor list 4 item 2", "factor list 4 item 3", "factor list 4 item 4", "factor list 4 item 5"]
b5 = ["factor list 5 item 1", "factor list 5 item 2", "factor list 5 item 3"]
a1 = 1
for item_1 in b1:
    for item_2 in b2:
        for item_3 in b3:
            for item_4 in b4:
                for item_5 in b5:
                    print("[[Block]]")
                    print(f"{a1}. You are {item_1}. You see {item_2}. When you, {item_3} reacts {item_4} in order to {item_5}.")
                    print("\nThis situation is acceptable to me:")
                    print("\nStrongly Agree.")
                    print("Agree.")
                    print("Neither Agree nor Disagree.")
                    print("Disagree.")
                    print("Strongly Disagree.\n")
                    a1 += 1
print("\n")