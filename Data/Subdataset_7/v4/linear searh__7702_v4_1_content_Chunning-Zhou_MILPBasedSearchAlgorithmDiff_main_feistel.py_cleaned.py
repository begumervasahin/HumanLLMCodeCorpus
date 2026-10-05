import time
from b10 import class_model
from numpy import *
import numpy as np
import copy
from parameter import b24
import function
global b24
global b11
global b25
global b1
global b2
global b3
global b4
global b13
global b21
global b6
def fonk1():
    global b24
    global b25
    global b1
    global b2
    global b3
    global b4
    b1 = np.zeros((b25), dtype=int)
    b2 = np.zeros((b25, 2, 1 + b25, 1 + b24.num_of_diff_pattern_all), dtype=int32)
    b3 = np.zeros((b25, 2, 1 + b25, 1 + b24.num_of_diff_pattern_all), dtype=int32)
    b4 = np.zeros((b25, 2, 1 + b25, b24.num_of_diff_pattern_all), dtype=int32)
def fonk2(b12, a2, b5, DP):
    global b2
    a1 = 0
    if b5 = = 0 and DP == 0:
        for a3 in range(1, b12):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b12 - a3 - 1, a2 - 1, -1, -1])
    elif 1 <= b5 < b12:
        if 1 < b5 < b12:
            a1 = b2[b5 - 1, a2 - 1, b5 - 1, DP - 1] + b2[b12 - b5 + 1 - 1, a2 - 1, 0, DP - 1]
        for a3 in range(1, b5):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b12 - a3 - 1, a2 - 1, b5 - a3 - 1, DP - 1])
        for a3 in range(b5 + 1, b12):
            a1 = max(a1, b2[a3 - 1, a2 - 1, b5 - 1, DP - 1] + b2[b12 - a3 - 1, a2 - 1, -1, -1])
    elif b5 = = b12:
        for a3 in range(1, b12 - 1):
            a1 = max(a1, b2[a3 - 1, a2 - 1, -1, -1] + b2[b12 - a3 - 1, a2 - 1, b12 - a3 - 1, DP - 1])
    b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], a1)
def fonk3(b12, a2, b5, DP):
    global b2
    global b13
    global b21
    global b6
    a1 = 0
    b6 = b21[np.where(b21 == b5)[0][0] - 1]
    if b5 < b21[0]:
        a1 = function.get_value(b5, b2[b5 - 1, a2 - 1, -1, -1]) + b2[b6 - b5 - 1, a2, -1, -1] + function.get_value(
            b12 - b6, b2[b12 - b6 - 1, a2 - 1, -1, -1])
        a1 = max(a1,
                   function.get_value(b5, b2[b5 - 1, a2 - 1, b5 - 1, DP - 1]) + b2[b6 - b5 + 1 - 1, a2, 0, DP - 1] + function.get_value(
                       b12 - b6, b2[b12 - b6 - 1, a2 - 1, -1, -1]))
    elif b5 > b21[0]:
        a1 = function.get_value(b6 - 1, b2[b6 - 2, a2 - 1, -1, -1]) + b2[b5 - 1 - b6, a2, -1, -1] + function.get_value(
            b12 - b5 + 1, b2[b12 - b5 + 1 - 1, a2 - 1, -1, -1])
        a1 = max(a1,
                   function.get_value(b6 - 1, b2[b6 - 1 - 1, a2 - 1, -1, -1]) + b2[b5 - b6, a2, b5 - b6, DP - 1] + function.get_value(
                       b12 - b5 + 1, b2[b12 - b5 + 1 - 1, a2 - 1, 0, DP - 1]))
    if a1 >= b13:
        b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], b13)
