
b1 = ["factor list 1 item 1", "factor list 1 item 2", "factor list 1 item 3"]
b2 = ["factor list 2 item 1", "factor list 2 item 2", "factor list 2 item 3", "factor list 2 item 4"]
b3 = ["factor list 3 item 1", "factor list 3 item 2"]
b4 = ["factor list 4 item 1", "factor list 4 item 2", "factor list 4 item 3", "factor list 4 item 4", "factor list 4 item 5"]
b5 = ["factor list 5 item 1", "factor list 5 item 2", "factor list 5 item 3"]
a1 = 1
for i in b1:
    for j in b2:
        for k in b3:
            for l in b4:
                for m in b5:
                    print("[[Block]]")
                    print(f"{a1}. You are {i}. You see {j}. When you, {k} reacts {l} in order to {m}.")
                    print("\nThis situation is acceptable to me:")
                    print("\nStrongly Agree.")
                    print("Agree.")
                    print("Neither Agree nor Disagree.")
                    print("Disagree.")
                    print("Strongly Disagree.\n")
                    a1 += 1