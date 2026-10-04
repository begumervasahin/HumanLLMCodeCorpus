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
questionnumber = 1
for i in factorlist1:
    for j in factorlist2:
        for k in factorlist3:
            for l in factorlist4:
                for m in factorlist5:
                    print("[[Block]]")
                    print(f"{questionnumber}. You are {i}. You see {j}. When you, {k}, react {l} in order to {m}.")
                    print()
                    print("This situation is acceptable to me:")
                    print()
                    print("Strongly Agree.")
                    print("Agree.")
                    print("Neither Agree nor Disagree.")
                    print("Disagree.")
                    print("Strongly Disagree.")
                    questionnumber += 1
                    print()
print()