def fonk4(b12, a2, b5, DP, b7, obj_compare):
    global b24
    global b11
    global b25
    global b2
    global b3
    global b4
    if b7 = = 'Rough':
        if b24.b8 = = "bit" and b24.branch_num_of_sbox == 2:
            return 0
        else:
            if b4[b12 - 1, a2 - 1, b5 - 1, DP - 1] == 0:
                if b5 = = b12:
                    b9 = {"model_goal": "LBAS", "model_round": b12, "const_diff": ["diff_pattern_front", b12,
                                                                                        b24.diff_pattern_all[DP - 1]],
                                   "const_sbox": [[1, b12 - 1, a2]], "obj_compare": 0}
                elif 1 <= b5 < b12:
                    b9 = {"model_goal": "LBAS", "model_round": b12, "const_diff": ["diff_pattern_next", b5,
                                                                                        b24.diff_pattern_all[DP - 1]],
                                   "const_sbox": [[1, b5 - 1, a2], [b5 + 1, b12, a2]], "obj_compare": 0}
                elif b5 = = 0 and DP == 0:
                    b9 = {"model_goal": "LBAS", "model_round": b12, "const_diff": [], "const_sbox": [[1, b12, a2]],
                                   "obj_compare": 0}
                b10 = class_model(b24, b9)
                if b11 = = "AS":
                    b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], b10.model_obj)
                elif b11 = = "DC":
                    b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1],
                                                            b10.model_obj * b24.min_weight_of_sbox)
                b4[b12 - 1, a2 - 1, b5 - 1, DP - 1] = 1
                for r2 in range(b12 + 1, b25 + 1):
                    if b5 = = b12:
                        fonk2(r2, a2, r2, DP)
                    elif 1 <= b5 <= b12:
                        fonk2(r2, a2, b5, DP)
                with open("b22/" + b24.name + "/" + b11 + "/solved_LBAS_model.txt", "a") as f:
                    f.write("%s: %d\n" % (b9, b10.model_obj))
    elif b7 = = 'Tightest':
        if b3[b12 - 1, a2 - 1, b5 - 1, DP - 1] == 0:
            if b5 = = b12:
                b9 = {"model_goal": b11, "model_round": b12, "const_diff": ["diff_pattern_front", b12,
                                                                                     b24.diff_pattern_all[DP - 1]],
                               "const_sbox": [[1, b12 - 1, a2]], "obj_compare": obj_compare}
            elif 1 <= b5 < b12:
                b9 = {"model_goal": b11, "model_round": b12, "const_diff": ["diff_pattern_next", b5,
                                                                                     b24.diff_pattern_all[DP - 1]],
                               "const_sbox": [[1, b5 - 1, a2], [b5 + 1, b12, a2]], "obj_compare": obj_compare}
            elif b5 = = 0 and DP == 0:
                b9 = {"model_goal": b11, "model_round": b12, "const_diff": [], "const_sbox": [[1, b12, a2]],
                               "obj_compare": obj_compare}
            b10 = class_model(b24, b9)
            b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], b10.model_obj)
            b3[b12 - 1, a2 - 1, b5 - 1, DP - 1] = 1
            for r2 in range(b12 + 1, b25 + 1):
                if b5 = = b12:
                    fonk2(r2, a2, r2, DP)
                elif 1 <= b5 <= b12:
                    fonk2(r2, a2, b5, DP)
            with open("b22/" + b24.name + "/" + b11 + "/solved_model.txt", "a") as f:
                f.write("%s: %d\n" % (b9, b10.model_obj))
def fonk5(b12):
    global b24
    global b11
    global b1
    global b2
    global b13
    global b21
    if b12 = = 1:
        fonk6(b12)
        fonk4(b12, 0, 0, 0, 'Tightest', 25600)
        b1[b12 - 1] = b2[b12 - 1, -1, -1, -1]
    else:
        b13 = fonk7(b12)
        fonk6(b12)
        fonk8(b12)
        fonk11(b12)
        b1[b12 - 1] = b13
    with open("b22/" + b24.name + "/" + b11 + "/" + str(b12) + "_round_search_result.txt", "a") as f:
        f.write("From all of above, we obtain an optimal objective value:%d.\n" % (b1[b12 - 1]))
    b2[b12 - 1] = np.maximum(b2[b12 - 1], b1[b12 - 1])
def fonk6(b12):
    global b24
    global b11
    global b25
    global b2
    for a2 in [0, 1]:
        fonk2(b12, a2, 0, 0)
        max_num_of_round_to_solve_lbas, b14 = b24.get_max_num_of_round_to_solve(b11)
        if b12 <= max_num_of_round_to_solve_lbas:
            fonk4(b12, a2, 0, 0, 'Rough', 0)
        if b12 <= b14 and a2 > 0:
            fonk4(b12, a2, 0, 0, 'Tightest', 0)
def fonk7(b12):
    global b24
    global b11
    b15 = {"model_goal": b11, "model_round": b12, "const_diff": [], "const_sbox": "get_upperbound_1",
                     "obj_compare": 25600}
    b16 = class_model(b24, b15)
    b17 = b16.model_obj
    b18 = {"model_goal": b11, "model_round": b12, "const_diff": [], "const_sbox": "get_upperbound_2",
                     "obj_compare": b17}
    b19 = class_model(b24, b18)
    b20 = b19.model_obj
    with open("b22/" + b24.name + "/" + b11 + "/" + str(b12) + "_round_search_result.txt", "a") as f:
        f.write("initialized b13 = min(%d,%d)=%d.\n" % (b17, b20,
                                                               min(b17, b20)))
    return min(b17, b20)
def fonk8(b12):
    global b24
    global b11
    global b2
    global b13
    global b21
    b21 = function.get_search_round(b12)
    a2 = 0
    for b5 in b21:
        for DP in range(1, 1 + b24.num_of_diff_pattern_all):
            b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], b2[b12 - 1, a2 - 1, -1, -1])
            fonk2(b12, a2, b5, DP)
            fonk3(b12, a2, b5, DP)
            if b2[b12 - 1, 0 - 1, b5 - 1, DP - 1] < b13:
                fonk9(b12, a2, b5, DP)
                if b2[b12 - 1, 0 - 1, b5 - 1, DP - 1] < b13:
                    b13 = b2[b12 - 1, -1, b5 - 1, DP - 1]
                    with open("b22/" + b24.name + "/" + b11 + "/" + str(
                            b12) + "_round_search_result.txt", "a") as f:
                        f.write("*****************************************************************\n")
                        f.write("(*_*) We update b13 = b2[%d,%d,%d,%d] = %d. \n" % (
                            b12, 0, b5, DP, b2[b12 - 1, -1, b5 - 1, DP - 1]))
                        f.write("*****************************************************************\n")
