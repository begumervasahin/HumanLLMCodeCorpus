factorlist1 = [
    "factor list 1 item 1",
    "factor list 1 item 2",
    "factor list 1 item 3"
]
factorlist2 = [
    "factor list 2 item 1",
    "factor list 2 item 2",
    "factor list 2 item 3",
    "factor list 2 item 4"
]
factorlist3 = [
    "factor list 3 item 1",
    "factor list 3 item 2"
]
factorlist4 = [
    "factor list 4 item 1",
    "factor list 4 item 2",
    "factor list 4 item 3",
    "factor list 4 item 4",
    "factor list 4 item 5"
]
factorlist5 = [
    "factor list 5 item 1",
    "factor list 5 item 2",
    "factor list 5 item 3"
]
question_number = 1
for item1 in factorlist1:
    for item2 in factorlist2:
        for item3 in factorlist3:
            for item4 in factorlist4:
                for item5 in factorlist5:
                    print("[[Block]]")
                    print(f"{question_number}. You are {item1}. You see {item2}. When you, {item3}, react {item4} in order to {item5}.")
                    print()
                    print("This situation is acceptable to me:")
                    print()
                    print("Strongly Agree.")
                    print("Agree.")
                    print("Neither Agree nor Disagree.")
                    print("Disagree.")
                    print("Strongly Disagree.")
                    question_number += 1
                    print()
print()