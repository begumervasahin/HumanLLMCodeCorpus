b1 = [
    "factor list 1 item 1",
    "factor list 1 item 2",
    "factor list 1 item 3"
]
b2 = [
    "factor list 2 item 1",
    "factor list 2 item 2",
    "factor list 2 item 3",
    "factor list 2 item 4"
]
b3 = [
    "factor list 3 item 1",
    "factor list 3 item 2"
]
b4 = [
    "factor list 4 item 1",
    "factor list 4 item 2",
    "factor list 4 item 3",
    "factor list 4 item 4",
    "factor list 4 item 5"
]
b5 = [
    "factor list 5 item 1",
    "factor list 5 item 2",
    "factor list 5 item 3"
]
a1 = 1
for item1 in b1:
    for item2 in b2:
        for item3 in b3:
            for item4 in b4:
                for item5 in b5:
                    print("[[Block]]")
                    print(f"{a1}. You are {item1}. You see {item2}. When you, {item3}, react {item4} in order to {item5}.")
                    print()
                    print("This situation is acceptable to me:")
                    print()
                    print("Strongly Agree.")
                    print("Agree.")
                    print("Neither Agree nor Disagree.")
                    print("Disagree.")
                    print("Strongly Disagree.")
                    a1 += 1
                    print()
print()