def fonk9(b12, a2, b5, DP):
    global b24
    global b11
    global b25
    global b2
    global b13
    global b21
    global b6
    for b7 in ['Rough', 'Tightest']:
        a3 = 2
        while a3 <= max(b5, b12 - b5 + 1) and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
            if b5 = = b21[0]:
                if a3 <= b12 - b5 + 1:
                    fonk4(a3, a2, 1, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
                if a3 <= b5 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2, a3, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
            elif b5 < b21[0]:
                if a3 <= b5 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2, a3, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
                    fonk3(b12, a2, b5, DP)
                if a3 <= b6 - b5 + 1 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2 + 1, 1, DP, b7, 0)
                    fonk3(b12, a2, b5, DP)
                if a3 <= b12 - b5 + 1 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2, 1, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
            elif b5 > b21[0]:
                if a3 <= b12 - b5 + 1:
                    fonk4(a3, a2, 1, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
                    fonk3(b12, a2, b5, DP)
                if a3 <= b5 - b6 + 1 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2 + 1, a3, DP, b7, 0)
                    fonk3(b12, a2, b5, DP)
                if a3 <= b5 and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
                    fonk4(a3, a2, a3, DP, b7, 0)
                    fonk2(b12, a2, b5, DP)
            a3 = a3 + 1
        if b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
            fonk4(b12, a2, b5, DP, b7, b13)
        if b7 = = 'Rough' and b5 != b21[0] and b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] < b13:
            fonk10(b12, a2, b5, DP)
def fonk10(b12, a2, b5, DP):
    global b24
    global b11
    global b2
    global b13
    global b21
    global b6
    if b24.b8 = = 'bit' and b24.branch_num_of_sbox == 2:
        return 0
    else:
        if b5 < b21[0]:
            b9 = {"model_goal": "LBAS", "model_round": b12,
                           "const_diff": ["diff_pattern_next", b5, b24.diff_pattern_all[DP - 1]],
                           "const_sbox": [[1, b5, a2], [b5 + 1, b6, a2 + 1], [b6 + 1, b12, a2]], "obj_compare": 0}
        elif b5 > b21[0]:
            b9 = {"model_goal": "LBAS", "model_round": b12,
                           "const_diff": ["diff_pattern_next", b5, b24.diff_pattern_all[DP - 1]],
                           "const_sbox": [[1, b6 - 1, a2], [b6, b5 - 1, a2 + 1], [b5, b12, a2]], "obj_compare": 0}
        b10 = class_model(b24, b9)
        with open("b22/" + b24.name + "/" + b11 + "/solved_LBAS_model.txt", "a") as f:
            f.write("%s: %d\n" % (b9, b10.model_obj))
        if b11 = = "AS":
            b22 = b10.model_obj
        elif b11 = = "DC":
            b22 = b10.model_obj * b24.min_weight_of_sbox
        if b22 >= b13:
            b2[b12 - 1, a2 - 1, b5 - 1, DP - 1] = max(b2[b12 - 1, a2 - 1, b5 - 1, DP - 1], b13)
def fonk11(b12):
    global b25
    global b13
    a2 = 1
    if b2[b12 - 1, a2 - 1, -1, -1] < b13:
        for b7 in ['Rough', 'Tightest']:
            a3 = 1
            while a3 <= b12 and b2[b12 - 1, a2 - 1, -1, -1] < b13:
                fonk4(a3, a2, 0, 0, b7)
                for r2 in range(a3 + 1, b25 + 1):
                    fonk2(r2, a2, 0, 0)
                a3 = a3 + 1
        b13 = min(b13, b2[b12 - 1, a2 - 1, -1, -1])
if b23 = = "__main__":
    global b24
    global b11
    global b25
    global b1
    b24 = parameter.b24
    b11 = parameter.b11
    b25 = b24.get_search_round(b11)
    b26 = []
    function.gen_filefolder(b24.name, b11)
    with open("b22/" + b24.name + "/" + b11 + "/" + "solved_LBAS_model.txt", "w") as f:
        f.write("models we solved:\n")
    with open("b22/" + b24.name + "/" + b11 + "/" + "solved_model.txt", "w") as f:
        f.write("models we solved:\n")
    fonk1()
    for b12 in range(1, b25 + 1):
        b27 = time.time()
        fonk5(b12)
        b28 = time.time()
        b26.append(b28 - b27)
        with open("b22/" + b24.name + "/" + b11 + "/" + "search_time.txt", "a") as f:
            f.write("search %d round: %fs.\n" % (b12, b28 - b27))
    with open("b22/" + b24.name + "/" + b11 + "/" + "search_time.txt", "a") as f:
        f.write("total time is %fs.\n" % sum(b26))