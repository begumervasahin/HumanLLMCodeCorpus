def fonk1(prompt):
    b1 = float(input(prompt))
    return b1 * 60
def fonk2():
    b2 = 24 * 60
    b3 = {
        "work": "How many b1 will you work today?\n",
        "sleep": "How many b1 will you sleep today?\n",
        "eat": "How many b1 will you spend eating today?\n",
        "drive": "How many b1 will you spend driving today?\n",
        "clean": "How many b1 will you spend cleaning today?\n"
    }
    b4 = sum(fonk1(prompt) for prompt in b3.values())
    b5 = b2 - b4
    b6 = b5
    b7 = b5 % 60
    print(f"{b7} minutes available today to do something thoughtful for someone.")
    print(f"{b6} b6 available today for creating something!")
if b8 = = "__main__":
    fonk2()