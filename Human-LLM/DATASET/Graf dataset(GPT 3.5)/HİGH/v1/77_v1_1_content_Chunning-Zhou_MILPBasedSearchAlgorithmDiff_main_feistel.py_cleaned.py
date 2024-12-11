import numpy as np
import time
class class1:
    pass
class class2:
    pass
class class3:
    pass
def fonk1():
    pass
def fonk2(r, Na, i, DP):
    pass
def fonk3(r, Na, i, DP):
    pass
def fonk4(r, Na, i, DP, Strategy, obj_compare):
    pass
def fonk5(r):
    pass
def fonk6(r):
    pass
def fonk7(r):
    pass
def fonk8(r):
    pass
def fonk9(r, Na, i, DP):
    pass
def fonk10(r, Na, i, DP):
    pass
def fonk11(r):
    pass
if b1 = = "__main__":
    b2 = class1()
    b3 = class2()
    b4 = class3()
    b2.b5 = "your_cipher_name"
    b3.b2 = b2
    b3.b6 = "your_goal"
    b7 = b2.get_search_round(b3.b6)
    b8 = []
    with open(f"result/{b2.b5}/{b3.b6}/solved_LBAS_model.txt", "w") as f:
        f.write("models we solved:\n")
    with open(f"result/{b2.b5}/{b3.b6}/solved_model.txt", "w") as f:
        f.write("models we solved:\n")
    fonk1()
    for r in range(1, b7 + 1):
        b9 = time.time()
        with open(f"result/{b2.b5}/{b3.b6}/{r}_round_search_result.txt", "w") as f:
            f.write("search process:\n")
        with open(f"result/{b2.b5}/{b3.b6}/solved_LBAS_model.txt", "a") as f:
            f.write("\n*****************************************************************************\n"
                    f"when searching the {r}-round b2, models we solved:\n")
        with open(f"result/{b2.b5}/{b3.b6}/solved_model.txt", "a") as f:
            f.write("\n*****************************************************************************\n"
                    f"when searching the {r}-round b2, models we solved:\n")
        fonk5(r)
        b10 = time.time()
        b11 = b10 - b9
        b8.append(b11)
        with open(f"result/{b2.b5}/{b3.b6}/{r}_round_search_result.txt", "a") as f:
            f.write(f"time is {b11} s.\n")
        with open(f"result/{b2.b5}/{b3.b6}/b12.txt", "w") as f:
            f.write(f"b12 = {str(b12)}\n")
            f.write(f"b8 = {str(b8)}\n")