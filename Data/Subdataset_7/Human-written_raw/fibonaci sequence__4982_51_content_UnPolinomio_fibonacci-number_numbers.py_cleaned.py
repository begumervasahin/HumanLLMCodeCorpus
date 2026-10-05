b1 = input("\nHow many numbers do you want to calculate?\n>> ")
def fonk1(howMany):
    b2 = [1, 1]
    for i in range(howMany-2):
        b3 = i + 2
        b2.append(b2[b3-1] + b2[b3-2])
    for i,num in enumerate(b2):
        print(str(i+1) + ".-", num)
if b1 = = "":
    print("\nError: Please insert a value.")
else:
    try:
        b1 = int(b1)
    except ValueError:
        print("\nError: Insert an integer number please.")
    else:
        if b1 < 2:
            print("\nError: Please insert a positive number; where number >= 2.")
        else:
            fonk1(b1)