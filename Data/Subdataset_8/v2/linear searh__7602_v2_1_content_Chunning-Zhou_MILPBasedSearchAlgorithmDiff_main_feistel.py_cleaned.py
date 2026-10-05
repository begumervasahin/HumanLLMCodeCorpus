import numpy as np
import time
class Cipher:
class Parameter:
class ClassModel:
def initArray():
    pass
def Method_1(r, Na, i, DP):
    pass
def Method_2(r, Na, i, DP):
    pass
def Method_3(r, Na, i, DP, Strategy, obj_compare):
    pass
def search(r):
    pass
def initLBArray(r):
    pass
def genUpperBound(r):
    pass
def searchSubset0(r):
    pass
def UpdateLBSubset0(r, Na, i, DP):
    pass
def estimateAddition1(r, Na, i, DP):
    pass
def searchSubset1(r):
    pass
if __name__ == "__main__":
    cipher = Cipher()
    parameter = Parameter()
    class_model = ClassModel()
    cipher.name = "your_cipher_name"
    parameter.cipher = cipher
    parameter.goal = "your_goal"
    search_round = cipher.get_search_round(parameter.goal)
    time_all = []
    with open(f"result/{cipher.name}/{parameter.goal}/solved_LBAS_model.txt", "w") as f:
        f.write("models we solved:\n")
    with open(f"result/{cipher.name}/{parameter.goal}/solved_model.txt", "w") as f:
        f.write("models we solved:\n")
    initArray()
    for r in range(1, search_round + 1):
        time_start = time.time()
        with open(f"result/{cipher.name}/{parameter.goal}/{r}_round_search_result.txt", "w") as f:
            f.write("search process:\n")
        with open(f"result/{cipher.name}/{parameter.goal}/solved_LBAS_model.txt", "a") as f:
            f.write("\n*****************************************************************************\n"
                    f"when searching the {r}-round cipher, models we solved:\n")
        with open(f"result/{cipher.name}/{parameter.goal}/solved_model.txt", "a") as f:
            f.write("\n*****************************************************************************\n"
                    f"when searching the {r}-round cipher, models we solved:\n")
        search(r)
        time_end = time.time()
        timespend = time_end - time_start
        time_all.append(timespend)
        with open(f"result/{cipher.name}/{parameter.goal}/{r}_round_search_result.txt", "a") as f:
            f.write(f"time is {timespend} s.\n")
        with open(f"result/{cipher.name}/{parameter.goal}/bestobj.txt", "w") as f:
            f.write(f"bestobj = {str(bestobj)}\n")
            f.write(f"time_all = {str(time_all)}\n")